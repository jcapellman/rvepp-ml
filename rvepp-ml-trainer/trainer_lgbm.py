
import lightgbm as lgb
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score

from trainer_lgbm_config import load_config


def train_model(config, data_set):
    print('Training with LightGBM (Version ' + lgb.__version__ + ')')

    train_data = lgb.Dataset(data_set.x_train, label=data_set.y_train)
    test_data = lgb.Dataset(data_set.x_val, label=data_set.y_val, reference=train_data)

    lgbm_config = load_config(config.lgbm_config_file_name)

    params = {
        'boosting_type': 'gbdt',  # for now this will remain gbdt
        'objective': 'binary',  # for this problem set this will remain binary
        'metric': lgbm_config.metric,
        'num_leaves': lgbm_config.num_leaves,
        'learning_rate': lgbm_config.learning_rate,
        'feature_fraction': lgbm_config.feature_fraction,
        "verbosity": 1 if config.verbose_logging else -1
    }

    bst = lgb.train(params, train_data)

    print('Saving model to ' + config.model_file_name + '...')

    bst.save_model(config.model_file_name)

    if config.enable_plot:
        lgb.plot_importance(bst, height=.5)
        plt.show()

    y_pred = bst.predict(data_set.x_val, num_iteration=bst.best_iteration)

    y_pred_binary = [1 if pred > 0.5 else 0 for pred in y_pred]

    accuracy = accuracy_score(data_set.y_val, y_pred_binary)
    print(f'Test Set Accuracy: {accuracy}')
