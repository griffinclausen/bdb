import xml.etree.ElementTree as ET

class BDB_Database:

    def __init__(self, entries):
        self.entries = entries


class BDB_Entry:
    
    def __init__(self, tree):
        self.tree = tree
        self.unpack_tree()

    def unpack_tree(self):
        for f in self.fields:
            self.__dict__[f] = self.tree.find(f"*[@name='{f}']").text

    def show_tree(self):
        for f in self.fields:
            print(f'{f}\n{self.__dict__[f]}\n')
            
