import json
import os


class DataSetConfig:
    classification_column: str
    test_size: float
    random_state: int

    def __init__(self, classification_column='is_malicious', test_size=0.2, random_state=42):
        self.classification_column = classification_column
        self.test_size = test_size
        self.random_state = random_state


def load_config(file_name: str) -> DataSetConfig:
    if not os.path.isfile(file_name):
        print('Dataset config file not found (' + file_name + '), using defaults...')

        return DataSetConfig()

    with open(file_name) as json_file:
        data = json.load(json_file)

        return DataSetConfig(**data)
