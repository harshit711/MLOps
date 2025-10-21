# Spam Classification using Snorkel

## Overview

This project demonstrates how to build a Spam vs Ham text classifier for YouTube comments using Snorkel’s supervision framework.

## Project Structure

├── data/
│   ├── Youtube01-Psy.csv
│   ├── Youtube02-KatyPerry.csv
│   ├── Youtube03-LMFAO.csv
│   ├── Youtube04-Eminem.csv
│   └── Youtube05-Shakira.csv
├── utils.py
├── Data_labeling_lab.ipynb
├── README.md

## Project Workflow

**1. Data Loading:** The dataset consists of YouTube comments labeled as spam or ham, stored in 5 CSV files. The utils.py contains a helper function to load and preprocess the dataset
**2. Creating Label Functions:** I have defined multiple heuristic labeling functions using regex patterns and text properties.
**3. Applying LFs & Analysis**
**4. Label Model Training**
**5. Feature Extraction with TF-IDF**
**6. Training on LinearSVM and Logistic Regression**
**7. Evaluation of Models**
