from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

def get_weather(city):
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        weather_info = {
            'status': w.detailed_status,
            'wind': w.wind(),
            'humidity': w.humidity,
            'temperature': w.temperature('celsius'),
            'clouds': w.clouds
        }

        return weather_info

    except Exception as e:
        print(f"Error fetching weather data: {str(e)}")
        return None
