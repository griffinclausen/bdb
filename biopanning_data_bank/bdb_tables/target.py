from biopanning_data_bank.bdb_tables.tables import (
        BDB_Entry, BDB_Database)
from biopanning_data_bank.bdb_tables.fields import (
	    TARGET_FIELDS)



class TargetDatabase(BDB_Database):
    pass


class Target(BDB_Entry):
    """
    Target entry container from Biopanning Data Bank Target Database.
    """
    def __init__(self, tree):
    	self.fields = TARGET_FIELDS
    	super().__init__(tree)