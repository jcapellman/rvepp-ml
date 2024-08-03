import os
import lightgbm as lgb
import pandas as pd

from datetime import datetime
from rvepp_ml_evaluator.evaluator_metrics import ModelMetrics
from rvepp_ml_evaluator.evaluator_config import Config
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from rvepp_ml_common.common_constants import CLASSIFICATION_COLUMN


def run_evaluation(config: Config) -> ModelMetrics:
    if not os.path.isfile(config.model_file_name):
        raise ValueError('Model file (' + config.model_file_name + ') does not exist, exiting...')

    if not os.path.isfile(config.testing_data_file_name):
        raise ValueError('Testing data file (' + config.testing_data_file_name + ') does not exist, exiting...')

    model = lgb.Booster(model_file=config.model_file_name)

    df = pd.read_csv(config.testing_data_file_name)

    x_test = df.drop(columns=[CLASSIFICATION_COLUMN])
    y_test = df[CLASSIFICATION_COLUMN]

    start_time = datetime.now()

    y_pred = model.predict(x_test, num_iteration=model.best_iteration)

    y_pred_binary = [1 if pred > 0.5 else 0 for pred in y_pred]

    accuracy = accuracy_score(y_test, y_pred_binary)

    precision = precision_score(y_test, y_pred_binary)
    recall = recall_score(y_test, y_pred_binary)
    f1 = f1_score(y_test, y_pred_binary)
    roc_auc = roc_auc_score(y_test, y_pred_binary)

    total_time = datetime.now() - start_time

    return ModelMetrics(accuracy, precision, recall, f1, roc_auc, total_time.total_seconds())
