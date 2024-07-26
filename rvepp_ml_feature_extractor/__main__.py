from fe_config import parse_arguments, ExtractionTypes
from fe_synthetic_generator import SyntheticDataGenerator

config = parse_arguments()

print('RVEPP-ML Feature Extractor (2024.7.0)')

if config.verbose_logging:
    print('Using the following config: ' + config.to_json())

match config.extraction_type:
    case ExtractionTypes.SYNTHETIC:
        SyntheticDataGenerator().run_extraction(config)
