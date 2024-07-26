import json
import os

from abc import abstractmethod

from fe_config import Config


class Feature:
    is_malicious: bool
    file_size: int
    is_packed: bool

    def __init__(self, is_malicious, file_size, is_packed):
        self.is_malicious = is_malicious
        self.file_size = file_size
        self.is_packed = is_packed


class Extractor:
    def write_row(self, data_file, row_object: Feature):
        json_str = json.dumps(row_object)

        data_file.writelines(json_str + os.linesep)

    @abstractmethod
    def run_extraction(self, config: Config) -> bool:
        pass
