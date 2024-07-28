import argparse

import trainer_constants
from rvepp_ml_common.common_constants import DEFAULT_MODEL_FILE_NAME, DEFAULT_EXTRACTION_OUTPUT_FILE_NAME


class Config:
    verbose_logging: bool = False
    model_file_name: str = DEFAULT_MODEL_FILE_NAME
    training_set_file_name: str = DEFAULT_EXTRACTION_OUTPUT_FILE_NAME
    training_set_config_file_name: str = trainer_constants.DEFAULT_TRAINING_SET_CONFIG_FILE_NAME
    lgbm_config_file_name: str = trainer_constants.DEFAULT_LGBM_CONFIG_FILE_NAME
    enable_plot: bool = False

    def __init__(self, verbose_logging, model_file_name, training_set_file_name, enable_plot, lgbm_config_file_name,
                 training_set_config_file_name):
        self.verbose_logging = verbose_logging
        self.model_file_name = model_file_name
        self.training_set_file_name = training_set_file_name
        self.enable_plot = enable_plot
        self.lgbm_config_file_name = lgbm_config_file_name
        self.training_set_config_file_name = training_set_config_file_name


def parse_arguments() -> Config:
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Trainer Application for RVEPP')

    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose logging')
    parser.add_argument('-mo', '--modeloutput', type=str,
                        default=DEFAULT_MODEL_FILE_NAME,
                        help='Output model file')
    parser.add_argument('-ts', '--trainingset', type=str,
                        default=DEFAULT_EXTRACTION_OUTPUT_FILE_NAME,
                        help='Training set input file')
    parser.add_argument('-ep', '--enableplot', action='store_true',
                        help='Enables the plotting of feature importance')
    parser.add_argument('-lc', '--lgbmconfig', type=str,
                        default=trainer_constants.DEFAULT_LGBM_CONFIG_FILE_NAME,
                        help='LGBM JSON config file')
    parser.add_argument('-dc', '--datasetconfig', type=str,
                        default=trainer_constants.DEFAULT_TRAINING_SET_CONFIG_FILE_NAME,
                        help='Training DataSet JSON config file')

    args = parser.parse_args()

    return Config(args.verbose, args.modeloutput, args.trainingset, args.enableplot, args.lgbmconfig,
                  args.datasetconfig)
