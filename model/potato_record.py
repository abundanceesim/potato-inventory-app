# potato_record.py by Abundance Esim
class PotatoRecord:
    """
    A class to represent a potato record. This class would be used for the instantiation of PotatoRecord objects
    which would contain records read from the CSV file. File created by Abundance Esim

    Attributes
    ----------
    ref_date : int
        Reference date for the potato
    geo : str
        Location where potato is found
    dguid : str
        DGUID of potato
    area_production_value : str
        Area, production and farm value of potatoes
    uom : str
        UOM of potato
    uom_id : int
        UOM ID of potato
    scalar_factor : int
        Scalar factor for the potato
    scalar_id : int
        Scalar ID of the potato
    vector : str
        Vector value for the potato
    coordinate : float
        Coordinate value of the potato
    value : float
        Value of the potato
    status : str
        Status of the potato
    symbol : str
        Symbol representing the potato
    terminated : str
        Date when potato record was terminated
    decimals : int
        Decimals of potato values

    """

    def __init__(self,
                 ref_date,
                 geo,
                 dguid,
                 area_production_value,
                 uom,
                 uom_id,
                 scalar_factor,
                 scalar_id,
                 vector,
                 coordinate,
                 value,
                 status,
                 symbol,
                 terminated,
                 decimals
                 ):
        """
        Constructs all the necessary attributes for a PotatoRecord object

        Parameters
        ----------
        ref_date : int
            Reference date for the potato
        geo : str
            Location where potato is found
        dguid : str
            DGUID of potato
        area_production_value : str
            Area, production and farm value of potatoes
        uom : str
            UOM of potato
        uom_id : int
            UOM ID of potato
        scalar_factor : int
            Scalar factor for the potato
        scalar_id : int
            Scalar ID of the potato
        vector : str
            Vector value for the potato
        coordinate : float
            Coordinate value of the potato
        value : float
            Value of the potato
        status : str
            Status of the potato
        symbol : str
            Symbol representing the potato
        terminated : str
            Date when potato record was terminated
        decimals : int
            Decimals of potato values        
            
        """         
        self.ref_date = ref_date
        self.geo = geo 
        self.dguid = dguid
        self.area_production_value = area_production_value
        self.uom = uom
        self.uom_id = uom_id
        self.scalar_factor = scalar_factor
        self.scalar_id = scalar_id
        self.vector = vector
        self.coordinate = coordinate
        self.value = value
        self.status = status
        self.symbol = symbol
        self.terminated = terminated
        self.decimals = decimals

    def get_ref_date(self):
        """
        Accessor for ref_date
        :returns: ref_date
        """
        return self.ref_date

    def set_ref_date(self, ref_date):
        """
        Mutator for ref_date
        :param int ref_date: Reference date for the potato
        """
        self.ref_date = ref_date

    def get_geo(self):
        """
        Accessor for geo
        :returns: geo
        """
        return self.geo

    def set_geo(self, geo):
        """
        Mutator for geo
        :param str geo: Location where potato is found
        """
        self.geo = geo

    def get_dguid(self):
        """
        Accessor for dguid
        :returns: dguid
        """
        return self.dguid

    def set_dguid(self, dguid):
        """
        Mutator for dguid
        :param str dguid: DGUID of potatoes
        """
        self.dguid = dguid

    def get_area_production_value(self):
        """
        Accessor for area_production_value
        :returns: area_production_value
        """
        return self.area_production_value

    def set_area_production_value(self, area_production_value):
        """
        Mutator for area_production_value
        :param str area_production_value: Area, production and farm value of potatoes
        """
        self.area_production_value = area_production_value

    def get_uom(self):
        """
        Accessor for uom
        :returns: uom
        """
        return self.uom

    def set_uom(self, uom):
        """
        Mutator for uom
        :param str: UOM of potatoes
        """
        self.uom = uom

    def get_uom_id(self):
        """
        Accessor for uom_id
        :returns: uom_id
        """
        return self.uom_id

    def set_uom_id(self, uom_id):
        """
        Mutator for uom_id
        :param int uom_id: UOM ID of potatoes
        """
        self.uom_id = uom_id

    def get_scalar_factor(self):
        """
        Accessor for scalar_factor
        :returns: scalar_factor
        """
        return self.scalar_factor

    def set_scalar_factor(self, scalar_factor):
        """
        Mutator for scalar_factor
        :param int scalar_factor: Scalar factor for the potato
        """
        self.scalar_factor = scalar_factor

    def get_scalar_id(self):
        """
        Accessor for scalar_id        
        :returns: scalar_id
        """
        return self.scalar_id

    def set_scalar_id(self, scalar_id):
        """
        Mutator for scalar_id
        :param int scalar_id: Scalar ID of the potato
        """
        self.scalar_id = scalar_id

    def get_vector(self):
        """
        Accessor for vector  
        :returns: vector
        """
        return self.vector

    def set_vector(self, vector):
        """
        Mutator for vector
        :param str vector: Vector value for the potato
        """
        self.vector = vector

    def get_coordinate(self):
        """
        Accessor for coordinate   
        :returns: coordinate
        """
        return self.coordinate

    def set_coordinate(self, coordinate):
        """
        Mutator for coordinate
        :param float coordinate: Coordinate value of the potato
        """
        self.coordinate = coordinate

    def get_value(self):
        """
        Accessor for value    
        :returns: value
        """
        return self.value

    def set_value(self, value):
        """
        Mutator for value
        :param float value: Value of the potato
        """
        self.value = value

    def get_status(self):
        """
        Accessor for status 
        :returns: status
        """
        return self.status

    def set_status(self, status):
        """
        Mutator for status
        :param str status: Status of the potato
        """
        self.status = status

    def get_symbol(self):
        """
        Accessor for symbol  
        :returns: symbol
        """
        return self.symbol

    def set_symbol(self, symbol):
        """
        Mutator for symbol
        :param str symbol: Symbol representing the potato
        """
        self.symbol = symbol

    def get_terminated(self):
        """
        Accessor for terminated  
        :returns: terminated
        """
        return self.terminated

    def set_terminated(self, terminated):
        """
        Mutator for terminated
        :param str terminated: Date when potato record was terminated 
        """
        self.terminated = terminated

    def get_decimals(self):
        """
        Accessor for decimals    
        :returns: decimals
        """
        return self.decimals

    def set_decimals(self, decimals):
        """
        Mutator for decimals
        :param int decimals: Decimals of potato values
        """
        self.decimals = decimals

    def __repr__(self):
        """
        Format string representation of PotatoRecord objects
        """
        return str(self.ref_date) + ", " + str(self.geo) + ", " + str(self.dguid) + ", " + \
            str(self.area_production_value) + ", " + str(self.uom) + ", " + str(self.uom_id) + ", " + \
            str(self.scalar_factor) + ", " + str(self.scalar_id) + ", " +  str(self.vector) + ", " + \
            str(self.coordinate) + ", " + str(self.value) + ", " + str(self.status) + ", " + \
            str(self.symbol) + ", " + str(self.terminated) + ", " + str(self.decimals)
    


class SweetPotatoRecord(PotatoRecord):
    """
    A subclass of PotatoRecord to override the format of a potato record. Created by Abundance Esim.
    """
    def __repr__(self):
        """
        Overridden method to format string representation of SweetPotatoRecord objects.
        Written by Abundance Esim.
        """
        return str(self.ref_date) + " ⇒ " + str(self.geo) + " ⇒ " + str(self.dguid) \
            + " ⇒ " + str(self.area_production_value) + " ⇒ " + str(self.uom) + " ⇒ " + str(self.uom_id) + " ⇒ " + \
            str(self.scalar_factor) + " ⇒ " + str(self.scalar_id) + " ⇒ " + str(self.vector) + " ⇒ " + \
            str(self.coordinate) + " ⇒ " + str(self.value) + " ⇒ " + str(self.status) + " ⇒ " + \
            str(self.symbol) + " ⇒ " + str(self.terminated) + " ⇒ " + str(self.decimals)
