#!/bin/bash
dos2unix client.py
pip install -r requirements.txt
if [ -f "/usr/local/bin/ai_suggest" ]; then
    echo "ai_suggest already exists. Overwriting..."
fi
cp client.py /usr/local/bin/ai_suggest
chmod +x /usr/local/bin/ai_suggest
echo "ai_suggest has been installed successfully."
echo "Please ensure the shebang line at the top of 'client.py' is correct. It should point to your Python interpreter (e.g., '#!/usr/bin/env python3')."
