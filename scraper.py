from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"  # URL of the NASA Exoplanet Catalog

# Webdriver
browser = webdriver.Chrome()  # Initializing Chrome WebDriver
browser.get(START_URL)  # Opening the specified URL in the browser

time.sleep(2)  # Adding a delay to allow the page to fully load

brown_stars_data = []  # List to store extracted planet data

soup = BeautifulSoup(browser.page_source, "html.parser")
table = soup.find_all("table", class_ = "wikitable")

print(len(table))

t_body = table[2].find("tbody")
table_rows = t_body.find_all("tr")
for row in table_rows:
    table_data = row.find_all("td")
    temp = []

    for data in table_data:
        value = data.text.strip()
        temp.append(value)
    
    brown_stars_data.append(temp)

print(brown_stars_data)

#headers = ["constellation", "right_ascension", "declination", "app_mag", "distance", "spectral_type", "mass", "radius", "discovery_year"]

constellation = []
distance = []
for row in brown_stars_data:
    constellation.append(row[0])
    distance.append(row[4])

headers_2 = ["constellation", "distance"]

df2 = pd.DataFrame(list(zip(constellation, distance)), columns=headers_2)

df2.to_csv("brown_stars_csv_file.csv",  index_label = "id")