import cv2
import numpy as np
import json
import time
import keyboard
from math import sqrt
from PIL import Image
import numpy as np
import pytesseract 
from pprint import pprint
import spacy
from spacy import displacy
import re
from collections import defaultdict
import numpy as np
import requests
import wikipedia
import pandas as pd
from selenium import webdriver
import pyautogui
from PIL import ImageGrab, Image, ImageDraw, ImageFont
from deep_translator import (GoogleTranslator) 
import textwrap
from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import difflib
from fuzzywuzzy import process




def webPart():
    main_list=[]
    final=[]
    browser = webdriver.Chrome('/Users/maheshjain/Desktop/Brain/godsEye/chromedriver')
    browser.get(f'https://yandex.ru/images/search?cbir_id=2512137%2F6_49cComoUjpkLFHqrCQbQ2800&rpt=imageview&lr=10562')
    time.sleep(10)
    im = pyautogui.screenshot(region=(626*2,310*2, 1182, 350))
    im.save('screenshot2.png')
    pyautogui.click(x=42, y=69, interval=1, button='left')
    final=[]
     
    NER = spacy.load("en_core_web_sm")
    hello= []
    edit = []
    img_cv = cv2.imread('screenshot2.png')
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    grayImage = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)


    yello = pytesseract.image_to_string(img_rgb,lang="rus")
    yello1 = pytesseract.image_to_string(img_rgb,lang="eng")
    yello1 = yello1.split()
    translated = GoogleTranslator(source='ru', target='en').translate(text=yello)
    print(translated)
    raw_text= str(translated)
    raw_text1 = raw_text.split()
   

    n=0
    list_one = []
    nameName = []

    df = pd.read_excel('Names.xlsx')
    strOptions = df['Name'].to_list()

    for names in raw_text1:
        for found, score in process.extract(names,strOptions):
            if score > 95:
                nameName.append(found)
        


    url1 = "https://www.google.com/search?q="
    url = url1 +str(nameName[0]) +"wiki"
    request_result=requests.get( url )
    soup = bs(request_result.text,"html.parser")
    links = soup.find("a")
    for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
             list_one.append(re.split(":(?=http)",link["href"].replace("/url?q=",""))) 
    
    hello = str(list_one[0])
    hello1 = re.split("'", hello)[1]
    hello2 = re.split("&", hello1)[0]
    print(hello2)
    r = requests.get(hello2)
    soup = bs(r.content, "lxml")
    div = soup.find("h1", {"id": "firstHeading"})
    x = div.string
    x = x + " " + " " + " "
    url = soup.select("td.infobox-image")
    url = str(url)
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,url)
    main_url=url[0]
    main_url = [t for t in main_url if t]
    main_url = main_url[0]
    final_url = "https://"+str(main_url)
    urllib.request.urlretrieve(final_url, "logo_image.png")
    list_one.clear()
    url1 = "logo_image.png"
    text10 = ''
    for paragraph in soup.find_all('p'):
        text10 += paragraph.text

    sep = '\n'
    stripped = text10.split(sep)[1]
    
    text = stripped
    content= textwrap.fill(text, width=35)    
    im = Image.new('RGBA', (500, 300), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    im2 = Image.open(url1)
    im2 = im2.resize((150,190))
    im.paste(im2,(50,60))
    title_font = ImageFont.truetype('Roboto-Bold.ttf', 12)
    title_font1 = ImageFont.truetype('Roboto-Bold.ttf', 10)
    image_editable = ImageDraw.Draw(im)
    image_editable.text((230,100), content, (0,0,0), font=title_font)
    im.show()
    PATH = "/Users/maheshjain/Desktop/Brain/card/"
    im.save(PATH+'card'+'.png','PNG')
    nameName.clear()
    


webPart()

"""
    try:
        search = final[n]
        search = search.replace(" ", "+")
        r = requests.get('https://www.google.com/search?q='+search)
        soup = bs(r.content, "lxml")
        url = soup.select("a[href*=wikipedia]")[0]
        url = str(url)
        end1 = url.find('&amp;')
        two = url[: end1]
        x = two.replace('<a href="/url?q=', "", 1)
        r = requests.get(x)
        soup = bs(r.content, "lxml")
        url = soup.select("h1.firstHeading")
        url = str(url)
        end1 = url.find('</h1>')
        two = url[: end1]
        x = two.replace('[<h1 class="firstHeading" id="firstHeading">', "", 1)
        x = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', x)
        x = ' '.join(x)
        print(x)
        summary= wikipedia.summary( x ,sentences=2)
        print(summary)

    except (wikipedia.exceptions.PageError, IndexError):
        n = n+1
        search = final[n]
        search = search.replace(" ", "+")
        r = requests.get('https://www.google.com/search?q='+search)
        soup = bs(r.content, "lxml")
        url = soup.select("a[href*=wikipedia]")[0]
        url = str(url)
        end1 = url.find('&amp;')
        two = url[: end1]
        x = two.replace('<a href="/url?q=', "", 1)
        r = requests.get(x)
        soup = bs(r.content)
        url = soup.select("h1.firstHeading")
        url = str(url)
        end1 = url.find('</h1>')
        two = url[: end1]
        x = two.replace('[<h1 class="firstHeading" id="firstHeading">', "", 1)
        x = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', x)
        x = ' '.join(x)
        print(x)
        summary= wikipedia.summary(x,sentences=2)
        print(summary)
    
 
       

    search = final[n]
    search = search.replace(" ", "+")
    r = requests.get('https://www.google.com/search?q='+search)
    soup = bs(r.content, "lxml")
    url = soup.select("a[href*=wikipedia]")[0]
    url = str(url)
    end1 = url.find('&amp;')
    two = url[: end1]
    x = two.replace('<a href="/url?q=', "", 1)
    r = requests.get(x)
    soup = bs(r.content, "lxml")
    url = soup.select("td.infobox-image")
    url = str(url)
    end1 = url.find('1.5x, //')
    two = url[end1 :]
    split_string = two.split(" ", 2)[1]
    split_string = "https:"+split_string
    urllib.request.urlretrieve(split_string, "logo_image.png")
    url1 = "logo_image.png"
    text = summary
    content= textwrap.fill(text, width=35)    
    im = Image.new('RGBA', (500, 300), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    im2 = Image.open(url1)
    im2 = im2.resize((150,190))
    im.paste(im2,(50,60))
    title_font = ImageFont.truetype('Roboto-Bold.ttf', 12)
    title_font1 = ImageFont.truetype('Roboto-Bold.ttf', 10)
    image_editable = ImageDraw.Draw(im)
    image_editable.text((230,70), "DESCRIPTION :" + " " + final[n], (0,0,0), font=title_font)
    image_editable.text((230,100), content, (0,0,0), font=title_font)
    im.show()
    PATH = "/Users/maheshjain/Desktop/Brain/card/"
    im.save(PATH+'card'+'.png','PNG')
"""


