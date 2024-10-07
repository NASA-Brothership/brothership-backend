import requests
import base64
import datetime

class MeteomaticsInterface:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.token_url = 'https://login.meteomatics.com/api/v1/token'
        self.api_url = 'https://api.meteomatics.com'
        self.token = None

    def _get_token(self):
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

    def get_precipitation_one_days(self, latitude: float, longitude: float, date_time: datetime.datetime):
        if not self.token:
            self._get_token()

        formatted_time = date_time.strftime('%Y-%m-%dT%H:%M:%SZ')
        weather_url = f"{self.api_url}/{formatted_time}/precip_24h:mm/{latitude},{longitude}/json"

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

    def get_precipitation_days(self, latitude: float, longitude: float, start_datetime: datetime.datetime,  end_datetime: datetime.datetime):
        if not self.token:
            self._get_token()

        start_datetime = start_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
        end_datetime = end_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
        url = f"{self.api_url}/{start_datetime}--{end_datetime}:P1D/precip_24h:mm/{latitude},{longitude}/json?model=mix"

        # Faz a requisição da previsão do tempo
        response = requests.get(
            url,
            headers={
                'Authorization': f'Bearer {self.token}'
            }
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erro ao obter os dados do tempo: {response.status_code} - {response.text}")

    def get_precipitation_sum(self, data):
        # Extrair a lista de coordenadas e os valores de precipitação
        coordenadas = data['data'][0]['coordinates'][0]['dates']
        
        # Extrair os valores de precipitação
        valores_precipitacao = [item['value'] for item in coordenadas]
        
        # Calcular a média
        precipitation = sum(valores_precipitacao)
        
        return precipitation

if __name__ == "__main__":
    username = "sonoda_gustavoshoiti"
    password = "5P6Kmg1ktI"
    
    api = MeteomaticsInterface(username, password)
    
    latitude = 52.520551
    longitude = 13.461804
    start = datetime.datetime.now()
    end = start + datetime.timedelta(days=14)

    try:
        weather_data = api.get_precipitation_days(latitude, longitude, start, end)
        precipitation_mean = api.get_precipitation_sum(weather_data)
    except Exception as e:
        print(str(e))
