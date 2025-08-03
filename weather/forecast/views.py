from django.shortcuts import render
import requests

def home(request):
    weather_data = None
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '66003f43c4f4abbe4f8a6512b668b67d'
        
        # First API Call: Get lat & lon
        geo_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}'
        res = requests.get(geo_url)
        
        if res.status_code == 200 and res.json():
            geo_data = res.json()
            
            lat = geo_data[0]['lat']
            lon = geo_data[0]['lon']
            
            # Second API Call: Get weather data using lat/lon
            weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
            response = requests.get(weather_url)
            
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'condition': data['weather'][0]['description']
                }
            else:
                weather_data = {'error': 'Weather data not found.'}
        else:
            print(res)
            weather_data = {'error': 'City not found.'}
            
    return render(request, 'forecast/index.html', {'weather_data': weather_data})
