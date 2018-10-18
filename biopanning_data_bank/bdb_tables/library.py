from biopanning_data_bank.bdb_tables.tables import (
        BDB_Entry, BDB_Database)
from biopanning_data_bank.bdb_tables.fields import (
        LIBRARY_FIELDS)


class LibraryDatabase(BDB_Database):

    def __init__(self, entries):
        self.fields = LIBRARY_FIELDS
        super().__init__(entries)


class Library(BDB_Entry):
    """
    Library entry container from Biopanning Data Bank Mimoset Database.
    """

    def __init__(self, tree):
        self.fields = LIBRARY_FIELDS
        super().__init__(tree)
