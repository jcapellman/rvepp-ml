import io
import json

from rvepp_ml_evaluator.evaluator_config import Config


class ModelMetrics:
    accuracy: float
    precision: float
    recall: float
    f_score: float
    duration_seconds: float

    def __init__(self, accuracy: float, precision: float, recall: float, f_score: float, duration_seconds: float):
        self.accuracy = accuracy
        self.precision = precision
        self.recall = recall
        self.f_score = f_score
        self.duration_seconds = duration_seconds

    def to_json(self) -> str:
        return json.dumps(vars(self))

    def save_to_disk(self, config: Config):
        json_file = io.open(config.metrics_output_file_name, mode='w')

        json_file.write(self.to_json())

        json_file.close()
