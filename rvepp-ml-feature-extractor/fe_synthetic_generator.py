import io
import random

from fe_config import Config
from fe_extractor import Extractor


class SyntheticDataGenerator(Extractor):
    def run_extraction(self, config: Config) -> bool:
        data_file = io.open(config.output_file, mode='w')

        random.seed(1985)

        dataset_size = 1000

        data_file.write('is_malicious,file_size,is_packed\n')

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

            data_file.writelines(str(is_malicious) + ',' + str(file_size) + ',' + str(is_packed) + '\n')

        return True
