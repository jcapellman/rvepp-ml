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

    def to_json(self):
        return json.dumps(vars(self))


class Extractor:
    def write_row(self, data_file, row_object: Feature):
        data_file.writelines(row_object.to_json() + os.linesep)

    @abstractmethod
    def run_extraction(self, config: Config) -> bool:
        pass
