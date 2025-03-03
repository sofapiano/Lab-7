import requests
import json

# функция для загрузки данных с API
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка: {response.status_code}")
        return None


if __name__ == "__main__":
    # загрузка данных о местоположении МКС
    url_iss = "http://api.open-notify.org/iss-now.json"
    iss_data = fetch_data(url_iss)

    # загрузка данных о космонавтах на МКС
    url_astros = "http://api.open-notify.org/astros.json"
    astros_data = fetch_data(url_astros)

    # объединение данных в один JSON-объект
    combined_data = {
        "iss_position": iss_data,
        "astros": astros_data
    }

    with open("space_data.json", "w", encoding="utf-8") as file:
        json.dump(combined_data, file, ensure_ascii=False, indent=4)