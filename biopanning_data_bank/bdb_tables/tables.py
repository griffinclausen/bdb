from collections import Counter

# import xml.etree.ElementTree as ET


class BDB_Database:

    def __init__(self, entries):
        self.entries = entries

    def get_field_counts(self):
        field_counts = {}
        for field in self.fields:
            counter = Counter()
            for entry in self.entries:
                counter.update({entry.__dict__[field]: 1})
            field_counts[field] = counter
        return field_counts

    def info(self):
        num = len(self.entries)
        output = str(f'Database of {num} entriesself.')
        return output

    def __str__(self):
        return self.info()


class BDB_Entry:

    def __init__(self, tree):
        self.tree = tree
        self.unpack_tree()

    def unpack_tree(self):
        for f in self.fields:
            try:
                self.__dict__[f] = self.tree.find(f"*[@name='{f}']").text
            except AttributeError:
                self.__dict__[f] = None

    def show_tree(self):
        for f in self.fields:
            print(f'{f}\n{self.__dict__[f]}\n')

    def info(self):
        keys = self.fields
        values = [self.__dict__[k] for k in keys]
        output = '\n'.join([f'{k}: {v}' for k, v in zip(keys, values)])
        return output

    def __str__(self):
        return self.info()
