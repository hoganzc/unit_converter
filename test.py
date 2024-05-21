import requests


def main():
    url = "http://127.0.0.1:5000/api/convert"

    data = {
        "unit": "lbs",
        "amount": 1
    }

    response = requests.get(url, json=data)
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
        return response.json()


print(main())