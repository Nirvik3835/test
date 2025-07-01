import tkinter as tk
import requests
from tkinter import messagebox

API_KEY = "abb321ac1a060c914b495cd104764c31"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    # API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        print("DEBUG:", data)

        if data.get("cod") != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result = f"""
📍 City: {city}
🌡️ Temperature: {temp}°C
☁️ Condition: {weather}
💧 Humidity: {humidity}%
🍃 Wind Speed: {wind} m/s
"""
        result_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch weather data.\n{e}")

# ---------------------- GUI Setup ---------------------- #

root = tk.Tk()
root.title("Live Weather App")
root.geometry("420x350")
root.resizable(False, False)
root.configure(bg="#1e1e1e")  # Dark mode

# Fonts and styles
label_style = {"font": ("Arial", 12), "bg": "#1e1e1e", "fg": "white"}
entry_style = {"font": ("Arial", 12)}

# City input
tk.Label(root, text="Enter City Name:", **label_style).pack(pady=(20, 5))
city_entry = tk.Entry(root, width=30, **entry_style)
city_entry.pack(pady=5)

# Get Weather button
tk.Button(root, text="Get Weather", command=get_weather,
          bg="#03a9f4", fg="white", font=("Arial", 12), width=20).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 11), bg="#1e1e1e", fg="lightgreen", justify="left")
result_label.pack(pady=20)

# Run the app
print("✅ Weather app is running...")
root.mainloop()
print("DEBUG:", data)
