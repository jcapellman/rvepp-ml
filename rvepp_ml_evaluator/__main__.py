from rvepp_ml_evaluator.evaluator_config import parse_arguments, Config
from rvepp_ml_evaluator.evaluator_lgbm import run_evaluation


def main():
    config: Config = parse_arguments()

    print('RVEPP-ML Evaluator (2024.7.0)')

    if config.verbose_logging:
        print('Using the following config: ' + config.to_json())

    print('Running the LightGBM evaluator...')

    model_metrics = run_evaluation(config)

    model_metrics.save_to_disk(config)

    print('Model Metrics were saved to ' + config.metrics_output_file_name)


if __name__ == '__main__':
    main()
