from fe_config import parse_arguments, ExtractionTypes
from fe_synthetic_generator import SyntheticDataGenerator

config = parse_arguments()

match config.extraction_type:
    case ExtractionTypes.SYNTHETIC:
        SyntheticDataGenerator().run_extraction(config)
