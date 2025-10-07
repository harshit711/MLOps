#!/bin/bash
set -e

# Remove existing .env file if it exists
echo "🧹 Cleaning old environment..."
rm -rf ./logs ./plugins ./config

# Stop and remove containers, networks, and volumes
docker compose down -v

# Create required Airflow directories
echo "📂 Creating Airflow directories..."
mkdir -p ./logs ./plugins ./config

# Write the current user's UID into .env
echo "👤 Setting AIRFLOW_UID..."
echo "AIRFLOW_UID=$(id -u)" | tee .env > /dev/null

# Run airflow CLI to show current config
echo "👤 Setting AIRFLOW_UID..."
docker compose run --rm airflow-cli airflow config list

echo "🗃️ Initializing Airflow metadata database..."
docker compose up airflow-init

echo "🚀 Starting Airflow services..."
docker compose up -d