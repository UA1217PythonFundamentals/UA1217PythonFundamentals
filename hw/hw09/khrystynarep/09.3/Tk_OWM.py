import tkinter as tk
from tkinter import font

from pkg_resources import *
from OWM import get_weather  

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

def get_weather_command():
    city = entry_field.get().strip()
    if city:
        weather_data = get_weather(city)
        if weather_data:
            weather_info = (
                f"Detailed Status: {weather_data['status']}\n"
                f"Wind: {weather_data['wind']}\n"
                f"Humidity: {weather_data['humidity']}%\n"
                f"Temperature: {weather_data['temperature']['temp']}°C\n"
                f"Clouds: {weather_data['clouds']}%"
            )
            label.config(text=weather_info)
        else:
            label.config(text="Error fetching weather data.")
    else:
        label.config(text="Please enter a city.")

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=get_weather_command)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), anchor='nw', justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
