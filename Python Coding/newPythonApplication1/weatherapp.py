import requests
import tkinter as tk
from tkinter import messagebox



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

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        result_str = (
            f"\nCity: {weather_data['name']}\n"
            f"Temperature: {weather_data['main']['temp']}°C\n"
            f"Condition: {weather_data['weather'][0]['description']}\n"
            f"Humidity: {weather_data['main']['humidity']}%\n"
            f"Wind Speed: {weather_data['wind']['speed']} m/s"
        )
        return result_str
    else:
        return "Weather data not available."

def get_weather_and_display(api_key, city, result_label):
    weather_data = get_weather(api_key, city)
    result_str = display_weather(weather_data)
    result_label.config(text=result_str)

def main():
    api_key = 'f223c151181072bd0b2292d3f58d2149'  # Replace with your OpenWeatherMap API key

    # Tkinter GUI setup
    root = tk.Tk()
    root.title("Weather App")

    # Labels and Entry widgets
    city_label = tk.Label(root, text="Enter city name:")
    city_entry = tk.Entry(root)
    result_label = tk.Label(root, text="Weather information will be displayed here.")

    # Button to trigger weather retrieval
    get_weather_button = tk.Button(
        root,
        text="Get Weather",
        command=lambda: get_weather_and_display(
            api_key, city_entry.get(), result_label
        ),
    )

    # Packing widgets
    city_label.pack()
    city_entry.pack()
    get_weather_button.pack()
    result_label.pack()

    # Running the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
