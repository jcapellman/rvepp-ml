import os
import lightgbm as lgb
from numpy import array
from evaluator_config import Config

def run_evaluation(config: Config):
    if not os.path.isfile(config.model_file_name):
        raise ValueError('Model file (' + config.model_file_name + ') does not exist, exiting...')

    model = lgb.Booster(model_file=config.model_file_name)

    input_vector = array([[4000, 1]])

    prediction = model.predict(input_vector)
    print("Prediction:", prediction)
