from biopanning_data_bank.bdb_tables.tables import (
        BDB_Entry, BDB_Database)
from biopanning_data_bank.bdb_tables.fields import (
	    SOTMC_FIELDS)


class SOTMCDatabase(BDB_Database):
    pass


class SOTMC(BDB_Entry):
    """
    SOTMC entry container from Biopanning Data Bank SOTMC Database.
    """
    
    def __init__(self, tree):
    	self.fields = SOTMC_FIELDS
    	super().__init__(tree)