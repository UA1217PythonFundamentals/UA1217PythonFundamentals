import tkinter as tk
from tkinter import font
from pyowm import OWM

HEIGHT = 600
WIDTH = 600


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()
def get_weather():
    city = entry_field.get()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    wind = w.wind()  # Call the method to get wind data
    temperature = w.temperature('celsius')
    weather_info = (
        f"City: {city}\n"
        f"Status: {w.detailed_status.capitalize()}\n"
        f"Wind Speed: {wind['speed']} m/s\n"
        f"Wind Direction: {wind.get('deg', 'N/A')}°\n"
        f"Humidity: {w.humidity}%\n"
        f"Temperature: {temperature['temp']}°C\n"
        f"Max Temp: {temperature['temp_max']}°C\n"
        f"Min Temp: {temperature['temp_min']}°C\n"
        f"Cloudiness: {w.clouds}%\n"
    )
    label['text'] = weather_info



frame = tk.Frame(root, bg="black", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="black", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

