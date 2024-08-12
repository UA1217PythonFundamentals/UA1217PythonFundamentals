from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'


owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather_data(city):
    try:
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        return {
            'detailed_status': weather.detailed_status.capitalize(),
            'wind_speed': weather.wind()['speed'],
            'humidity': weather.humidity,
            'temperature': weather.temperature('celsius')['temp'],
            'temp_max': weather.temperature('celsius')['temp_max'],
            'temp_min': weather.temperature('celsius')['temp_min'],
            'rain': weather.rain.get('1h', 0),  # Rain in mm per hour
            'heat_index': weather.heat_index if weather.heat_index is not None else "Not available",
            'clouds': weather.clouds
        }
    except Exception as e:
        return {'error': str(e)}
