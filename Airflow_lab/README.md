# Crypto ETL Pipeline using Apache Airflow

## Overview

This project demonstrates a data engineering workflow using **Apache Airflow** to automate the **Extract, Transform, Load, and Analyze (ETL)** process for cryptocurrency data.

The workflow reads raw cryptocurrency data, performs data cleaning and transformation, loads the processed dataset into a clean file, and computes analytical metrics such as average price per cryptocurrency symbol.

**Apache Airflow**: Airflow is an open-source platform for programmatically authoring, scheduling, and monitoring workflows.

The workflow involves the following steps:
1. Extract raw cryptocurrency data from a local CSV file.
2. Transform and normalize the price fields.
3. Load the cleaned data into an output CSV file.
4. Analyze and compute the average price per symbol.

---

## Setting up the Lab
1. Clone the repository and navigate to the Airflow directory.
   ```bash
   git clone <repository_url>
   cd Airflow
   ```
2. Start the Airflow environment using Docker Compose
   ```bash
   docker-compose up -d
   ```
3. Access the Airflow Web UI
   ```bash
   http://localhost:8080
   ```
4. In the Airflow UI, locate the DAG named Crypto_ETL_Pipeline and toggle it to the “On” state.
5. To trigger the DAG manually, click Trigger DAG in the Airflow interface.
6. Once executed, the DAG performs the following tasks:
  a. extract_data: Reads raw data from crypto_raw.csv
  b. transform_data: Cleans and formats numeric fields
  c. load_data: Writes cleaned data to crypto_clean.csv
  d. analyze_data: Calculates average price per symbol and stores it in the output file

Below is a snapshot of a successful DAG run showing all four tasks completed successfully:

<img width="1470" height="837" alt="image" src="https://github.com/user-attachments/assets/8b1b9d0f-3d5d-46a2-bdce-efd0e38cd1f4" />
