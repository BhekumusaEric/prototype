#!/bin/bash

echo "🚗 Starting WesBank FML EV Fleet Analytics System..."
echo "=================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip first."
    exit 1
fi

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies. Please check your Python environment."
    exit 1
fi

echo "✅ Dependencies installed successfully!"

# Start the Flask server in background
echo "🚀 Starting Flask backend server..."
python app.py &
FLASK_PID=$!

# Wait a moment for server to start
sleep 3

# Check if Flask server is running
if ps -p $FLASK_PID > /dev/null; then
    echo "✅ Backend server started successfully on http://localhost:5000"
else
    echo "❌ Failed to start backend server"
    exit 1
fi

# Start simple HTTP server for frontend
echo "🌐 Starting frontend server..."
python -m http.server 8080 &
HTTP_PID=$!

sleep 2

if ps -p $HTTP_PID > /dev/null; then
    echo "✅ Frontend server started successfully on http://localhost:8080"
else
    echo "❌ Failed to start frontend server"
    kill $FLASK_PID 2>/dev/null
    exit 1
fi

echo ""
echo "🎉 WesBank FML EV Fleet Analytics System is now running!"
echo "=================================================="
echo "📊 Dashboard: http://localhost:8080"
echo "🔌 API Server: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop all servers..."

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down servers..."
    kill $FLASK_PID 2>/dev/null
    kill $HTTP_PID 2>/dev/null
    echo "✅ All servers stopped. Goodbye!"
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Keep script running
while true; do
    sleep 1
done