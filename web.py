# import cv2
# import numpy as np
# import json
# import time
# import keyboard
# from math import sqrt
# from PIL import Image
# import numpy as np
# import pytesseract 
# from googletrans import Translator, constants
# from pprint import pprint
# import spacy
# from spacy import displacy
# import re
# from collections import defaultdict
# import numpy as np
# import requests
# import wikipedia
# import pandas as pd
# from selenium import webdriver
# import pyautogui
# from PIL import ImageGrab

# def web_part():
#     browser = webdriver.Chrome('/Users/maheshjain/Desktop/Brain/godsEye/chromedriver')
#     browser.get('https://yandex.com/images/')
#     search_input = browser.find_element_by_class_name("input__cbir-button.input__button")
#     time.sleep(1)
#     search_input.click()
#     search_input1 = browser.find_element_by_class_name("Button2")
#     time.sleep(1)
#     search_input1.click()
#     pyautogui.click(x=813, y=228, button='left')
#     pyautogui.click(x=871, y=216, interval=1, button='left')
#     pyautogui.click(x=900, y=286, interval=1, button='left')
#     pyautogui.click(x=884, y=190, button='left')
#     pyautogui.click(x=969, y=558, interval=1, button='left')
#     time.sleep(10)
#     im = pyautogui.screenshot(region=(626*2,310*2, 1182, 150))
#     im.save('screenshot2.png')
#     pyautogui.click(x=42, y=69, interval=1, button='left')
#     NER = spacy.load("en_core_web_sm")
#     hello= []
#     edit = []
#     img_cv = cv2.imread('godsEye/screenshot2.png')
#     img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
#     grayImage = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)


#     yello = pytesseract.image_to_string(img_rgb,lang="rus")
#     yello1 = pytesseract.image_to_string(img_rgb,lang="eng")
#     yello1 = yello1.split()
#     translator = Translator()
#     translation = translator.translate(yello)
#     raw_text= str(translation.text)
#     raw_text1 = raw_text.split()
#     text1= NER(raw_text)
#     for word in text1.ents:
#         hello.append((word.text,word.label_))
        
#     def Repeat(x):
#         _size = len(x)
#         repeated = []
#         for i in range(_size):
#             k = i + 1
#             for j in range(k, _size):
#                 if x[i] == x[j] and x[i] not in repeated:
#                     repeated.append(x[i])
#         return repeated

#     hello1 = Repeat(raw_text1)
#     hello1 = ' '.join(hello1)
#     edit.append(hello1)
#     hello2 = Repeat(yello1)
#     hello2 = ' '.join(hello2)
#     edit.append(hello2)

#     for list1 in hello:
#         if list1[1] =='ORG' or list[1] =='PERSON':
#             edit.append(list1[0])

#     res = []

#     [res.append(x) for x in edit if x not in res]

#     while("" in res) :
#         res.remove("")
        
#     for i in res:
#         word=i.replace('logo','')
#         summary= wikipedia.summary(word,sentences=2)
     
#     text = summary
#     content= textwrap.fill(text, width=55)
#     hello12 = cv2.putText(image2, summary)
#     cv2.imshow("final", hello12) 

import time

# Start the timer
start_time = time.time()

# Your code goes here
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import requests

def web_part():


    file_path = "1.jpg"
    search_url = 'https://yandex.ru/images/search'
    files = {'upfile': ('blob', open(file_path, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(search_url, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url = search_url + '?' + query_string
    print(img_search_url)
    # Configure Chrome options for running in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Initialize the WebDriver with the configured Chrome options
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    time.sleep(1)
    driver.get(img_search_url)
    page_source = driver.page_source

    # Parse the page source using Beautiful Soup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all <span> elements with class "Button2-Text"
    span_elements = soup.find_all('span', class_='Button2-Text')

    # Iterate over the found elements and print their contents
    for span in span_elements:
        print(span.text)

    # Close the WebDriver
    driver.quit()

    # End the timer and calculate the execution time
    end_time = time.time()
    execution_time = end_time - start_time

    # Print the execution time
    print("Execution time:", execution_time, "seconds")


