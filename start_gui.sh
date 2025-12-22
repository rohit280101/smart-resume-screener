#!/bin/bash
# Quick start script for Resume Screener GUI

echo "🚀 Starting Resume Screener GUI..."
echo ""
echo "Opening at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

cd "$(dirname "$0")"
streamlit run gui.py
