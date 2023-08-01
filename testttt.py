from selenium import webdriver
 
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(f'https://yandex.ru/images/search?cbir_id=3598935%2F6_49cComoUjpkLFHqrCQbQ2565&rpt=imageview&lr=110480')
pageSource = driver.page_source
fileToWrite = open("page_source.html", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
fileToRead = open("page_source.html", "r")
print(fileToRead.read())
fileToRead.close()
driver.quit()