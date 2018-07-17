from biopanning_data_bank.bdb_tables.tables import (
        BDB_Entry, BDB_Database)
from biopanning_data_bank.bdb_tables.fields import (
	    TEMPLATE_FIELDS)


class TemplateDatabase(BDB_Database):
    pass


class Template(BDB_Entry):
    """
    Template entry container from Biopanning Data Bank Template Database.
    """
    def __init__(self, tree):
    	self.fields = TEMPLATE_FIELDS
    	super().__init__(tree)