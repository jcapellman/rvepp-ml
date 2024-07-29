import argparse
import json

from enum import Enum

from rvepp_ml_common.common_constants import DEFAULT_EXTRACTION_OUTPUT_FILE_NAME
from rvepp_ml_feature_extractor.fe_constants import DEFAULT_EXTRACTION_CONFIG_FILE_NAME


class ExtractionTypes(str, Enum):
    SYNTHETIC = 'Synthetic'
    ELFPARSER = 'ELFParser'


class Config:
    verbose_logging: bool = False
    profiler_mode: bool = False
    extraction_type: ExtractionTypes = ExtractionTypes.SYNTHETIC
    output_file: str = DEFAULT_EXTRACTION_OUTPUT_FILE_NAME
    extraction_config_file_name: str = DEFAULT_EXTRACTION_CONFIG_FILE_NAME

    def __init__(self, verbose_logging: bool, profiler_mode: bool, extraction_type: ExtractionTypes, output_file: str,
                 extraction_config_file_name: str):
        self.verbose_logging = verbose_logging
        self.profiler_mode = profiler_mode

        if extraction_type is None:
            raise ValueError('Extraction type must be specified')

        if output_file is None:
            raise ValueError('Output file must be specified')

        if extraction_config_file_name is None:
            raise ValueError('Extraction configuration file name must be specified')

        self.extraction_type = extraction_type
        self.output_file = output_file
        self.extraction_config_file_name = extraction_config_file_name

    def to_json(self) -> str:
        return json.dumps(vars(self))


def parse_arguments() -> Config:
    parser = argparse.ArgumentParser(description='Feature Extraction Application for RVEPP')

    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose logging')
    parser.add_argument('-p', '--profiler', action='store_true', help='Enable profiler mode')
    parser.add_argument('-t', '--extractiontype', type=ExtractionTypes,
                        default=ExtractionTypes.SYNTHETIC,
                        help='Extraction type')
    parser.add_argument('-o', '--outputfile', type=str,
                        default=DEFAULT_EXTRACTION_OUTPUT_FILE_NAME,
                        help='Extraction output file')
    parser.add_argument('-c', '--configfile', type=str,
                        default=DEFAULT_EXTRACTION_CONFIG_FILE_NAME,
                        help='JSON configuration for the extraction type')

    args = parser.parse_args()

    return Config(args.verbose, args.profiler, args.extractiontype, args.outputfile, args.configfile)
