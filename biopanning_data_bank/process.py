import os
import tarfile
import gzip

from biopanning_data_bank.config import (DATA_DIRECTORY,
                                         INVALID_XML_TOKENS)


def process_raw_data_file(input_filepath, release_index):
    
    filename = os.path.basename(input_filepath)
    print(f'Processing file: {filename} from release {release_index}')
    
    output_directory = os.path.join(DATA_DIRECTORY, release_index, 'processed')
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_filepath = os.path.join(output_directory, filename)
    
    with open(input_filepath, 'r', encoding='utf-8') as f, \
         open(output_filepath, 'w', encoding='utf-8') as g:
        for line in f:
            for token in INVALID_XML_TOKENS:
                if token in line:
                    print('\tError reading line: ', line.strip())
                    line = line.replace(token, '')
                    print('\tRemoved invalid token: ', token)
                    print('\tProcessed line: ', line.strip())
            g.write(line)


def process_all_raw_data_files(release_index):

    i = str(release_index)
    input_directory = os.path.join(DATA_DIRECTORY, i)
    for d in next(os.walk(input_directory))[1]:
        if d.startswith('bdb') and d.endswith('_xml'):
            version = d[3:-4]
            print(f'\tProcessing BDB Version {version}')
            break

    input_directory = os.path.join(input_directory, d)
    for filename in os.listdir(input_directory):
        if filename.endswith('.xml'):
            filepath = os.path.join(input_directory, filename)
            process_raw_data_file(filepath, i)


def extract_all_raw_data_files(release_index=34):

    input_directory = os.path.join(DATA_DIRECTORY, str(release_index))
    tgz_filepath  = os.path.join(input_directory, str(release_index) + '.tgz')
    tar_filepath = os.path.join(input_directory, str(release_index) + '.tar')

    for filename in os.listdir(input_directory):
            if filename.endswith('tgz'):
                
                print('\tExtracting .tgz to .tar')
                with gzip.open(tgz_filepath, 'rb') as f, open(tar_filepath, 'wb') as g:
                    g.write(f.read())
                print('\tExtracting tar to xml files')
                with tarfile.open(tar_filepath, 'r') as h:
                    h.extractall(input_directory)


def process_release(release_index=34):
    """
    Extracts and processes data files from release index
    """

    print('Extracting data files')
    extract_all_raw_data_files(release_index)

    print('Processing data files')
    process_all_raw_data_files(release_index)


def main():
    process_release(34)


if __name__ == '__main__':
    main()
