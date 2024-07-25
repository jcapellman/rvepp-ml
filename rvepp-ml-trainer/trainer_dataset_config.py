import trainer_common


class DataSetConfig:
    classification_column: str
    test_size: float
    random_state: int

    def __init__(self, classification_column='is_malicious', test_size=0.2, random_state=42):
        self.classification_column = classification_column
        self.test_size = test_size
        self.random_state = random_state

    def __eq__(self, other):
        if not isinstance(other, DataSetConfig):
            return NotImplemented

        return (self.classification_column == other.classification_column and self.test_size == other.test_size
                and self.random_state == other.random_state)

    @staticmethod
    def load_from_file(file_name: str):
        return trainer_common.load_from_file(file_name, DataSetConfig)
