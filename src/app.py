from modules.data_processing.processing import SpreadSheet
from modules.service.connection import Client
from modules.logger.logger import setup_logger


def main():
    # Setup logger configurations
    setup_logger()

    # Define spreadsheet_id
    spreadsheet_id = "1CFZMCweRllZ5jkGm61EmkZStJPXnlbMnsn7O0zaOUOE"
    # Define the range for getting the data
    range_name = ["engenharia_de_software!A2", "engenharia_de_software!A4:F27"]

    # Instantiation of Client object
    connection = Client()
    # Load the credentials from service account file
    connection.get_credentials()
    # Call the Sheets API to build the service
    connection.call_api()

    # Instantiation of SpreadSheet object
    spreadsheet = SpreadSheet(spreadsheet_id)
    # Get the sheet from the service builted
    spreadsheet.get_sheet(connection.service)
    # Get multiples values from sheet to process data
    spreadsheet.batch_get_values(range_name)
    # Process data and stores in ent_values
    ent_values = spreadsheet.process_sheet()

    # Update the Google spreadsheet with the new values
    spreadsheet.update_values("engenharia_de_software!G4", ent_values)


if __name__ == "__main__":
    main()
