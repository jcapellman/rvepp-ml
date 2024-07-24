import pandas as pd

from sklearn.model_selection import train_test_split

import trainer_dataset_config


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

    print('Read in Training Data Set (' + config.training_set_file_name + ')...')

    if config.verbose_logging:
        print('Printing Header...')
        print(df.head())

        print('Shape: ' + str(df.shape))

        print(df.info())

        print(df.describe())

    training_set_config = trainer_dataset_config.load_config(config.training_set_config_file_name)

    features = df.drop(training_set_config.classification_column, axis=1)
    target = df[training_set_config.classification_column]

    x_train, x_val, y_train, y_val = train_test_split(features, target, test_size=training_set_config.test_size,
                                                      random_state=training_set_config.random_state)

    return DataSet(x_train, x_val, y_train, y_val)
