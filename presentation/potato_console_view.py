# potato_console_view.py by Abundance Esim
import os
import sys
sys.path.append("./business")
from potato_service import PotatoService

class PotatoConsoleView:
    """
    This class is the presentation layer of the application. It displays an interactive
    menu where the user can select options and get results based on their choice.
    File created by Abundance Esim.

    Attributes
    ----------
    potatoService: PotatoService
        Reference to PotatoService class which contains methods that will
        be called depending on the user's choice of menu options.
    RELOAD_DATASET: str
        String constant that represents the first menu option.
    WRITE_NEW_CSV: str
        String constant that represents the second menu option.
    SELECT_POTATOES: str
        String constant that represents the third menu option.
    CREATE_NEW_RECORD: str
        String constant that represents the fourth menu option.
    EDIT_RECORD: str
        String constant that represents the fifth menu option.
    DELETE_RECORD: str
        String constant that represents the sixth menu option.
    DISPLAY_ALL: str
        String constant that represents the seventh menu option.

    """

    def __init__(self):
        """
        Constructs all the necessary attributes for a PotatoConsoleView object.
        """
        self.potatoService = PotatoService()
        self.RELOAD_DATASET = '1'
        self.WRITE_NEW_CSV = '2'
        self.SELECT_POTATOES = '3'
        self.CREATE_NEW_RECORD = '4'
        self.EDIT_RECORD = '5'
        self.DELETE_RECORD = '6'
        self.DISPLAY_ALL = '7'
        self.DISPLAY_FORMATTED = '8'
        self.CREATE_BAR_CHART = '9'
        self.shouldContinue = True

    def startup(self):
        """
        Function called to startup the application.
        """
        self.display_menu()

    def display_menu(self):
        """
        Function that displays the interactive menu to the user on application
        startup.
        """
        os.system('cls')
        while (self.shouldContinue == True):
            
            print('Potato Inventory Application by Abundance Esim')
            print('1. Reload data from CSV file (Do this first to enable the functionality of the application)')
            print('2. Create new CSV file with data from existing CSV')
            print('3. Display one or multiple potato records')
            print('4. Create new potato record')
            print('5. Edit potato record')
            print('6. Delete potato record')
            print('7. Display all potato records')
            print('8. Display all sweet potato records (formatted)')
            print('9. Create a vertical bar chart with potato data')
            print()

            self.process_response()
            print('Program by Abundance Esim')

            continue_program = input('Continue? (Y/N): ')
            print()
            self.continueProgram(continue_program)

    def continueProgram(self, response:str):
        """
        This function determines whether or not the program should be re-run.
        :param response: The user's response for whether or not the program
                            should be re-run.
        """
        if response.lower() == 'y':
            os.system('cls')
            self.shouldContinue = True
        else:
            print('Application terminated.')
            print('Program by Abundance Esim')
            self.shouldContinue = False

    def process_response(self):
        """
        Process user's response by calling the appropriate functions.
        """
        selected_option = input('Please select option: ')
        match selected_option:
            case self.RELOAD_DATASET:
                self.loadCSV()
                print('CSV data reloaded. All existing in-memory data replaced.')
            case self.WRITE_NEW_CSV:
                self.writeNewCSV()
            case self.SELECT_POTATOES:
                self.displayPotatoes()
            case self.CREATE_NEW_RECORD:
                self.createPotato()
            case self.EDIT_RECORD:
                self.editPotato()
            case self.DELETE_RECORD:
                self.deletePotato()
            case self.DISPLAY_ALL:
                self.displayAll()
            # Project by Abundance Esim
            case self.DISPLAY_FORMATTED:
                self.displayFormatted()
            # Project by Abundance Esim    
            case self.CREATE_BAR_CHART:
                self.createBarChart()
            case _:
                print('Invalid option entered. Valid options are 1 - 8')
                       
        print()

    def loadCSV(self):
        """
        Load data from the CSV file into memory.
        """
        self.potatoService.loadCSV()

    def writeNewCSV(self):
        """
        Create a new CSV file using data in memory.
        """
        self.potatoService.writeCSV()

    def displayPotatoes(self):
        """
        Display a certain number of potato records. Depending on the user's input, the
        appropriate PotatoService method is called.
        """
        try:
            num_of_potatoes = int(input('Enter the number of potato records to be displayed: '))
            if (num_of_potatoes > 1):
                # Program by Abundance Esim
                self.potatoService.displayMultiple(num_of_potatoes)
            else:
                self.potatoService.displayOne()
        except:
            print('Invalid input. Accepted input type: int')

    def createPotato(self):
        """
        Create a new PotatoRecord object and append it to the list.
        """
        self.potatoService.createRecord()

    def editPotato(self):
        """
        Edit properties of an existing potato record.
        """
        self.potatoService.editRecord()

    def deletePotato(self):
        """
        Delete specific potato record.
        """
        self.potatoService.deleteRecord()

    def displayAll(self):
        """
        Display all potato records currently available in memory.
        """
        self.potatoService.displayAll()

    def displayFormatted(self):
        """
        Display all potato records currently available in memory. Written by
        Abundance Esim
        """
        self.potatoService.displayFormattedList()

    # Modifications for Practical Project 4 by Abundance Esim.
    def createBarChart(self):
        """
        Create a bar chart with 2 columns based on users selection from options.
        Written by Abundance Esim.
        """
        accepted_range = [1, 2, 3, 4]
        try:
            # Display menu containing columns to choose from
            print('1. uom_id')
            print('2. geo')
            print('3. coordinate')
            print('4. scalar_factor')

            x_value = int(input('Please enter number for chart\'s x-axis: '))
            y_value = int(input('Please enter number for chart\'s y-axis: '))

            if((x_value not in accepted_range) or (y_value not in accepted_range)):
                print('Invalid option(s) selected. Input must be from 1-4.')
            else:
                self.potatoService.createBarChart(x_value, y_value)
        except:
            print('Invalid input. Accepted input type: int')