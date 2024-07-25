from abc import abstractmethod

from fe_config import Config


class Extractor:
    @abstractmethod
    def run_extraction(self, config: Config) -> bool:
        pass
