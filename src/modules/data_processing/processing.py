import logging
import math

from googleapiclient.errors import HttpError, Error

logger = logging.getLogger()


class SpreadSheet:
    def __init__(self, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id
        self.sheet = None
        self.values = None

    # Get the spreadsheet of the created service
    def get_sheet(self, service):
        try:
            self.sheet = service.spreadsheets()
            logger.info("Successfully obtained the spreadsheet")
        except Error as error:
            logger.error(f"An error occurred: {error}")

    # Processes the data and stores it in ent_values
    def process_sheet(self):
        values = self.values[1].get("values", [])
        ent_values = []
        for row in values:
            average = self.calc_average(int(row[3]), int(row[4]), int(row[5]))
            situation = self.calc_situation(average, row[2])

            if not situation == "Exame Final":
                ent_values.append([situation, '0'])
            else:
                approval_final_grade = self.calc_approval_final_grade(average)
                ent_values.append([situation, math.ceil(approval_final_grade)])
        logger.info("Processed the values successfully")
        return ent_values

    # Obtains multiple values ​​from the spreadsheet to process data, both the row with the total number of
    # classes and the rows with student data
    def batch_get_values(self, range_names):
        try:
            result = (
                self.sheet
                .values()
                .batchGet(spreadsheetId=self.spreadsheet_id, ranges=range_names)
                .execute()
            )
            ranges = result.get("valueRanges", [])
            logger.info(f"{len(ranges)} ranges retrieved successfully")
            self.values = ranges
        except Error as error:
            logger.error(f"An error occurred: {error}")
            return error

    # Updates the Google spreadsheet with new values
    def update_values(self, range_name, ent_values):
        try:
            self.sheet.values().update(spreadsheetId=self.spreadsheet_id, range=range_name,
                                       valueInputOption="USER_ENTERED", body={'values': ent_values}).execute()
            logger.info("Successfully updated the values")
        except HttpError as error:
            logger.error(f"An error occurred: {error}")

    # Extracts the total number of classes from data
    def get_total_classes(self):
        values = self.values[0].get("values", [])
        return int(values[0][0].partition(":")[2].strip())

    # Calculates student situation based on challenge rules
    def calc_situation(self, average, absence):
        total_classes = self.get_total_classes()
        if int(absence) > total_classes * 0.25:
            return "Reprovado por Falta"
        elif average < 5:
            return "Reprovado por Nota"
        elif 5 <= average < 7:
            return "Exame Final"
        else:
            return "Aprovado"

    # Calculates the average of p1, p2, p3
    @staticmethod
    def calc_average(p1, p2, p3):
        return ((p1 + p2 + p3) / 3) / 10

    # Calculates the approval final grade
    @staticmethod
    def calc_approval_final_grade(average):
        naf = (5 * 2) - average
        return naf * 10
