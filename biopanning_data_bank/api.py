"""
Interface for Biopanning Data Bank website.

Usage:
    from biopanning_data_bank.api import download
    download()

http://immunet.cn/bdb/
"""

import os

import requests

from biopanning_data_bank.config import DATA_DIRECTORY

from biopanning_data_bank import (
    get_most_recent_local_release_index)


def download_bdb_release(release_index=34):
    """
    Downloads zipped BDB database from web
    """
    base_url = 'http://immunet.cn/bdb/index.php/site/download/'
    url = base_url + str(release_index)
    print(f'Downloading from {url}')

    r = requests.get(url, stream=True)
    print(f'\tStatus Code: {r.status_code}')

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


def download(release_index=None, overwrite=False):
    if release_index is None:
        release_index = get_most_recent_web_release_index()

    subdirectory = os.path.join(DATA_DIRECTORY, str(release_index))
    if not overwrite and os.path.exists(subdirectory):
        print('Local database already downloaded')
    else:
        download_bdb_release(release_index)
