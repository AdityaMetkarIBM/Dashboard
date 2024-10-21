import requests
from dotenv import load_dotenv
import os

# Load GitHub token from environment variable
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

BASE_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}"  # Replace with your GitHub token
}


def check_rate_limit():
    response = requests.get(f"{BASE_URL}/rate_limit", headers=HEADERS)
    
    if response.status_code == 200:
        rate_limit_data = response.json()
        core_limit = rate_limit_data['rate']['limit']
        remaining = rate_limit_data['rate']['remaining']
        reset_time = rate_limit_data['rate']['reset']
        
        print(f"Core limit: {core_limit}")
        print(f"Remaining: {remaining}")
        print(f"Reset time (UTC): {reset_time}")

        # Convert reset time to a more readable format
        from datetime import datetime
        reset_time_readable = datetime.utcfromtimestamp(reset_time).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Rate limit resets at: {reset_time_readable} UTC")
    else:
        print(f"Error fetching rate limit: {response.status_code} {response.text}")

# Example usage
check_rate_limit()
