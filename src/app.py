from modules.data_processing.processing import SpreadSheet
from modules.service.connection import Client
from modules.logger.logger import setup_logger


def main():
    setup_logger()
    spreadsheet_id = "1CFZMCweRllZ5jkGm61EmkZStJPXnlbMnsn7O0zaOUOE"
    range_name = ["engenharia_de_software!A2", "engenharia_de_software!A4:F27"]

    connection = Client()
    connection.get_credentials()
    connection.call_api()

    spreadsheet = SpreadSheet(spreadsheet_id)
    spreadsheet.get_sheet(connection.service)
    spreadsheet.batch_get_values(range_name)
    ent_values = spreadsheet.process_sheet()

    spreadsheet.update_values("engenharia_de_software!G4", ent_values)


if __name__ == "__main__":
    main()
