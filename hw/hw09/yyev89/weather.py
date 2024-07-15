# Task 9.3 Weather program
import tkinter as tk
from tkinter import font
from pyowm import OWM

HEIGHT = 350
WIDTH = 450
API_KEY = 'ef2206ff5da67de63306d0b143e20872'

def get_weather(city: str):
    '''Gets city as parameter and displays its weather on the label widget'''
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        weather_data = f'''
        Details: {w.detailed_status}
        Wind speed: {w.wind()['speed']} m/sec
        Humidity: {w.humidity}%
        Temperature: {w.temperature('celsius')['temp']}°C
        Rain: {w.rain}
        Heat Index: {w.heat_index}
        Clouds: {w.clouds}%
        '''
        label.config(text=weather_data)
    except Exception:
        label.config(text="Please enter a correct city")


owm = OWM(API_KEY)
mgr = owm.weather_manager()

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()