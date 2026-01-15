import tkinter as tk #tkinter--tk interface
import requests

def get_weather():
    city = city_entry.get()

    if city == "":
        result_label.config(text="Please enter a city name")
        assistant_label.config(text="")
        return

    api_key = "80d3fa2d928bd972d344c50667d5ade4"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]

        result_label.config(text=f"Temperature: {temp} °C\nCondition: {condition}")

        # Assistant message
        if condition == "Rain":
            msg = "☔ It's raining – carry an umbrella!"
        elif temp >= 30:
            msg = "💧 It's very hot – stay hydrated!"
        elif 20 <= temp < 30:
            msg = "🙂 Pleasant weather – enjoy your day!"
        elif 10 <= temp < 20:
            msg = "🧥 It's cool – wear a light jacket!"
        else:
            msg = "❄ It's cold – wear warm clothes!"

        assistant_label.config(text=msg)

    except:
        result_label.config(text="City not found!")
        assistant_label.config(text="")


#creating main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x350")
root.configure(bg="skyblue")
#frame -- container storing diff widgets like label,buttons...

frame = tk.Frame(root, bg="skyblue", bd=0, highlightthickness=0)
frame.pack(pady=20)

title = tk.Label(frame, text="Weather App", font=("Arial", 20, "bold"),
                 bg="skyblue", fg="black")
title.pack(pady=10)

city_entry = tk.Entry(frame, font=("Arial", 14), bd=0, highlightthickness=0, justify="center")
city_entry.pack(pady=10)

get_btn = tk.Button(frame, text="Get Weather", font=("Arial", 15, "bold"),
                    bg="#2b235a", fg="white", bd=0, highlightthickness=0,
                    command=get_weather)
get_btn.pack(pady=10)

result_label = tk.Label(frame, text="", font=("Arial", 15),
                        bg="skyblue", fg="#2b235a")
result_label.pack(pady=10)

assistant_label = tk.Label(frame, text="", font=("Arial", 15, "italic"),
                           bg="skyblue", fg="black", wraplength=300)
assistant_label.pack(pady=10)
#running the window
root.mainloop()
