import json
import os

from abc import abstractmethod

from rvepp_ml_feature_extractor.fe_config import Config


class Feature:
    is_malicious: bool
    file_size: int
    is_packed: bool

    def __init__(self, is_malicious: bool, file_size: int, is_packed: bool):
        self.is_malicious = is_malicious
        self.file_size = file_size
        self.is_packed = is_packed

    def to_json(self):
        return json.dumps(vars(self))

    def to_csv(self) -> str:
        values = [int(value) if isinstance(value, bool) else value for value in self.__dict__.values()]

        return ','.join(str(value) for value in values)


class Extractor:
    def write_row(self, data_file, row_object: Feature):
        data_file.writelines(row_object.to_csv() + os.linesep)

    def write_header_row(self, data_file, row_object: Feature):
        data_file.writelines(','.join(row_object.__dict__.keys()) + os.linesep)

    @abstractmethod
    def run_extraction(self, config: Config) -> bool:
        pass
