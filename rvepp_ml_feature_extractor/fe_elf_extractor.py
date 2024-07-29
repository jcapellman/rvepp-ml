import glob
import os
import io

from rvepp_ml_feature_extractor.fe_config import Config
from rvepp_ml_feature_extractor.fe_extractor import Extractor, Feature
from elftools.elf.elffile import ELFFile


class ElfExtractor(Extractor):
    def run_extraction(self, config: Config) -> bool:
        data_file = io.open(config.output_file, mode='w')

        super().write_header_row(data_file, Feature(True, 1, True))

        files =  glob.glob('samples/')

        for filename in files:
            with open(filename, 'rb') as f:
                # elffile = ELFFile(f)

                content = f.read()

                is_packed: bool = b'UPX!' in content or b'UPX0' in content
                is_malicious: bool = filename.startswith('malware')

                super().write_row(data_file, Feature(is_malicious, os.path.getsize(filename), is_packed))

        data_file.close()

        print('Generated a ELF Extracted Data Set to ' + config.output_file)

        return True
