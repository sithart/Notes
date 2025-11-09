#Import neccesary libraries

from selenium import webdriver              # driver to control chrome browser
# import pyautogui
from bs4 import BeautifulSoup          # to parse the html code
import threading                       # to do multi threding
import time
import pandas as pd                   # to store data in csv file


#enter the filename

# print("Enter the filename")            # filename to store data
# filename=str(input())


#intiate the chrome webdriver instance
browser=webdriver.Chrome()           # chrome instance
record=[]
e=[]
def Selenium_extractor():
    print("Enter selenium extractor")
    time.sleep(5)
    source=browser.page_source
                                                      #Beautiful soup for scraping the html source
    soup=BeautifulSoup(source,'html.parser')
    for data in soup.find_all("div",attrs={"class":"AeaXub"}):
        print(data.get_text())

    # n2H0ue-RWgCYc hH0dDd PcZHt-KW5YQd
    # time.sleep(2)
    # a=browser.find_elements_by_class_name("x3AX1-LfntMc-header-title")
    # print(a)
    # time.sleep(1)
    # for i in range(len(a)):
    #     a[i].click()
    #     time.sleep(2)
    #     source=browser.page_source
    #                                                       #Beautiful soup for scraping the html source
    #     soup=BeautifulSoup(source,'html.parser')
    #     for data in soup.find_all("div",attrs={"class":"AeaXub"}):
    #         print(data.get_text())
        # print(soup)
        # f = open("demo_4.txt", "a")
        # f.write(str(soup))
        # f.close()
    #     try:
    #         Name_Html=soup.findAll('div',{"class":"SPZz6b"})
    #
    #         name=Name_Html[0].text
    #         if name not in e:
    #             e.append(name)
    #             print(name)
    #             Phone_Html=soup.findAll('span',{"class":"LrzXr zdqRlf kno-fv"})
    #             phone=Phone_Html[0].text
    #             print(phone)
    #
    #             Address_Html=soup.findAll('span',{"class":"LrzXr"})
    #
    #             address=Address_Html[0].text
    #             #print(address)
    #             try:
    #                 Website_Html=soup.findAll('div',{"class":"QqG1Sd"})
    #                 web=Website_Html[0].findAll('a')
    #
    #                 website=web[0].get('href')
    #             except:
    #                 website="Not available"
    #             #print(website)
    #             record.append((name,phone,address,website))
    #             df=pd.DataFrame(record,columns=['Name','Phone number','Address','Website'])  # writing data to the file
    #             df.to_csv(filename + '.csv',index=False,encoding='utf-8')
    #
    #     except:
    #         print("error")
    #         continue
    #
    #
    #
    # try:
    #     time.sleep(1)
    #     next_button=browser.find_element_by_id("pnnext")                  # clicking the next button
    #     next_button.click()
    #     browser.implicitly_wait(2)
    #     time.sleep(2)
    #     Selenium_extractor()
    # except:
    #     print("ERROR occured at clicking net button")


# print("Enter the link of the page")
# link=input()
link = "https://www.google.com/maps/place/Ganesh+Medicals/@12.9245534,77.5985686,17z/data=!4m12!1m6!3m5!1s0x3bae6a6c7ca7d509:0xf86f19cde67a21b3!2sIBM+India!8m2!3d12.924306!4d77.600745!3m4!1s0x3bae1500b648549f:0xaea6f28b62ed26e!8m2!3d12.9210636!4d77.6025601?hl=en"
browser.get(str(link))
# time.sleep(10)                                             # pausing the program for 10 secs
Selenium_extractor()
