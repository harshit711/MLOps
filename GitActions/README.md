# GitHub Actions

## Overview
This project implements a simple MLOps workflow that automatically trains and evaluates a machine learning model using GitHub Actions

## Workflow
The pipeline runs the following everytime a push is made to the main branch:
1. Generates data
2. Trains a random forest model
3. Evaluates accuracy and F1 score
4. Saves artifacts to GitActions/models and GitActions/metrics
5. Commits new version

## Run the pipeline
```bash
git add .
git commit -m "run pipeline"
git push
```

## The results
1. Trained models are saved in GitActions/models
2. Evaluation metrics are saved in GitActions/metrics

Each run generates timestamped files so you can track model version history
