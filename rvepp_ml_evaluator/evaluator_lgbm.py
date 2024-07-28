import os
import lightgbm as lgb
import pandas as pd

from evaluator_metrics import ModelMetrics
from evaluator_config import Config
from sklearn.metrics import accuracy_score


def run_evaluation(config: Config) -> ModelMetrics:
    if not os.path.isfile(config.model_file_name):
        raise ValueError('Model file (' + config.model_file_name + ') does not exist, exiting...')

    if not os.path.isfile(config.testing_data_file_name):
        raise ValueError('Testing data file (' + config.testing_data_file_name + ') does not exist, exiting...')

    model = lgb.Booster(model_file=config.model_file_name)

    df = pd.read_csv(config.testing_data_file_name)

    y_pred = model.predict(df.x_val, num_iteration=model.best_iteration)

    y_pred_binary = [1 if pred > 0.5 else 0 for pred in y_pred]

    accuracy = accuracy_score(df.y_val, y_pred_binary)

    return ModelMetrics(accuracy)
