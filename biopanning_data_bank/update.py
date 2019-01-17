"""
Interface for Biopanning Data Bank website.

Usage:
    from bdb import api
    api.download_lastest_update()
    api.download()

http://immunet.cn/bdb/
"""

import os

import requests

from biopanning_data_bank.config import DATA_DIRECTORY
from biopanning_data_bank.process import process_release


def create_data_folder():
    if not os.path.exists(DATA_DIRECTORY):
        os.makedirs(DATA_DIRECTORY)


def parse_data_files(release_index):
    """
    Parses each raw BDB file.

    data/34/parsed/{filename}
    """
    print(f'\tTBD')


def download_bdb_release(release_index=33):
    """
    Downloads zipped BDB database from web
    """
    base_url = 'http://immunet.cn/bdb/index.php/site/download/'
    url = base_url + str(release_index)
    print(f'\tDownloading from {url}')

    r = requests.get(url, stream=True)
    print(f'\t\tStatus code: {r.status_code}')

    subdirectory = os.path.join(DATA_DIRECTORY, str(release_index))
    if not os.path.exists(subdirectory):
        os.makedirs(subdirectory)

    filepath = os.path.join(subdirectory, str(release_index) + '.tgz')
    with open(filepath, 'wb') as f:
        f.write(r.content)


def get_most_recent_web_release_index():
    """
    Returns largest release index for BDB downloads pages

    BDB releases are uploaded to the web in sequential order
        ...
        bdb8.0_xml --> http://immunet.cn/bdb/index.php/history/33
        bdb8.1_xml -->                                        /34
        ...

    http://immunet.cn/bdb/index.php/site/download/34
    """
    local_index = int(get_most_recent_local_release_index())

    max_attempts = 2

    base_url = 'http://immunet.cn/bdb/index.php/history/'

    for i in range(max_attempts):
        url = base_url + str(local_index + 1 + i)
        print(f'\t{url}')

        r = requests.get(url)
        print(f'\t\tStatus code:', r.status_code)

        if r.status_code == 200:
            pass
        elif r.status_code == 404:
            return str(local_index + i)
        else:
            break

    return str(local_index + i)


def get_most_recent_local_release_index():
    """
    Returns most recent version of the bdb database in the data directory.

    Data files for each release are stored in separated subdirectories.

    Returns
    -------
    int    Most recent BDB database currently in data directory
    """
    dirs = [f.name for f in os.scandir(DATA_DIRECTORY) if f.is_dir()]
    return max(dirs + ['33'])


def download(release_index=None, overwrite=False):
    """
    Downloads most recent BDB release, or specified release index
    """

    if release_index is None:
        release_index = get_most_recent_web_release_index()

    subdirectory = os.path.join(DATA_DIRECTORY, str(release_index))
    if not overwrite and os.path.exists(subdirectory):
        print('Local database already downloaded')
    else:
        download_bdb_release(release_index)


def update():
    """
    Updates data directory with latest BDB database from the web.
    """

    # creates data directory if it does not exist
    create_data_folder()

    print('Checking for latest release index available on data directory')
    local_index = get_most_recent_local_release_index()
    print(f'\t{local_index}')

    print('Checking for latest release index available on web')
    web_index = get_most_recent_web_release_index()
    print(f'\t{web_index}')

    if web_index > local_index:
        print('Downloading latest database')
        download_bdb_release(web_index)

        print('Processing compressed download file')
        process_release(web_index)

        print('Parsing data tables')
        parse_data_files(web_index)

    else:
        print('Local data is up to date.')


def test():
    process_release(34)


def main():
    update()


if __name__ == '__main__':
    test()
