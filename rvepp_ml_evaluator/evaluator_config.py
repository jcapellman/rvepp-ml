import argparse
import json

import common_constants
from evaluator_constants import DEFAULT_TESTING_DATA_FILE_NAME


class Config:
    verbose_logging: bool = False
    model_file_name: str = common_constants.DEFAULT_MODEL_FILE_NAME
    testing_data_file_name: str = DEFAULT_TESTING_DATA_FILE_NAME

    def __init__(self, verbose_logging: bool, model_file_name: str, testing_data_file_name: str):
        self.verbose_logging = verbose_logging
        self.model_file_name = model_file_name
        self.testing_data_file_name = testing_data_file_name

    def to_json(self) -> str:
        return json.dumps(vars(self))


def parse_arguments() -> Config:
    parser = argparse.ArgumentParser(description='Inference Application for RVEPP')

    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose logging')
    parser.add_argument('-mi', '--modelinput', type=str,
                        default=common_constants.DEFAULT_MODEL_FILE_NAME,
                        help='Input model file')
    parser.add_argument('-td', '--testdata', type=str,
                        default=DEFAULT_TESTING_DATA_FILE_NAME,
                        help='Input testing data file name')

    args = parser.parse_args()

    return Config(args.verbose, args.modelinput, args.testdata)
