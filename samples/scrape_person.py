import os
import sys
import time

start = time.time()

from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\ACER\\Documents\\College\\TA\\Scraper\\samples\\chromedriver")

actions.login(driver, cookie="AQEDAS1A-iAE-1p-AAABiAmoCKkAAAGIcKl8HVYAD4WWluhSKFJT6Ge0tVuNSDRljUBxZstL1BVIYt0R7MJ1D1AzTXHrT5FoVHpE1667qCjy-DyBdG6khk2HByQkvlbrx0HCLXpArJG_dydUT5fjI6xk") 

person = Person("https://www.linkedin.com/in/thomas-ferdinand-martin-b94322192", driver=driver)

print('Person data', person)
end = time.time()

print(f'Execution time: {end - start} seconds')