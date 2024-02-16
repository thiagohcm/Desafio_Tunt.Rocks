from modules.data_processing.processing import SpreadSheet
from modules.service.connection import Client
from modules.logger.logger import setup_logger


def main():
    # Logger setup
    setup_logger()

    # Defines spreadsheet_id
    spreadsheet_id = "1CFZMCweRllZ5jkGm61EmkZStJPXnlbMnsn7O0zaOUOE"
    # Defines the range for getting the data (First the range to get the row with the number of classes,
    # second the row only with data)
    range_name = ["engenharia_de_software!A2", "engenharia_de_software!A4:F27"]

    # Instantiation of Client object
    connection = Client()
    # Load the credentials from service account file
    connection.get_credentials()
    # Calls the Sheets API to build the service
    connection.call_api()

    # Instantiation of SpreadSheet object
    spreadsheet = SpreadSheet(spreadsheet_id)
    # Get the sheet from the service builted
    spreadsheet.get_sheet(connection.service)
    # Gets multiples values from sheet to process the data
    spreadsheet.batch_get_values(range_name)
    # Calls process_sheet method to process the data and returns the new values
    ent_values = spreadsheet.process_sheet()

    # Update the Google spreadsheet with the new values
    spreadsheet.update_values("engenharia_de_software!G4", ent_values)


if __name__ == "__main__":
    main()
