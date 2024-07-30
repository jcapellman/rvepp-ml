from rvepp_ml_common.common_json_file_loader import load_from_file

DEFAULT_SAMPLE_PATH: str = 'samples/'


class ElfExtractorConfig:
    sample_path: str

    def __init__(self, sample_path: str = DEFAULT_SAMPLE_PATH):
        self.sample_path = sample_path

    @staticmethod
    def load_from_file(file_name: str) -> 'ElfExtractorConfig':
        return load_from_file(file_name, ElfExtractorConfig)
