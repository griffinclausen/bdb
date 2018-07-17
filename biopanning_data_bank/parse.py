import os

import xml.etree.ElementTree as ET

from biopanning_data_bank.config import (
    DATA_DIRECTORY,
    DEFAULT_RELEASE_INDEX)
from biopanning_data_bank.bdb_tables import (
    BDB_ENTRIES,
    BDB_DATABASES)


def get_tree(tablename,
             release_index=DEFAULT_RELEASE_INDEX):
    release_data_directory = os.path.join(DATA_DIRECTORY,
                                          str(release_index))
    input_filepath = os.path.join(release_data_directory,
                                  'processed',
                                  tablename + '.xml')
    tree = ET.parse(input_filepath)
    return tree


def parse_table(tablename,
                release_index=DEFAULT_RELEASE_INDEX):
    tree = get_tree(tablename, release_index)
    root = tree.getroot()
    db = root.find('database')
    entries = []
    for tbl in db:
        entry = BDB_ENTRIES[tablename](tbl)
        entries.append(entry)
    return entries


def parse_all_tables(release_index=DEFAULT_RELEASE_INDEX):
    databases = {}
    for k, v in BDB_DATABASES.items():
        if v is not None:
            entries = parse_table(k)
            database = BDB_DATABASES[k](entries)
            databases[k] = database
    return databases


def main():
    # parse_table('mimoset')
    parse_all_tables()


if __name__ == '__main__':
    main()
