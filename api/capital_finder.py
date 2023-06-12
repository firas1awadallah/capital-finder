from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    # list_of_dif=[]
    message="testing"
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_list = parse.parse_qsl(url_components.query)
    my_dict = dict(query_list)

    # print(111,my_dict)
    if 'country' in my_dict:
      country = my_dict.get('country')
      url= 'https://restcountries.com/v3.1/name/{name}'
      res = requests.get(url+country)
      data = res.json()
    #   print(222,data)
    for country_data in data :
      Country = country_data['name']
      message = str(Country)
    #   list_of_dif.append(message)
    # print(2222,list_of_dif)


    self.wfile.write(message.encode())
    return