#!/usr/bin/python3
import requests
import json
import sys

API_URL = 'https://suggest.includes-ai.com/includes_suggest'
API_KEY = 'bl3c79nGIDGp2CNwScU8oPNnSM5TZdetj0S9gpLQ2FuyYXhh7Y'

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
