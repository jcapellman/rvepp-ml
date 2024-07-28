from rvepp_ml_feature_extractor.__main__ import main as fe_main
from rvepp_ml_feature_extractor.__main__ import import_main
from rvepp_ml_trainer.__main__ import main as train_main
from rvepp_ml_evaluator.__main__ import main as eval_main

fe_main()  # Generate the Synthetic Data for the Model

train_main()  # Generate the Model

import_main()  # Generate the Test Data for the Model Evaluation

eval_main()  # Evaluate the Model
