from biopanning_data_bank.config import DATA_DIRECTORY


def test_data_directory():
    assert isinstance(DATA_DIRECTORY, str)
    print(DATA_DIRECTORY)
