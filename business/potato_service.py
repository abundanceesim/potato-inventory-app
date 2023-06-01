# potato_service.py by Abundance Esim
import sys
sys.path.append("./persistence")
from data_store import DataStore

class PotatoService:
    """
    This class contains the business logic for the application. It makes use of functions from the 
    persistence layer which acts as a DAO.
    Attributes
    ----------
    dataStore: DataStore
        Reference to the DataStore class
    potatoRecordList: list
        List that contains the potato records retrieved from CSV file

    """

    def __init__(self):
        """
        Constructs all the necessary attributes for a PotatoService object.
        """
        self.dataStore = DataStore('32100358.csv')
        self.potatoRecordList = []
        self.sweetPotatoRecordList = []

    def loadCSV(self):
        """
        Load CSV data into memory from CSV file.
        """
        self.potatoRecordList = self.dataStore.loadCSV()
        self.sweetPotatoRecordList = self.dataStore.sweetPotatoRecordList

    def displayOne(self):
        """
        Display one potato record. The index of the record to be displayed is based
        on the user's input.
        """
        try:
            index = int(input('Please enter the index of the potato record to be displayed (1-100): '))
            self.dataStore.displayOne(index, self.potatoRecordList)
        except IOError as err:
            print(err)

    def displayMultiple(self, rowCount):
        """
        Display multiple potato records based on the row count specified by the user. 
        :param rowCount: The number of rows to be displayed.
        """
        self.dataStore.displayMultiple(rowCount, self.potatoRecordList)

    def displayAll(self):
        """
        Display all potato records from list.
        """
        self.dataStore.displayAll(self.potatoRecordList)
    
    def displayFormattedList(self):
        """
        Display formatted sweet potato records from list.
        """
        self.dataStore.displayAll(self.sweetPotatoRecordList)
        
    def writeCSV(self):
        """
        Write new CSV file using the data from the old CSV file that is currently
        stored in memory.
        """
        if self.potatoRecordList:
            try:
                file_name = input('Enter the file name for your output file: ')
                self.dataStore.writeNewCSV(file_name)
                print(f'Output file "{file_name}".csv created.')
            except IOError as err:
                print(err)
        else:
            print('In order to run this, you must first load CSV file (Option 1).')

    def deleteRecord(self):
        """
        Delete a potato record from the list.
        """
        try:
            index = int(input('Enter index of the potato record: '))
            deleted = self.dataStore.deletePotato(self.potatoRecordList, index)
            if deleted:
                print(f'[{deleted}] deleted.')
        except:
            print('Invalid input. Expected input type: int')

    def editRecord(self):
        """
        Edit a potato record at a specific index. It accepts user input and passes
        these as arguments to the method from the data store.
        """
        # index: int, ref_date, geo, dguid, area_production_value, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals
        try:
            index = int(input('Enter index for potato record to be edited: '))
            ref_date = input('Enter ref_date value: ')
            geo = input('Enter geo value: ')
            dguid = input('Enter dguid value: ')
            area_production_value = input('Enter area production and farm value: ')
            uom = input('Enter UOM value: ')
            uom_id = input('Enter UOM ID value: ')
            scalar_factor = input('Enter scalar factor value: ')
            scalar_id = input('Enter scalar ID value: ')
            vector = input('Enter vector value: ')
            coordinate = input('Enter coordinate value: ')
            value = input('Enter value of potato: ')
            status = input('Enter status value: ')
            symbol = input('Enter symbol value: ')
            terminated = input('Enter terminated value: ')
            decimals = input('Enter decimals value: ')

            potato = self.dataStore.editPotato(self.potatoRecordList, index, ref_date, geo, dguid, area_production_value, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
            if potato:
                print(f'[{potato}] modified.')
        except IOError as err:
            print(err)


    def createRecord(self):
        """
        Create a potato record and append it to the existing list. It accepts user
        input and passes these as arguments to method of the datastore.
        """
        # ref_date, geo, dguid, area_production_value, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals
        try:
            ref_date = input('Enter ref_date value: ')
            geo = input('Enter geo value: ')
            dguid = input('Enter dguid value: ')
            area_production_value = input('Enter area production and farm value: ')
            uom = input('Enter UOM value: ')
            uom_id = input('Enter UOM ID value: ')
            scalar_factor = input('Enter scalar factor value: ')
            scalar_id = input('Enter scalar ID value: ')
            vector = input('Enter vector value: ')
            coordinate = input('Enter coordinate value: ')
            value = input('Enter value of potato: ')
            status = input('Enter status value: ')
            symbol = input('Enter symbol value: ')
            terminated = input('Enter terminated value: ')
            decimals = input('Enter decimals value: ')

            potato = self.dataStore.createPotato(self.potatoRecordList, ref_date, geo, dguid, area_production_value, uom, uom_id,
                                            scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
            print(f'Potato [{potato}] created.')
        except IOError as err:
            print(err)

    def createBarChart(self, x_value, y_value):
        """
        Create a bar chart based on the user's column choices.
        """
        # list of dictionaries containing menu options and corresponding values
        options = [
            {'option': 1, 'value': 'uom_id'},
            {'option': 2, 'value': 'geo'},
            {'option': 3, 'value': 'coordinate'},
            {'option': 4, 'value': 'scalar_factor'}
        ]

        x_column = ''
        y_column = ''

        # the bar chart should only be created if there are two distinct values for x and y
        if (x_value != y_value):
            for optionObj in options:
                if (x_value == optionObj['option']):
                    x_column = optionObj['value']
                    
                if (y_value == optionObj['option']):
                    y_column = optionObj['value']
                    
            print(f'x_column: {x_column}')
            print(f'y_column: {y_column}')
            self.dataStore.createBarChart(self.potatoRecordList, x_column, y_column)
        else:
            print('Bar chart cannot contain same column on both axes')