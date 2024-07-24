import argparse

from trainer_constants import DEFAULT_MODEL_FILE_NAME, DEFAULT_TRAINING_SET_FILE_NAME


class Config:
    verbose_logging: bool = False
    model_file_name: str = DEFAULT_MODEL_FILE_NAME
    training_set_file_name: str = DEFAULT_TRAINING_SET_FILE_NAME
    enable_plot: bool = False

    def __init__(self, verbose_logging, model_file_name, training_set_file_name, enable_plot):
        self.verbose_logging = verbose_logging
        self.model_file_name = model_file_name
        self.training_set_file_name = training_set_file_name
        self.enable_plot = enable_plot


def parse_arguments() -> Config:
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Trainer Application for RVEPP')

    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose logging')
    parser.add_argument('-mo', '--modeloutput', type=str, default=DEFAULT_MODEL_FILE_NAME,
                        help='Output model file')
    parser.add_argument('-ts', '--trainingset', type=str, default=DEFAULT_TRAINING_SET_FILE_NAME,
                        help='Training set input file')
    parser.add_argument('-ep', '--enableplot', action='store_true',
                        help='Enables the plotting of feature importance')

    args = parser.parse_args()

    return Config(args.verbose, args.modeloutput, args.trainingset, args.enableplot)
