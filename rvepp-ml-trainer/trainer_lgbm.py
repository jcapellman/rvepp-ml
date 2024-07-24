import lightgbm as lgb
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score


def train_model(config, data_set):
    print('Training with LightGBM (Version ' + lgb.__version__ + ')')

    train_data = lgb.Dataset(data_set.x_train, label=data_set.y_train)
    test_data = lgb.Dataset(data_set.x_val, label=data_set.y_val, reference=train_data)

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

    y_pred = bst.predict(data_set.x_val, num_iteration=bst.best_iteration)

    y_pred_binary = [1 if pred > 0.5 else 0 for pred in y_pred]

    accuracy = accuracy_score(data_set.y_val, y_pred_binary)
    print(f'Test Set Accuracy: {accuracy}')
