__author__ = 'BackOffice-3'


import csv
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



driver = webdriver.Firefox()
base_url = 'https://www.bomberg.ch/accounts/'

with open('import-data.csv') as csv_file:
   readCSV = csv.reader(csv_file, delimiter=',')
   u = []
   p = []
   for row in readCSV:
       username = row[0]
       password = row[1]
       u.append(username)
       p.append(password)

for i in range(0, len(u)):
   driver.get(base_url)
   element3 = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "reg_email")))
   element = driver.find_element(By.ID, "reg_email")
   print (u[i])
   element.send_keys(u[i])
   element1 = driver.find_element_by_id("reg_password")
   element1.send_keys(p[i])
   print (p[i])
   driver.find_element_by_name("register").click()

   try:
       driver.find_element_by_xpath("//div[@id='content']/div/div[1]/ul/li").text
   except NoSuchElementException:
       logged_in = driver.find_element_by_xpath("//article[@id='post-8']/div/div/div/p[1]/strong").text
       driver.find_element_by_xpath("//div[@id='main-navbar']/div[1]/ul[2]/li[11]/ul/li/a").click()
i =i + 1

driver.quit()


