import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import argparse

DEFAULT_MODEL_FILE_NAME = 'elf.mdl'


class Config:
    verbose_logging = False
    model_file_name = DEFAULT_MODEL_FILE_NAME

    def __init__(self, verbose_logging, model_file_name):
        self.verbose_logging = verbose_logging
        self.model_file_name = model_file_name


def parse_arguments() -> Config:
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Trainer Application for RVEPP')

    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose logging')
    parser.add_argument('-mo', '--modeloutput', type=str, default=DEFAULT_MODEL_FILE_NAME, help='Output model file')

    args = parser.parse_args()

    return Config(args.verbose, args.modeloutput)


config = parse_arguments()

if config.verbose_logging:
    print('Initializing...')
    print('Training with LightGBM (Version ' + lgb.__version__ + ')')

df = pd.read_csv('../DataSets/Synthetic/Test001.csv')

if config.verbose_logging:
    print('Printing Header...')
    print(df.head())

    print('Shape: ' + str(df.shape))

    print(df.info())

    print(df.describe())

features = df.drop('is_malicious', axis=1)
target = df['is_malicious']

X_train, X_val, Y_train, Y_val = train_test_split(features, target, test_size=0.2, random_state=42)

train_data = lgb.Dataset(X_train, label=Y_train)
test_data = lgb.Dataset(X_val, label=Y_val, reference=train_data)

params = {
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': 'auc',
    'num_leaves': 5,
    'learning_rate': 0.05,
    'feature_fraction': 0.9
}

bst = lgb.train(params, train_data)

print('Saving model to ' + config.model_file_name + '...')

bst.save_model(config.model_file_name)

lgb.plot_importance(bst, height=.5)
plt.show()

y_pred = bst.predict(X_val, num_iteration=bst.best_iteration)

y_pred_binary = [1 if pred > 0.5 else 0 for pred in y_pred]

accuracy = accuracy_score(Y_val, y_pred_binary)
print(f'Test Set Accuracy: {accuracy}')
