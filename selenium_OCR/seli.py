from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.google.com/maps/place/Sai+Aqua+Products+(AQUA+VALE)/@11.6888281,78.1112543,17z/data=!4m12!1m6!3m5!1s0x3babf081ab367a7b:0x29af954071e6b3b6!2sVee+Technologies!8m2!3d11.688902!4d78.1134617!3m4!1s0x3babf0840b95b3cf:0x7c7edeb11f565b9a!8m2!3d11.6927977!4d78.116826?hl=en")
# pageSource = driver.page_source
# print(pageSource)
# fileToWrite = open("page_source.html", "w")
# fileToWrite.write(pageSource)
# fileToWrite.close()
# fileToRead = open("page_source.html", "r")
# print(fileToRead.read())
# fileToRead.close()
# driver.quit()


class MapScraper:

    location_data = {}

    PATH = "/usr/local/bin/chromedriver"
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(PATH, options=options)
    location_data["name"] = "NA"
    location_data["location"] = "NA"
    location_data["contact"] = "NA"
    location_data["website"] = "NA"

    def get_location_data(driver):
    	try:
    		name = driver.find_element_by_tag_name('h1')
    		address = driver.find_element_by_css_selector('[data-item-id="address"]')
    		phone_number = driver.find_element_by_css_selector('[data-tooltip="Copy phone number"]')
    		website = driver.find_element_by_css_selector('[data-item-id="authority"]')
    	except:
    		pass
    	try:
    		location_data["name"] = name.text
    		location_data["location"] = address.text
    		location_data["contact"] = phone_number.text
    		location_data["website"] = 'www.'+ website.text

    	except:
    		pass

    def scrape(driver, url):
    	try:
    		driver.get(url)
    	except Exception as e:
    		driver.quit()
    		# continue
    	time.sleep(5)

    	get_location_data()
    	driver.quit()
    	location_data
    	return(location_data)

if __name__ == '__main__':
	# url = "https://www.google.com/maps/place/Vee+Technologies/@11.6888281,78.1112543,17z/data=!3m1!4b1!4m5!3m4!1s0x3babf081ab367a7b:0x29af954071e6b3b6!8m2!3d11.688902!4d78.1134617?hl=en"
    result = []
    inputs = open('links.txt', 'r')
    for url in inputs:
        x = MapScraper()
        x.scrape(url)
        result.append(x.scrape(url))
        print("Inside",result)
    inputs.close()
    print("Final",result)
