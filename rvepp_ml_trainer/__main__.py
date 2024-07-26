from trainer_config import parse_arguments
from trainer_dataset import load_data_set
from trainer_lgbm import train_model

config = parse_arguments()

data_set = load_data_set(config)

train_model(config, data_set)
