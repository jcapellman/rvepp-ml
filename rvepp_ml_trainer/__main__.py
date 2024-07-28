from rvepp_ml_trainer.trainer_config import parse_arguments
from rvepp_ml_trainer.trainer_dataset import load_data_set
from rvepp_ml_trainer.trainer_lgbm import train_model


def main():
    config = parse_arguments()

    data_set = load_data_set(config)

    train_model(config, data_set)


if __name__ == '__main__':
    main()
