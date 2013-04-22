#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "http://factual.com/data/t/places"
driver = webdriver.Chrome()
driver.get(url)

elem = driver.find_element_by_id("search-query")
elem.send_keys("beverage store")
#location = driver.find_element_by_id("facet-selector-country")
#location.send_keys("US")
#driver.execute_script("document.getElementById('facet-selector-country').value = 'US';")
#driver.find_element_by_id("facet-selector-country").clear()
#driver.find_element_by_id("facet-selector-country").send_keys("US")
#time.sleep(1)
elem.send_keys(Keys.RETURN)

time.sleep(2)

def output():
  rows = driver.find_elements_by_css_selector(".ui-widget-content.slick-row")
  file = open("beverage_store.csv", "a")
  global count
  for row in rows:
    li = row.text.splitlines()
    s = str(count) + ", "
    if (li[6] == "us"):
      for i in range(1, len(li)):
        s += "\""
        s += li[i].encode('utf-8')
        s += "\""
        if i != len(li) - 1:
          s += ", "
        else:
          s += "\n"
      count += 1
      #print s
      file.write(s)


count = 1
rows = driver.find_elements_by_css_selector(".ui-widget-content.slick-row")
output()

nextPage = driver.find_element_by_link_text("NEXT")
parent = nextPage.find_element_by_xpath("..")
#print parent.text

while (parent.get_attribute("class") != "disabled"):
  nextPage.click()
  time.sleep(2)
  output()
  nextPage = driver.find_element_by_link_text("NEXT")
  parent = nextPage.find_element_by_xpath("..")
