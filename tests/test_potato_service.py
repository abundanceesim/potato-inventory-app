# test_potato_service.py by Abundance Esim
import sys
sys.path.append("./model")
sys.path.append("./business")
from potato_service import PotatoService
from potato_record import PotatoRecord, SweetPotatoRecord

def test_is_subclass():
    """
    This test validates that SweetPotatoRecord class(child class) is a subclass of PotatoRecord (parent class).
    """
    assert issubclass(SweetPotatoRecord, PotatoRecord)


def test_load_csv():
    """
    This test validates the functionality of the loadCSV() function of the PotatoService class.
    """
    potato_service = PotatoService()
    potatoList = potato_service.potatoRecordList
    # Original size of empty list
    list_size = potatoList.__len__()

    potato_service.loadCSV()
    potatoList = potato_service.potatoRecordList
    # List size after loadCSV() has been called.
    list_size = potatoList.__len__()

    assert list_size == 100
