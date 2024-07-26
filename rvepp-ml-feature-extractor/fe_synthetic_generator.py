import io
import random

from fe_config import Config
from fe_extractor import Extractor, Feature
from fe_synthetic_generator_config import SyntheticGeneratorConfig


class SyntheticDataGenerator(Extractor):
    def run_extraction(self, config: Config) -> bool:
        data_config = SyntheticGeneratorConfig.load_from_file(config.extraction_config_file_name)

        data_file = io.open(config.output_file, mode='w')

        random.seed(data_config.seed_value)

        for i in range(data_config.dataset_size):
            is_malicious = random.randint(0, 1)

            if is_malicious == 0:
                file_size = random.randint(200, 2000)

                if file_size > 1500:
                    is_packed = random.randint(0, 1)
                else:
                    is_packed = 1
            else:
                file_size = random.randint(1000, 10000)

                if file_size > 2500:
                    is_packed = random.randint(0, 1)
                else:
                    is_packed = 0

            super().write_row(data_file, Feature(is_malicious, file_size, is_packed))

        data_file.close()

        print('Generated a Synthetic Data Set of (' + str(data_config.dataset_size) + ' rows) to ' + config.output_file)

        return True
