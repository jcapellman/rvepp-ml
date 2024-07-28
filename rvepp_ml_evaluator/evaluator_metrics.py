import io
import json

from evaluator_config import Config


class ModelMetrics:
    accuracy: float

    def __init__(self, accuracy: float):
        self.accuracy = accuracy

    def to_json(self) -> str:
        return json.dumps(vars(self))

    def save_to_disk(self, config: Config):
        json_file = io.open(config.metrics_output_file_name, mode='w')

        json_file.write(self.to_json())

        json_file.close()
