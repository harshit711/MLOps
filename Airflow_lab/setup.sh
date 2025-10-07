#!/bin/bash
set -e

# Remove existing .env file if it exists
rm -rf ./logs ./plugins ./config

# Stop and remove containers, networks, and volumes
docker compose down -v

# Create required Airflow directories
mkdir -p ./logs ./plugins ./config

# Write the current user's UID into .env
echo "AIRFLOW_UID=$(id -u)" | tee .env > /dev/null

# Run airflow CLI to show current config
docker compose run --rm airflow-cli airflow config list

docker compose up airflow-init

docker compose up -d