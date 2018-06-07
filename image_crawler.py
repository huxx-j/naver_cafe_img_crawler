import os
import urllib.request

from bs4 import BeautifulSoup
from selenium import webdriver


def naver_cafe_img_crawler(url):
    wd = webdriver.Chrome("./webdriver/chromedriver.exe")
    wd.get(url)
    wd.switch_to.frame("cafe_main")
    html = wd.page_source
    soup = BeautifulSoup(html, "html.parser")
    img_tag = soup.find("div", {"id": "tbody"})
    img_tags = img_tag.find_all("img")
    title_tag = soup.find("div", {"id": "main-area"})
    title = title_tag.find("span", {"class": "b m-tcol-c"}).string
    date = title_tag.find("td", {"class": "m-tcol-c date"}).string.split(" ")
    date = date[0].replace(".", "")
    save_path = os.getcwd()

    for i, img_src in enumerate(img_tags):
        src = img_src.get("src")
        if os.path.exists("{0}/{1}".format(save_path, date)):
            urllib.request.urlretrieve(src, "{0}/{1}/{2}_{3}.jpg".format(save_path, date, title, i+1))
        else:
            os.makedirs("{0}/{1}".format(save_path, date))
            urllib.request.urlretrieve(src, "{0}/{1}/{2}_{3}.jpg".format(save_path, date, title, i+1))


url = "http://cafe.naver.com/temadica/711258"

naver_cafe_img_crawler(url)
