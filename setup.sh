#!/bin/bash

echo "🔧 Setting up Python venv..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

echo "📦 Installing all dependencies..."
pip install -r requirements.txt

echo "🚀 Starting server on port 8000"
uvicorn main:app --host 0.0.0.0 --port 8000

export PATH=$HOME/bin:$PATH
cloudflared tunnel --url http://localhost:8000
