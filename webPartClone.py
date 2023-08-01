import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

file_path = "testt.jpeg"
search_url = 'https://yandex.ru/images/search'
files = {'upfile': ('blob', open(file_path, 'rb'), 'image/jpeg')}
params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
response = requests.post(search_url, params=params, files=files)
query_string = json.loads(response.content)['blocks'][0]['params']['url']
img_search_url = search_url + '?' + query_string
browser = webdriver.Chrome('chromedriver')
browser.get(img_search_url)
