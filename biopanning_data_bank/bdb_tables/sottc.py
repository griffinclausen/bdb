from biopanning_data_bank.bdb_tables.tables import (
        BDB_Entry, BDB_Database)
from biopanning_data_bank.bdb_tables.fields import (
	    SOTTC_FIELDS)


class SOTTCDatabase(BDB_Database):
    pass

class SOTTC(BDB_Entry):
    """
    SOTTC entry container from Biopanning Data Bank SOTTC Database.
    """
    
    def __init__(self, tree):
    	self.fields = SOTTC_FIELDS
    	super().__init__(tree)