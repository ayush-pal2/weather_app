A simple Weather Forecast Web App built using Django that allows users to enter a city name and fetch real-time weather data (temperature, humidity, condition) by integrating with the OpenWeatherMap API.


🚀 Features
Search weather by city name.
Fetches current temperature, humidity, and weather condition.
Uses OpenWeatherMap Geo API to convert city name to latitude & longitude.
Simple, responsive UI with vibrant design.
Clean API integration using Python requests.

📸 Preview


🛠️ Tech Stack
Python 3.x
Django 4.x
HTML5 & CSS3
OpenWeatherMap API

⚙️ Installation & Setup
git clone https://github.com/ayush-pal2/weather_app
cd django-weather-app

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

pip install django requests

python manage.py migrate
python manage.py runserver

http://127.0.0.1:8000/



