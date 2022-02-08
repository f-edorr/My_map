import requests
from io import BytesIO

class Map:
    @staticmethod
    def find_toponym(toponym):
        search_api_server = "https://search-maps.yandex.ru/v1/"
        api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

        search_params = {
            "apikey": api_key,
            "text": toponym,
            "lang": "ru_RU",
            "type": "geo"
        }

        response = requests.get(search_api_server, params=search_params)

        if not response:
            print("Ошибка выполнения запроса:")
            print("Http статус:", response.status_code, "(", response.reason, ")")

        json_response = response.json()

        # Координаты центра топонима:
        toponym_coodrinates = json_response["features"][0]['geometry']['coordinates']

        bounded_coords = response.json()["features"][0]["properties"]["boundedBy"]

        delta = abs(bounded_coords[0][0] - bounded_coords[1][0]) / 2, \
                abs(bounded_coords[0][1] - bounded_coords[1][1]) / 2

        return toponym_coodrinates, bounded_coords, delta

    @staticmethod
    def get_image(adress):
        toponym = Map.find_toponym(adress)

        map_params = {
            "ll": ",".join([str(toponym[0][0]), str(toponym[0][1])]),
            "spn": ",".join([str(toponym[2][0]), str(toponym[2][1])]),
            "l": "map"
        }

        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=map_params)
        file = open("data/map.png", mode="wb")
        file.write(response.content)
        file.close()

