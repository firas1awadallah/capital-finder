from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_list = parse.parse_qsl(url_components.query)
        params_dict = dict(query_list)

        if 'country' in params_dict:
            country_param = params_dict.get('country')
            country_url = f'https://restcountries.com/v3.1/name/{country_param}'
            country_response = requests.get(country_url)
            country_data = country_response.json()
            capital_result = country_data[0]['capital'][0]
            message = f"The capital of {country_param} is {capital_result}"
        elif 'capital' in params_dict:
            capital_param = params_dict.get('capital')
            capital_url = f'https://restcountries.com/v3.1/capital/{capital_param}'
            capital_response = requests.get(capital_url)
            capital_data = capital_response.json()
            country_result = capital_data[0]['name']['common']
            message = f"{capital_param} is the capital of {country_result}"
        else:
            message = "Invalid request"

        self.wfile.write(message.encode())
        return
