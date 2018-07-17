from biopanning_data_bank.bdb_tables.tables import (
        BDB_Entry, BDB_Database)
from biopanning_data_bank.bdb_tables.fields import (
        MIMOSET_FIELDS)

test_sequences = """
IMPHKHRRKLRL(1)[0.50 ± 0.02]
MLTISQRQLSIS(1)[0.48]
RNRTKKQITTQR(1)[0.56 ± 0.01]
RMKMLMMLMRRK(11)[0.52]
""".strip()


class MimosetDatabase(BDB_Database):

    def __init__(self, entries):
        self.fields = MIMOSET_FIELDS
        super().__init__(entries)

    def output_peptide_info(self, filepath='del.psv'):
        sep = '|'
        with open(filepath, 'w') as f:
            columns = ['MimotopeSetID', 'Peptide', 'Count', 'Affinity']
            header = sep.join(columns)
            f.write(header + '\n')

            for e in self.entries:
                for p, c, a in zip(e.peptides, e.counts, e.affinities):
                    line = f'{e.MimotopeSetID}{sep}{p}{sep}{c}{sep}{a}'
                    f.write(line + '\n')


class Mimoset(BDB_Entry):
    """
    Mimoset entry container from Biopanning Data Bank Mimoset Database.
    """
    
    def __init__(self, tree):
        self.fields = MIMOSET_FIELDS
        super().__init__(tree)

        self.get_peptides()
        self.get_most_abundant_peptides()


    def get_peptides(self):
        peptides = []
        counts = []
        affinities = []
        for seq in self.Sequences.split('\n'):
            s = self._extract_sequence_string(seq)
            count = self._extract_sequence_count(seq)
            affinity = self._extract_sequence_affinity(seq)

            peptides.append(s)
            counts.append(count)
            affinities.append(affinity)

        self.peptides = peptides
        self.counts = counts
        self.affinities = affinities

        return peptides


    def get_most_abundant_peptides(self):
        
        if all([isinstance(_, (int, float)) for _ in self.counts]):
            index_max = max(range(len(self.counts)), key=self.counts.__getitem__)
            self.most_abundant_peptides = self.peptides[index_max]
        else:
            self.most_abundant_peptides = []


    def _extract_sequence_string(self, line):

        for i, letter in enumerate(line):
            if letter in '[(':
                break
        return line[:i]


    def _extract_sequence_count(self, line):
        count = -1
        if line.find('(') > 0:
            left = line.find('(') + 1
            if line.find(')') > 0:
                right = line.find(')')
                raw_count = line[left:right]

                # process raw_count
                if raw_count.isdigit():
                    count = int(raw_count)

                elif raw_count.replace('.', '').replace(',', '').isdigit():
                    count = float(raw_count.replace(',', ''))

                elif '/' in raw_count:
                    a, b = raw_count.split('/')[:2]
                    a = a.strip()
                    b = b.strip()
                    if a.isdigit() and b.isdigit():
                        count = int(a) / int(b)
                    else:
                        count = -2

                elif '%' in raw_count:
                    a = float(raw_count.split('%')[0].strip())
                    count = a / 100

                else:
                    count = -3
        return count

    def _extract_sequence_affinity(self, line):
        if line.find('[') > 0:
            left = line.find('[') + 1
            if line.find(']') > 0:
                right = line.find(']')
                return line[left:right]
        return -1

    def peptide_info(self):
        for p, c, a in zip(self.peptides, self.counts, self.affinities):
            if c == -1:
                c = ''
            if a == -1:
                a = ''
            print(f'{p}\t{c}\t{a}')
