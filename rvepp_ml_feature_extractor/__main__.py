import cProfile
import pstats

from rvepp_ml_evaluator.evaluator_constants import DEFAULT_TESTING_DATA_FILE_NAME
from rvepp_ml_feature_extractor.fe_config import parse_arguments, ExtractionTypes, Config
from rvepp_ml_feature_extractor.fe_synthetic_generator import SyntheticDataGenerator
from rvepp_ml_feature_extractor.fe_constants import PROFILER_OUTPUT_FILE_NAME
from rvepp_ml_feature_extractor.fe_elf_extractor import ElfExtractor


def main():
    config = parse_arguments()
    run(config)


def import_main():
    config = Config(False, False, ExtractionTypes.SYNTHETIC, DEFAULT_TESTING_DATA_FILE_NAME,
                    PROFILER_OUTPUT_FILE_NAME)
    run(config)


def run(config: Config):
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
            case ExtractionTypes.ELFPARSER:
                ElfExtractor().run_extraction(config)


if __name__ == '__main__':
    main()
