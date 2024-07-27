from evaluator_config import parse_arguments, Config
from evaluator_lgbm import run_evaluation

config: Config = parse_arguments()

print('RVEPP-ML Evaluator (2024.7.0)')

if config.verbose_logging:
    print('Using the following config: ' + config.to_json())

model_metrics = run_evaluation(config)

model_metrics.save_to_disk(config)
