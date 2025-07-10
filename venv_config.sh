#!/bin/bash

# Stop on error
set -e

# venv variable names
ENV_NAME="venv-nutria"
KERNEL_NAME="nutria"
KERNEL_DISPLAY_NAME="NutrIA"

echo "🔧 Creating virtual environment: $ENV_NAME"
python3 -m venv $ENV_NAME

echo "📦 Activating environment and installing packages..."
source "$ENV_NAME/bin/activate"
pip install --upgrade pip
pip install openai google-genai jupyter ipykernel

echo "🧠 Registering Jupyter kernel: $KERNEL_DISPLAY_NAME"
python -m ipykernel install --user --name=$KERNEL_NAME --display-name="$KERNEL_DISPLAY_NAME"

echo "✅ Environment setup complete"