import io
import random

from fe_config import Config
from fe_extractor import Extractor, Feature


class SyntheticDataGenerator(Extractor):
    def run_extraction(self, config: Config) -> bool:
        data_file = io.open(config.output_file, mode='w')

        random.seed(1985)

        dataset_size = 1000

        for i in range(dataset_size):
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

        return True
