from biopanning_data_bank.bdb_tables.tables import (
        BDB_Entry, BDB_Database)
from biopanning_data_bank.bdb_tables.fields import (
	    SOC_FIELDS)


class SOCDatabase(BDB_Database):
    pass


class SOC(BDB_Entry):
    """
    SOC entry container from Biopanning Data Bank SOC Database.
    """
    
    def __init__(self, tree):
    	self.fields = SOC_FIELDS
    	super().__init__(tree)
