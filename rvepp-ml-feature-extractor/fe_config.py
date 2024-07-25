import argparse
from enum import Enum

from fe_constants import DEFAULT_EXTRACTION_OUTPUT_FILE_NAME


class ExtractionTypes(Enum):
    SYNTHETIC = 1


class Config:
    verbose_logging: bool = False
    extraction_type: ExtractionTypes = ExtractionTypes.SYNTHETIC
    output_file: str = DEFAULT_EXTRACTION_OUTPUT_FILE_NAME

    def __init__(self, verbose_logging, extraction_type, output_file):
        self.verbose_logging = verbose_logging
        self.extraction_type = extraction_type
        self.output_file = output_file


def parse_arguments() -> Config:
    parser = argparse.ArgumentParser(description='Feature Extraction Application for RVEPP')

    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose logging')
    parser.add_argument('-t', '--extractiontype', type=ExtractionTypes,
                        default=ExtractionTypes.SYNTHETIC,
                        help='Extraction type')
    parser.add_argument('-o', '--outputfile', type=str,
                        default=DEFAULT_EXTRACTION_OUTPUT_FILE_NAME,
                        help='Extraction output file')

    args = parser.parse_args()

    return Config(args.verbose, args.extractiontype, args.outputfile)
