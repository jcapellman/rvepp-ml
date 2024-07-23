import argparse

# Constants
DEFAULT_MODEL_FILE_NAME = 'elf.mdl'
DEFAULT_TRAINING_SET_FILE_NAME = '../DataSets/Synthetic/Test001.csv'


class Config:
    verbose_logging = False
    model_file_name = DEFAULT_MODEL_FILE_NAME
    training_set_file_name = DEFAULT_TRAINING_SET_FILE_NAME

    def __init__(self, verbose_logging, model_file_name, training_set_file_name):
        self.verbose_logging = verbose_logging
        self.model_file_name = model_file_name
        self.training_set_file_name = training_set_file_name


def parse_arguments() -> Config:
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Trainer Application for RVEPP')

    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose logging')
    parser.add_argument('-mo', '--modeloutput', type=str, default=DEFAULT_MODEL_FILE_NAME, help='Output model file')
    parser.add_argument('-ts', '--trainingset', type=str, default=DEFAULT_TRAINING_SET_FILE_NAME, help='Training set input file')

    args = parser.parse_args()

    return Config(args.verbose, args.modeloutput, args.trainingset)
