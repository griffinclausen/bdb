# import click

from biopanning_data_bank import parse_all_tables


# @click.command()
# @click.argument('i', default=1)
# def cli(i):
#     print('Running Tests' * i)


db = parse_all_tables()

# for k, v in BDB_ENTRIES.items():
#     if v is not None:
#         entries = parse_table(k)

#         print(k)
#         print(len(entries))
#         for entry in entries:
#             print(entry.MimotopeSetID)


# def get_tree(tablename,
#              release_index=DEFAULT_RELEASE_INDEX):
#     release_data_directory = os.path.join(DATA_DIRECTORY,
#                                           str(release_index))
#     input_filepath = os.path.join(release_data_directory,
#                                   'processed',
#                                   tablename + '.xml')
#     tree = ET.parse(input_filepath)
#     return tree


# def parse_table(tablename,
#                 release_index=DEFAULT_RELEASE_INDEX):
#     tree = get_tree(tablename, release_index)
#     root = tree.getroot()
#     db = root.find('database')
#     entries = []
#     for tbl in db:
#         entry = BDB_ENTRIES[tablename](tbl)
#         entries.append(entry)
#     return entries


# def parse_all_tables(release_index=DEFAULT_RELEASE_INDEX):
#     databases = {}
#     for k, v in BDB_TABLES.items():
#         if v is not None:
#             entries = parse_table(k)
#             database = BDB_TABLES[k](entries)
#             databases[k] = database
#     return databases
