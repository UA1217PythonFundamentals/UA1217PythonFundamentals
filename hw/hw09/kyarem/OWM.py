from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(city):
    # Search for current weather in the specified city and get details
    observation = mgr.weather_at_place(city)
    w = observation.weather

    return (
        f"{w.detailed_status},\n"
        f"{w.wind()},\n"
        f"{w.humidity},\n"
        f"{w.temperature('celsius')},\n"
        f"{w.rain},\n"
        f"{w.heat_index},\n"
        f"{w.clouds}"
    )