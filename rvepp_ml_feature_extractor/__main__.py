import cProfile
import pstats

from fe_config import parse_arguments, ExtractionTypes
from fe_synthetic_generator import SyntheticDataGenerator
from fe_constants import PROFILER_OUTPUT_FILE_NAME

config = parse_arguments()

print('RVEPP-ML Feature Extractor (2024.7.0)')

if config.profiler_mode:
    with cProfile.Profile() as profile:
        SyntheticDataGenerator().run_extraction(config)

        results = pstats.Stats(profile).sort_stats('tottime')
        results.print_stats()
        results.dump_stats(PROFILER_OUTPUT_FILE_NAME)
else:
    if config.verbose_logging:
        print('Using the following config: ' + config.to_json())

    match config.extraction_type:
        case ExtractionTypes.SYNTHETIC:
            SyntheticDataGenerator().run_extraction(config)
