import requests
import json

# Выполняем GET-запрос
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": 59.93,
    "lon": 30.34,
    "appid": "0d015f1e8c78cecaaac74b822060d1f9"
}
response = requests.get(url, params=params)

# Проверяем, что запрос успешен
if response.status_code == 200:
    # Преобразуем ответ в JSON (если ответ уже в JSON)
    data = response.json()

    # Сохраняем данные в JSON-файл
    with open("weather_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    # сохраняем в отдельные переменные температуру, погоду, давление и влажность
    temp_k = data["main"]["temp"]
    temp = f"{(temp_k - 273):.2f}"
    weather = data["weather"][0]["main"]
    pressure_hpa = data["main"]["pressure"]
    pressure = f"{(pressure_hpa / 101325 * 760 * 100):.2f}"
    humidity = data["main"]["humidity"]

    print("погода в Санкт-Петербурге на сегодня:")
    print(f"температура: {temp}")
    print(f"погода: {weather}")
    print(f"давление: {pressure}")
    print(f"влажность: {humidity}")

else:
    print(f"Ошибка: {response.status_code}")