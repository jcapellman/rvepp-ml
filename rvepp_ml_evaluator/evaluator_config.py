import argparse
import json

import common_constants


class Config:
    verbose_logging: bool = False
    model_file_name: str = common_constants.DEFAULT_MODEL_FILE_NAME

    def __init__(self, verbose_logging, model_file_name):
        self.verbose_logging = verbose_logging
        self.model_file_name = model_file_name

    def to_json(self) -> str:
        return json.dumps(vars(self))


def parse_arguments() -> Config:
    parser = argparse.ArgumentParser(description='Inference Application for RVEPP')

    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose logging')
    parser.add_argument('-mi', '--modelinput', type=str,
                        default=common_constants.DEFAULT_MODEL_FILE_NAME,
                        help='Input model file')

    args = parser.parse_args()

    return Config(args.verbose, args.modelinput)
