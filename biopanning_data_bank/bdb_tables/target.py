from biopanning_data_bank.bdb_tables.tables import (
        BDB_Entry, BDB_Database)
from biopanning_data_bank.bdb_tables.fields import (
	    TARGET_FIELDS)



class TargetDatabase(BDB_Database):

    def __init__(self, entries):
        self.fields = TARGET_FIELDS
        super().__init__(entries)


class Target(BDB_Entry):
    """
    Target entry container from Biopanning Data Bank Target Database.
    """
    def __init__(self, tree):
    	self.fields = TARGET_FIELDS
    	super().__init__(tree)