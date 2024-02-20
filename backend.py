import requests

API_KEY = "ee5f7220a85cf0c1989f93a6d1da65a5"


def get_data(place, days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [filtered_data[i]['main']['temp'] for i in
                         range(nr_values)]
    if kind == "Sky":
        filtered_data = [filtered_data[i]['weather'][0]['main'] for i in
                         range(nr_values)]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Tokyo", days=3, kind="Sky"))
