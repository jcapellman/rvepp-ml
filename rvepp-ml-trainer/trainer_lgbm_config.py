import trainer_common


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

    @staticmethod
    def load_from_file(file_name: str):
        return trainer_common.load_from_file(file_name, LGBMConfig)
