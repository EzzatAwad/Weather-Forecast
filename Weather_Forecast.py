import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        precipitation = data['clouds']['all']

        return temperature, humidity, wind_speed, pressure, precipitation
    except Exception as e:
        print(f"Error: {e}")
        return None

def search_weather():
    city = location_entry.get()

    if not city:
        messagebox.showinfo("Error", "Please enter a location.")
        return

    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    weather_data = get_weather(api_key, city)

    if weather_data:
        temperature_label.config(text=f"Temperature: {weather_data[0]}°C")
        humidity_label.config(text=f"Humidity: {weather_data[1]}%")
        wind_speed_label.config(text=f"Wind Speed: {weather_data[2]} km/h")
        pressure_label.config(text=f"Pressure: {weather_data[3]} hPa")
        precipitation_label.config(text=f"Precipitation: {weather_data[4]}%")

root = tk.Tk()
root.title("Weather Forecast")

location_label = tk.Label(root, text="Enter Location:")
location_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search_weather)
temperature_label = tk.Label(root, text="Temperature: ")
humidity_label = tk.Label(root, text="Humidity: ")
wind_speed_label = tk.Label(root, text="Wind Speed: ")
pressure_label = tk.Label(root, text="Pressure: ")
precipitation_label = tk.Label(root, text="Precipitation: ")

location_label.grid(row=0, column=0, pady=10, padx=10, sticky="e")
location_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")
search_button.grid(row=0, column=2, pady=10, padx=10)
temperature_label.grid(row=1, column=0, pady=5)
humidity_label.grid(row=2, column=0, pady=5)
wind_speed_label.grid(row=3, column=0, pady=5)
pressure_label.grid(row=4, column=0, pady=5)
precipitation_label.grid(row=5, column=0, pady=5)


root.mainloop()
