import pandas as pd

from sklearn.model_selection import train_test_split


class DataSet:
    x_train: []
    x_val: []
    y_train: []
    y_val: []

    def __init__(self, x_train, x_val, y_train, y_val):
        self.x_train = x_train
        self.x_val = x_val
        self.y_train = y_train
        self.y_val = y_val


def load_data_set(config) -> DataSet:
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

    x_train, x_val, y_train, y_val = train_test_split(features, target, test_size=0.2, random_state=42)

    return DataSet(x_train, x_val, y_train, y_val)
