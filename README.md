🌤️ Weather App (Django + OpenWeatherMap API)

A simple Weather Forecast Web App built using Django that allows users to enter a city name and fetch real-time weather data (temperature, humidity, condition) by integrating with the OpenWeatherMap API.

📸 Preview
<img width="1440" height="779" alt="Screenshot 2025-08-03 at 14 19 07" src="https://github.com/user-attachments/assets/645b7799-d913-4316-b834-439750eecccd" />
<img width="1440" height="779" alt="Screenshot 2025-08-03 at 14 19 17" src="https://github.com/user-attachments/assets/a334b36f-be01-4c84-9076-96e3680da4a7" />
<img width="1440" height="778" alt="Screenshot 2025-08-03 at 14 19 25" src="https://github.com/user-attachments/assets/308b3092-db63-4373-b563-fba9f5f74cda" />

🚀 Features

* Search weather by city name.
* Fetches current temperature, humidity, and weather condition.
* Uses OpenWeatherMap Geo API to convert city name to latitude & longitude.
* Simple, responsive UI with vibrant design.
* Clean API integration using Python requests.

🛠️ Tech Stack
* Python 3.x
* Django 4.x
* HTML5 & CSS3
* OpenWeatherMap API

⚙️ Installation & Setup
Clone the Repository

git clone https://github.com/yourusername/django-weather-app.git
cd django-weather-app

* Create Virtual Environment & Activate 
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

* Install Dependencies
pip install django requests

* Add Your OpenWeatherMap API Key

Open views.py
Replace api_key = 'YOUR_API_KEY' with your actual API Key

* Run Migrations & Start Server
python manage.py migrate
python manage.py runserver


🧩 API Usage Flow
* User enters a city name.
* Geo API (/geo/1.0/direct) converts city to latitude & longitude
* Weather API (/data/2.5/weather) fetches current weather data using lat & lon
* Data is rendered dynamically on the webpage.
