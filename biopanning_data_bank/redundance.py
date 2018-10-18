import os

import pandas as pd

from bdb.config import DATA_DIRECTORY


aa_red = {
   'R': 3,
   'L': 3,
   'S': 3,
   'G': 2,
   'A': 2,
   'P': 2,
   'T': 2,
   'V': 2,
   'Q': 2,
   'C': 1,
   'D': 1,
   'E': 1,
   'F': 1,
   'H': 1,
   'I': 1,
   'K': 1,
   'M': 1,
   'N': 1,
   'W': 1,
   'Y': 1
}


fp = os.path.join(DATA_DIRECTORY, 'nnk_dna_percentile_table.csv')
df_nnk_dna = pd.read_csv(fp, index_col='F')

fp = os.path.join(DATA_DIRECTORY, 'nnk_protein_percentile_table.csv')
df_nnk_pro = pd.read_csv(fp, index_col='F')


def calculate_nnk_percentile(pep):
    red = calculate_redundance(pep)
    if red == 0:
        return 0, 0

    length = str(len(pep))
    dna = df_nnk_dna.loc[red][length]
    pro = df_nnk_pro.loc[red][length]
    return pro, dna


def calculate_redundance(pep):
    red = 1
    for aa in pep:
        try:
            red *= aa_red.get(aa, 0)
        except Exception as e:
            red = 0
    return red


def main():
    input_filepath = os.path.join(DATA_DIRECTORY,
                                  '34', 'analysis', 'all_sequences_neb_1_2_3')
    with open(input_filepath, 'r') as f:
        for line in f:
            pep = line.strip()

            pep = pep.replace('*', 'Q')
            pep = pep.replace('X', 'Q')

            if pep.endswith('GGG'):
                pep = pep[:-3]

            if pep.startswith('C') and pep.endswith('C'):
                pep = pep[1:-1]

            length = len(pep)

            if length in [7, 12]:
                red = calculate_redundance(pep)
                if red > 0:
                    pro, dna = calculate_nnk_percentile(pep)
                    print(f'{pep}\t{length}\t{red}\t{pro}\t{dna}')


def test():
    # filename = 'delete_tags.txt'
    # filename = 'birnbaum_test.txt'
    # filename = '1st_generation_random_library_Filtered_AA_UNIQUE.fs'
    # filename = 'NT-TriNuc_filtered_SLN_pep.txt'
    filename = 'he_nnk.txt'

    with open(filename) as f:
        for line in f:
            pep = line.strip()

    if len(pep) <= 12:
        red = calculate_redundance(pep)
        pro, dna = calculate_nnk_percentile(pep)
    else:
        red, dna, pro = 0, 0, 0
    print(pep, red, dna, pro)


if __name__ == '__main__':
    test()
    # main()
