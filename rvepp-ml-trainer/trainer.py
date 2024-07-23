import pandas as pd

from sklearn.model_selection import train_test_split

from trainer_config import parse_arguments
from trainer_lgbm import train_model

config = parse_arguments()

if config.verbose_logging:
    print('Initializing...')

df = pd.read_csv(config.training_set_file_name)

print('Read in (' + config.training_set_file_name + ') for training...')

if config.verbose_logging:
    print('Printing Header...')
    print(df.head())

    print('Shape: ' + str(df.shape))

    print(df.info())

    print(df.describe())

features = df.drop('is_malicious', axis=1)
target = df['is_malicious']

X_train, X_val, Y_train, Y_val = train_test_split(features, target, test_size=0.2, random_state=42)

train_model(config, X_train, X_val, Y_train, Y_val)
