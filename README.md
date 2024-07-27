# rvepp-ml
Repository for the Machine Learning model related work for RVEPP.

The work is split into three components:
* Feature Extractor (either from synthetic generation or extraction from samples)
* Model Training via the Trainer Application
* Testing Predictions and Evaluating the Model

The focus initially will be on the trainer itself followed by the evaluator.

# Components
## Feature Extractor
[![ML Feature Extractor Application](https://github.com/jcapellman/rvepp-ml/actions/workflows/feature-extractor-app.yaml/badge.svg)](https://github.com/jcapellman/rvepp-ml/actions/workflows/feature-extractor-app.yaml)

Application that supports synthetic and sample based feature extraction with configurable parameters. The output of this application is to be used with the trainer application.

## Trainer
[![ML Trainer Application](https://github.com/jcapellman/rvepp-ml/actions/workflows/trainer-app.yml/badge.svg)](https://github.com/jcapellman/rvepp-ml/actions/workflows/trainer-app.yml)

Application that accepts a dataset, parameters for the model and then trains the LightGBM model. Over time, the data source might expand to include other sources than a local csv.

## Evaluator
https://github.com/jcapellman/rvepp-ml/actions/workflows/evaluator-app.yml/badge.svg

Application that accepts a trained model and a testing data set, in which model metrics are performed.