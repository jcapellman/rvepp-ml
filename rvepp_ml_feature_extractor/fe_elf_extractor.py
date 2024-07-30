import glob
import os
import io

from rvepp_ml_feature_extractor.fe_config import Config
from rvepp_ml_feature_extractor.fe_extractor import Extractor, Feature
from elftools.elf.elffile import ELFFile


class ElfExtractor(Extractor):
    def run_extraction(self, config: Config) -> bool:
        if not os.path.exists('samples/'):
            print('Path does not exist...')

            return False

        files =  glob.glob('samples/')

        if len(files) == 0:
            print('No samples found')

            return False

        data_file = io.open(config.output_file, mode='w')

        super().write_header_row(data_file, Feature(True, 1, True))

        for filename in files:
            with open(filename, 'rb') as f:
                elffile = ELFFile(f)

                if elffile is None:
                    print(filename + ' was not an ELF file, ignoring...')

                    continue

                content = f.read()

                is_packed: bool = b'UPX!' in content or b'UPX0' in content
                is_malicious: bool = filename.startswith('malware')

                super().write_row(data_file, Feature(is_malicious, os.path.getsize(filename), is_packed))

        data_file.close()

        print('Generated a ELF Extracted Data Set to ' + config.output_file)

        return True
