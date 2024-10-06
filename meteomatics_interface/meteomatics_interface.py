import requests
import base64
import datetime

class MeteomaticsAPI:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.token_url = 'https://login.meteomatics.com/api/v1/token'
        self.api_url = 'https://api.meteomatics.com'
        self.token = None

    def get_token(self):
        credentials = f"{self.username}:{self.password}".encode("utf-8")
        auth_header = base64.b64encode(credentials).decode("utf-8")

        response = requests.get(
            self.token_url,
            headers={
                'Authorization': f'Basic {auth_header}'
            }
        )

        if response.status_code == 200:
            self.token = response.json().get('access_token')
        else:
            raise Exception(f"Erro ao obter o token: {response.status_code} - {response.text}")

    def get_weather(self, latitude: float, longitude: float, date_time: datetime.datetime):
        if not self.token:
            self.get_token()

        formatted_time = date_time.strftime('%Y-%m-%dT%H:%M:%SZ')
        weather_url = f"{self.api_url}/{formatted_time}/t_2m:C/{latitude},{longitude}/json"

        # Faz a requisição da previsão do tempo
        response = requests.get(
            weather_url,
            headers={
                'Authorization': f'Bearer {self.token}'
            }
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erro ao obter os dados do tempo: {response.status_code} - {response.text}")

if __name__ == "__main__":
    username = "sonoda_gustavoshoiti"
    password = "5P6Kmg1ktI"
    
    api = MeteomaticsAPI(username, password)
    
    latitude = 52.520551
    longitude = 13.461804
    date_time = datetime.datetime(2024, 10, 6, 0, 0, 0)

    try:
        weather_data = api.get_weather(latitude, longitude, date_time)
        print(weather_data)
    except Exception as e:
        print(str(e))
