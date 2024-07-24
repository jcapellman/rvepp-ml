import json
import os


class LGBMConfig:
    metric: str
    num_leaves: int
    learning_rate: float
    feature_fraction: float

    def __init__(self, metric='auc', num_leaves=5, learning_rate=0.05, feature_fraction=.9):
        self.metric = metric
        self.num_leaves = num_leaves
        self.learning_rate = learning_rate
        self.feature_fraction = feature_fraction


def load_config(file_name: str) -> LGBMConfig:
    if not os.path.exists(file_name):
        print('LGBM Config file (' + file_name + ') does not exist, using defaults...')

        return LGBMConfig()

    with open(file_name, 'r') as f:
        data = json.load(f)
        return LGBMConfig(**data)
