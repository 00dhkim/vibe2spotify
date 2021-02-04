# -*- encoding: utf-8 -*-
"""
vibe_crawl.py

vibe에서 크롤링 해서, 메인 모듈로 리턴함

"""

import time
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class VibeCrawler:
    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.crawl_data = []

    def crawl(self):
        self.driver.get("https://vibe.naver.com/")
        input("self login and press ENTER")  # self login
        self.driver.get("https://vibe.naver.com/library/tracks")
        time.sleep(5)  # page loading

        # 더 보기 button click
        while True:
            try:
                self.driver.find_element_by_css_selector('body').send_keys(Keys.END)
                button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[2]/a')
                button.click()
                print("button clicked")
                time.sleep(1)

            except selenium.common.exceptions.ElementClickInterceptedException:
                print("ElementClickInterceptedException")
                time.sleep(5)

            except selenium.common.exceptions.NoSuchElementException:
                print("NoSuchElementException")
                break

        print("button click finished")

        # crawl and append
        trs = self.driver.find_elements_by_xpath('//*[@id="content"]/div/div[4]/div[1]/div/table/tbody/tr')
        for i in range(len(trs)):
            tr = trs[i]
            song = tr.find_element_by_xpath('td[3]').text
            artist = tr.find_element_by_xpath('td[4]').text
            music = {'song': song, 'artist': artist}
            self.crawl_data.append(music)
            print(f'crawling...{i}/{len(trs)}')

        print("crawling complete")

        # store crawl_data in txt file
        with open('vibe_crawl_data.txt', 'w', encoding='utf-8') as f:
            f.write(self.crawl_data.__str__())
            # TODO "\n청소년 청취 불가" 라는 문구가 곡명에 붙어서 나옴.

        return self.crawl_data


if __name__ == '__main__':
    vibe_crawler = VibeCrawler()
    vibe_crawler.crawl()

    # testing crawled file (with eval)
    with open('vibe_crawl_data.txt', 'r', encoding="utf-8") as f:
        filedata = f.read()
        print(type(eval(filedata)))
