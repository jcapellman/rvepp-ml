from rvepp_ml_common.common_json_file_loader import load_from_file

DEFAULT_SEED_VALUE: int = 1985
DEFAULT_DATASET_SIZE: int = 2003


class SyntheticGeneratorConfig:
    seed_value: int
    dataset_size: int

    def __init__(self, seed_value: int = DEFAULT_SEED_VALUE, dataset_size: int = DEFAULT_DATASET_SIZE):
        self.seed_value = seed_value
        self.dataset_size = dataset_size

    @staticmethod
    def load_from_file(file_name: str):
        return load_from_file(file_name, SyntheticGeneratorConfig)
