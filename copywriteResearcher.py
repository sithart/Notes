'''
Class to scrap the daily horoscope details for each sign and write the
response in text files. The horoscope is scraped from five various websites
'''

import urllib

from bs4 import BeautifulSoup


class horoscope:

    '''
    Function which scrap the text from various websites.
    '''
    def scrap(self):
        signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

        for sign in signs:
            sign = sign.lower()
            url1 = "https://www.google.com/search?q=" + sign
            url2 = "https://www.google.com/search?q=" + sign
            url3 = "https://www.google.com/search?q=" + sign
            url4 = "https://www.google.com/search?q=" + sign

            urllist = [url1,url2,url3,url4]
            article = ""

            for url in urllist:
                htmltext = urllib.urlopen(url)
                soup = BeautifulSoup(htmltext)
                print(soup)
        	# 	if url == url1:
        	# 		for p in soup.findAll("p",attrs = {"class":"horoscope"}):
        	# 			if p.string is not None:
        	# 				article += str(p.string)
            #
        	# 	elif url == url2:
        	# 		article += str(soup.find("div",attrs = {"class":"body bodySign"}).text).replace("&#x2019;","'")
            #
        	# 	elif url == url3:
        	# 		article += soup.find("div",attrs={"class":"horoscope-copy"}).p.string
            #
        	# 	elif url == url4:
        	# 		article += soup.find("div",attrs={"class":"astro-tab-body"}).text
            #
        	# f = open("daily_horoscope/" + sign + ".txt",'w')
        	# f.write(article)


if __name__ == "__main__":
    o = horoscope()
    o.scrap()
