import shap
import lightgbm as lgb
import pandas as pd

from rvepp_ml_evaluator.evaluator_config import Config
from rvepp_ml_common.common_constants import CLASSIFICATION_COLUMN


def run_shap(config: Config):
    model = lgb.Booster(model_file=config.model_file_name)

    df = pd.read_csv(config.testing_data_file_name)

    x_test = df.drop(columns=[CLASSIFICATION_COLUMN])

    shap.initjs()

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(x_test)

    shap.force_plot(explainer.expected_value[0], shap_values[0])

    shap.summary_plot(shap_values, x_test)
