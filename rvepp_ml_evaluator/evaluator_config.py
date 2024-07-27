import argparse
import json

import common_constants
from evaluator_constants import DEFAULT_TESTING_DATA_FILE_NAME, DEFAULT_METRICS_OUTPUT_FILE_NAME


class Config:
    verbose_logging: bool = False
    model_file_name: str = common_constants.DEFAULT_MODEL_FILE_NAME
    testing_data_file_name: str = DEFAULT_TESTING_DATA_FILE_NAME
    metrics_output_file_name: str = DEFAULT_METRICS_OUTPUT_FILE_NAME

    def __init__(self, verbose_logging: bool, model_file_name: str, testing_data_file_name: str, metrics_output_file_name: str):
        if model_file_name == '':
            raise ValueError('model_file_name cannot be None')

        if testing_data_file_name == '':
            raise ValueError('testing_data_file_name cannot be None')

        self.verbose_logging = verbose_logging
        self.model_file_name = model_file_name
        self.testing_data_file_name = testing_data_file_name
        self.metrics_output_file_name = metrics_output_file_name

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
    parser.add_argument('-mo', '--metricsoutput', type=str,
                        default=DEFAULT_METRICS_OUTPUT_FILE_NAME,
                        help='File to save the metrics to')

    args = parser.parse_args()

    return Config(args.verbose, args.modelinput, args.testdata, args.metricsoutput)
