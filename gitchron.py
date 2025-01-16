import os
from datetime import datetime
import subprocess
import requests

# Set your repository path
repo_path = "/Users/natewardy/Desktop/gitchron"

# OpenWeatherMap API setup
api_key = "415315e4cb827aaa3ae143c31ac6eed2"
city = "Columbia"
state = "SC"
country = "US"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={api_key}&units=imperial"

# Change directory to the repository
os.chdir(repo_path)

# Path to the log file
log_file = "log.txt"

# Fetch weather data
try:
    response = requests.get(weather_url)
    response.raise_for_status()
    weather_data = response.json()
    weather_main = weather_data['weather'][0]['description'].capitalize()
    temperature = weather_data['main']['temp']
    weather_log = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Weather: {weather_main}, Temp: {temperature}°F"
except Exception as e:
    weather_log = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Failed to fetch weather data: {e}"

# Overwrite the log file with today's weather data
with open(log_file, "w") as file:
    file.write(weather_log + "\n")

# Add the file to the Git index
subprocess.run(["git", "add", log_file], check=True)

# Commit the changes
commit_message = f"Updated log.txt with weather data on {datetime.now().strftime('%Y-%m-%d')}"
subprocess.run(["git", "commit", "-m", commit_message], check=True)

# Push to the remote repository
subprocess.run(["git", "push"], check=True)

print(f"Log updated with weather data: {weather_log}")
