# data_store.py by Abundance Esim
import matplotlib.pyplot as plt
import csv
import sys
sys.path.append("./model")
from potato_record import PotatoRecord, SweetPotatoRecord

# Data Store 

class DataStore:
    """
    This class is the equivalent of a DataAccessObject in SQL. It connects directly to the CSV
    file and performs CRUD operations on it. It is used by other layers in the application to 
    access the CSV file. File created by Abundance Esim.

    Attributes
    ----------
    file: str
        The name of the CSV file to be used.
    potatoListL: list
        A list containing potato records read directly from the CSV file.
    header: list
        A list containing the column header's columns.
    column_names: list
        Secondary list to store the column names.
    csv_data: list
        List containing CSV data.
    
    """
    def __init__(self, file: str):
        """
        Constructs all the necessary attributes for a DataStore object.
        :param str file: The CSV file to be used throughout application.
        """
        self.file:str = file
        self.potatoList = []
        # self.sweetPotatoList = []
        self.header = []
        self.column_names = []
        self.csv_data = []
        # Project by Abundance Esim
        self.sweetPotatoRecordList: SweetPotatoRecord = []

    def loadCSV(self):
        """
        This function opens, reads and appends CSV data to the appropriate lists. It
        also creates potato record objects and appends them to the appropriate list.
        Written by Abundance Esim
        """
        try:    
            with open(self.file, 'r') as csv_file:
                reader = csv.reader(csv_file)
                self.header = next(reader)
                # Program by Abundance Esim
                potatoRecordList: PotatoRecord = []
                # sweetPotatoRecordList: SweetPotatoRecord = []
                lineCount = 1
                limit = 100
                # Program by Abundance Esim
                for line in reader:
                    if lineCount > limit:
                        break
                    else:
                        self.potatoList.append(line)
                        lineCount += 1

                for i in range(15):
                    for potatoLine in self.potatoList:
                        potatoLine[i] = '\'' + potatoLine[i] + '\''
                        # Handling null values
                        if (potatoLine[i] == '\'\'') or (not potatoLine[i]):
                            potatoLine[i] = "null"
                            # Project by Abundance Esim

                for potato in self.potatoList:
                    # Modifications for Project 3:
                    sweetPotatoObj = SweetPotatoRecord(potato[0], potato[1], potato[2], potato[3], potato[4], potato[5],
                                                       potato[6], potato[7], potato[8], potato[9], potato[10], potato[11],
                                                       potato[12], potato[13], potato[14])
                    # Program by Abundance Esim
                    self.sweetPotatoRecordList.append(sweetPotatoObj)

                    # Create a PotatoRecord object for each row in potatoList
                    potatoObj = PotatoRecord(potato[0], potato[1], potato[2], potato[3], potato[4], potato[5],
                                            potato[6], potato[7], potato[8], potato[9], potato[10], potato[11],
                                            potato[12], potato[13], potato[14])
                    # Program by Abundance Esim
                    potatoRecordList.append(potatoObj)

                for column in self.header:
                    self.column_names.append(column)
                
                for line in reader:
                    self.csv_data.append(line)

                return potatoRecordList
        except IOError as err:
            print(err)

    def writeNewCSV(self, new_csv):
        """
        Create a new CSV file by writing data loaded using the loadCSV() function to 
        a separate file.
        
        :param new_csv: The name of the new CSV file to be created.
        """
        try:
            new_csv += '.csv'
            with open(new_csv, 'w', newline='') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=',')
                writer.writerow(self.header)
                for potatoRow in self.csv_data:
                    writer.writerow(potatoRow)
                # Program by Abundance Esim
        except IOError as err:
            print(err)

    def displayOne(self, index: int, potatoRecordList):
        if not potatoRecordList:
            print('There are no potato records in memory. Please load CSV file first.')
        else:
            if index > 0 and index < (potatoRecordList.__len__() + 1):
                for potato in potatoRecordList:
                    # if the potato's index matches the index that the user specified, print that specific potato
                    if (potatoRecordList.index(potato)) == (index - 1):  # indexes would be between 0 and 99
                        print(potato)
            else:
                print("Index out of bounds")


    def displayMultiple(self, rowCount, potatoRecordList:list):
        """
        Display multiple potato record objects from the list contatining these objects.
        :param rowCount: The number of records to be displayed.
        :param list potatoRecordList: The list containing the potato records.

        """
        if not potatoRecordList:
            print('There are no potato records in memory. Please load CSV file first.')
        else:
            lineCount = 1
            print(self.column_names)
            for potatoRecord in potatoRecordList:
                if lineCount > rowCount:
                    break
                else:
                    print(f'{lineCount}. {potatoRecord}')
                    lineCount += 1

    def displayAll(self, potatoRecordList):
        """
        Display all records from the potato record list.
        :param: potatoRecordList: The list containing data loaded into memory from the
                CSV file.
        """
        if not potatoRecordList:
            print('There are no potato records in memory. Please load CSV file first.')
        else:
            rowCount = 1
            print(self.column_names)
            for potato in potatoRecordList:
                print(f'{rowCount}. {potato}')
                rowCount += 1

    def createPotato(self, potatoRecordList:list, ref_date, geo, dguid, area_production_value, uom, uom_id, scalar_factor, scalar_id, 
                        vector, coordinate, value, status, symbol, terminated, decimals):

        """
        Create a new PotatoRecord object and append it to the existing potato record list. It accepts arguments which
            are the properties of the PotatoRecord object to be created.
        :param list potatoRecordList: The list containing data loaded into memory from the
                CSV file.
        """
        newPotato:PotatoRecord = PotatoRecord(ref_date, geo, dguid, area_production_value, uom, uom_id, scalar_factor, scalar_id,
                                 vector, coordinate, value, status, symbol, terminated, decimals)
        if potatoRecordList:
            potatoRecordList.append(newPotato)
            return newPotato
        else:
            print('There are no potato records in memory. Please load CSV file first.')

    def editPotato(self, potatoRecordList: list, index: int, ref_date, geo, dguid, area_production_value, uom, uom_id, scalar_factor, scalar_id,
                            vector, coordinate, value, status, symbol, terminated, decimals):

        """
        Edit an existing potato record from the potato record list.It accepts arguments which
            are the properties of the PotatoRecord object to be edited.
        :param list potatoRecordList: The list containing data loaded into memory from the
                CSV file.
        """
        if not potatoRecordList:
            print('There are no potato records in memory. Please load CSV file first.')
        else: 
            potato: PotatoRecord
            if index > 0 and index < (potatoRecordList.__len__() + 1):
                for potato in potatoRecordList:
                    if (potatoRecordList.index(potato)) == (index - 1):

                        potato.set_ref_date(ref_date)
                        potato.set_geo(geo)
                        potato.set_dguid(dguid)
                        potato.set_area_production_value(area_production_value)
                        potato.set_uom(uom)
                        potato.set_uom_id(uom_id)
                        potato.set_scalar_factor(scalar_factor)
                        potato.set_scalar_id(scalar_id)
                        potato.set_vector(vector)
                        potato.set_coordinate(coordinate)
                        potato.set_value(value)
                        potato.set_status(status)
                        potato.set_symbol(symbol)
                        potato.set_terminated(terminated)
                        potato.set_decimals(decimals)

                        return potato

    def deletePotato(self, potatoRecordList:list, index: int):
        """
        Delete specific potato record from list.
        :param list potatoRecordList: The list containing data loaded into memory from the
                CSV file.
        :index: The index of the potato record to be removed from the list.
        """
        if not potatoRecordList:
            print('There are no potato records in memory. Please load CSV file first.')
        else:
            if index > 0 and index < (potatoRecordList.__len__() + 1):
                for potato in potatoRecordList:
                    if (potatoRecordList.index(potato)) == (index - 1):
                        return potatoRecordList.pop(index)
            else:
                print('Index out of bounds.')

    # Modifications for Practical Project 4 by Abundance Esim
    def createBarChart(self, potatoRecordList: list, x_value:str, y_value:str):
        """
        Create a bar chart from two columns of the user's choice retrieved from the
        potato record list. Written by Abundance Esim.
        :param list potatoRecordList: The list containing data loaded into memory from the
                CSV file.
        :param str x_value: The column from which values would be taken to populate the x-axis
        :param str y_value: The column from which values would be taken to populate the y-axis

        """
        # Lists to contain x and y values. Written by Abundance Esim
        x_values = [] 
        y_values = []
        # these lists need to contain exactly the same number of values for the 
        # chart to work
        if not potatoRecordList:
            print('There are no potato records in memory. Please load CSV file first.')
        else:
            potato: PotatoRecord
            # based on the x and y values passed as arguments, we can
            # choose which property to get and append them to the two lists
            # Project by Abundance Esim
            for potato in potatoRecordList:
                if (x_values.__len__() > 15):
                    break
                else:
                    match x_value:
                        case 'uom_id':
                            if(potato.uom_id):
                                x_values.append(potato.uom_id)
                        case 'geo':
                            if(potato.geo):
                                x_values.append(potato.geo)
                        case 'coordinate':
                            if(potato.coordinate):
                                x_values.append(potato.coordinate)
                        case 'scalar_factor':
                            if(potato.scalar_factor):
                                x_values.append(potato.scalar_factor)

                if (y_values.__len__() > 15):
                    break
                else:
                    match y_value:
                        case 'uom_id':
                            if(potato.uom_id):
                                y_values.append(potato.uom_id)
                        case 'geo':
                            if(potato.geo):
                                y_values.append(potato.geo)
                        case 'coordinate':
                            if(potato.coordinate):
                                y_values.append(potato.coordinate)
                        case 'scalar_factor':
                            if(potato.scalar_factor):
                                y_values.append(potato.scalar_factor)

            plt.bar(x_values, y_values)
            plt.xlabel(x_value)
            plt.ylabel(y_value)
            plt.title('Bar chart by Abundance Esim')
            plt.show()