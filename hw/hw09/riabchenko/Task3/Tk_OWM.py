import tkinter as tk
from tkinter import font
from OWM import get_weather_data

HEIGHT = 350
WIDTH = 450

def update_weather():
    city = entry_field.get()
    if not city:
        label.config(text="Please enter a city.")
        return

    weather_data = get_weather_data(city)
    
    if 'error' in weather_data:
        label.config(text=f"Error: {weather_data['error']}")
    else:
        weather_info = (f"Weather: {weather_data['detailed_status']}\n"
                        f"Wind Speed: {weather_data['wind_speed']} m/s\n"
                        f"Humidity: {weather_data['humidity']}%\n"
                        f"Temperature: {weather_data['temperature']}°C (Max: {weather_data['temp_max']}°C, Min: {weather_data['temp_min']}°C)\n"
                        f"Rain: {weather_data['rain']} mm\n"
                        f"Heat Index: {weather_data['heat_index']}\n"
                        f"Clouds: {weather_data['clouds']}%")
        label.config(text=weather_info)


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
                   command=update_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
