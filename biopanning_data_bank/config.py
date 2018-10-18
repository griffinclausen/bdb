import os

PACKAGE_NAME = 'biopanning_data_bank'
PACKAGE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIRECTORY = os.path.dirname(PACKAGE_DIRECTORY)
DATA_DIRECTORY = os.path.join(PROJECT_DIRECTORY, 'data')
TESTS_DIRECTORY = os.path.join(PROJECT_DIRECTORY, 'tests')

DEFAULT_RELEASE_INDEX = 34


def info():
    print(f'Package Name: {PACKAGE_NAME}')
    print(f'Package Directory: {PACKAGE_DIRECTORY}')
    print(f'Project Directory: {PROJECT_DIRECTORY}')
    print(f'Data Directory: {DATA_DIRECTORY}')
    print(f'Tests Directory: {TESTS_DIRECTORY}')
    print(f'Default Release: {DEFAULT_RELEASE_INDEX}')


INVALID_XML_TOKENS = [
    '',
]
