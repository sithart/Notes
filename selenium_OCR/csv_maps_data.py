from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

arr = []

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
			# with open('sample.csv', 'a', newline='') as csvfile:
			#     fieldnames = ['name', 'location', 'contact', 'website']
			#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			#
			#     writer.writeheader()
			#     writer.writerow({
			# 	'name': name.text,
			# 	'location': address.text,
			# 	'contact': phone_number.text,
			# 	'website': 'www.'+ website.text})


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
		try:
			self.driver.get(url)
		except Exception as e:
			self.driver.quit()
			# continue
		time.sleep(5)

		self.get_location_data()
		# arr.append(self.location_data)
		self.driver.quit()
		# arr.append(self.location_data)
		return(self.location_data)

if __name__ == '__main__':
	# url = "https://www.google.com/maps/place/Sun+Pharmaceutical+Industries+Limited/@13.0365756,77.5882213,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae1796759068af:0x3dee712ea40aa47b!8m2!3d13.0365749!4d77.5904099?hl=en"
	inputs = open('links.txt', 'r')

	for url in inputs:
		# time.sleep(5)
		x = MapScraper()
		fin = x.scrape(url)
		arr.append(fin)
		# time.sleep(2)
	inputs.close()
	print(arr)
