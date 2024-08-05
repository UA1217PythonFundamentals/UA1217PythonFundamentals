import tkinter as tk
from tkinter import font
from pyowm import OWM

# Weather API setup
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Function to get weather based on city name
def get_weather_data():
    city = entry_field.get()
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        
        # Extract weather details
        detailed_status = w.detailed_status
        wind = w.wind()
        humidity = w.humidity
        temperature = w.temperature('celsius')
        rain = w.rain
        heat_index = w.heat_index
        clouds = w.clouds
        
        # Format and display the weather information
        weather_info = (
            f"Weather: {detailed_status}\n"
            f"Wind Speed: {wind.get('speed', 'N/A')} m/s\n"
            f"Humidity: {humidity}%\n"
            f"Temperature: {temperature['temp']}°C (Max: {temperature['temp_max']}°C, Min: {temperature['temp_min']}°C)\n"
            f"Rain: {rain.get('1h', 'N/A')} mm\n"
            f"Heat Index: {heat_index if heat_index is not None else 'N/A'}\n"
            f"Cloudiness: {clouds}%"
        )
    except Exception as e:
        weather_info = f"Error: {e}"

    label.config(text=weather_info)

# Tkinter setup
HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=get_weather_data)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
