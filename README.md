# rvepp-ml
Repository for the Machine Learning model related work for RVEPP.

The work is split into three components:
* Feature Extractor (either from synthetic generation or extraction from samples)
* Model Training via the Trainer Application
* Testing Predictions and Evaluating the Model

The focus initially will be on the trainer itself followed by the evaluator.

# Components
## Feature Extractor
TBD

## Trainer
[![ML Trainer Application](https://github.com/jcapellman/rvepp-ml/actions/workflows/trainer-app.yml/badge.svg)](https://github.com/jcapellman/rvepp-ml/actions/workflows/trainer-app.yml)

Application that accepts a dataset, parameters for the model and then trains the LightGBM model. Over time, the data source might expand to include other sources than a local csv.

## Evaluator
TBD
