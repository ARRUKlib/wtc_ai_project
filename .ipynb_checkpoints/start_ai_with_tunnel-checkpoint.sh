#!/bin/bash

echo "🐍 Activate Python venv..."
source venv/bin/activate

echo "🌐 Preparing cloudflared..."
mkdir -p ~/bin

if [ ! -f ~/bin/cloudflared ]; then
  echo "⬇️ Downloading cloudflared..."
  wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O ~/bin/cloudflared
  chmod +x ~/bin/cloudflared
fi

export PATH=$HOME/bin:$PATH

echo "🚀 Starting FastAPI server on port 8000..."
uvicorn main:app --host 0.0.0.0 --port 8000 &

sleep 5  # รอให้ uvicorn เปิดก่อน

echo "🚇 Opening Cloudflare tunnel..."
cloudflared tunnel --url http://localhost:8000
