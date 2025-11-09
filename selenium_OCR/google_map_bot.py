import os
import sys
import requests
from bs4 import BeautifulSoup


def address(soup):
    data = soup.find('meta',attrs={"property":"og:title"})
    if soup.find('meta',attrs={"property":"og:title"}):
        addre = data["content"]
        # return addre
    else:
        return "Address Not Found"


if __name__ == '__main__':
    url = "https://www.google.com/maps/place/Sai+Aqua+Products+(AQUA+VALE)/@11.6888281,78.1112543,17z/data=!4m12!1m6!3m5!1s0x3babf081ab367a7b:0x29af954071e6b3b6!2sVee+Technologies!8m2!3d11.688902!4d78.1134617!3m4!1s0x3babf0840b95b3cf:0x7c7edeb11f565b9a!8m2!3d11.6927977!4d78.116826?hl=en"
    response  = requests.get(url)
    # print(response.status_code)
    soup = BeautifulSoup(response.text, features="html.parser")
    print(soup.find_all("meta"))

    print(address(soup))
