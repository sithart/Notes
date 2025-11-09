from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

class MapScraper:

	location_data = {}

	def __init__(self):
		self.PATH = "/usr/local/bin/chromedriver"
		self.options = Options()
		# self.options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
		self.options.add_argument("--headless")
		self.driver = webdriver.Chrome(self.PATH, options=self.options)
		self.location_data["name"] = "NA"
		self.location_data["location"] = "NA"
		self.location_data["contact"] = "NA"
		self.location_data["website"] = "NA"


	def get_location_data(self):

		try:
			name = self.driver.find_element_by_tag_name('h1')
			address = self.driver.find_element_by_css_selector('[data-item-id="address"]')
			phone_number = self.driver.find_element_by_css_selector('[data-tooltip="Copy phone number"]')
			website = self.driver.find_element_by_css_selector('[data-item-id="authority"]')
		except:
			pass
		try:

			self.location_data["name"] = name.text
			self.location_data["location"] = address.text
			self.location_data["contact"] = phone_number.text
			self.location_data["website"] = 'www.'+ website.text

		except:
			pass


	def scrape(self, url):
		# print('url',url)
		try:
			self.driver.get(url)
		except Exception as e:
			self.driver.quit()
			# continue
		time.sleep(5)

		self.get_location_data()
		self.driver.quit()
		return(self.location_data)

if __name__ == '__main__':
	# url = "https://www.google.com/maps/place/Vee+Technologies/@11.6888281,78.1112543,17z/data=!3m1!4b1!4m5!3m4!1s0x3babf081ab367a7b:0x29af954071e6b3b6!8m2!3d11.688902!4d78.1134617?hl=en"
	inputs = open('links.txt', 'r')
	for url in inputs:
		x = MapScraper()
		x.scrape(url)
		print(x.scrape(url))
	inputs.close()
