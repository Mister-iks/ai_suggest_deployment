#!/usr/bin/python3
import os
from dotenv import load_dotenv
import requests
import json
import sys


load_dotenv()
API_URL = 'https://suggest.includes-ai.com/includes_suggest'

# Access the API key
API_KEY = os.getenv('API_KEY')

def includes_suggest(command):
    headers = {'Content-Type': 'application/json', 'x-api-key': API_KEY}
    data = {'command': command}
    
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json().get('suggested_command', 'No suggestion provided')
    else:
        return f"Error: {response.status_code}, {response.text}"

def main():
    if len(sys.argv) < 2:
        print("Usage: includes_suggest <command>")
        sys.exit(1)

    command = ' '.join(sys.argv[1:])
    suggestion = includes_suggest(command)
    print(f"Suggested command: {suggestion}")

if __name__ == "__main__":
    main()
