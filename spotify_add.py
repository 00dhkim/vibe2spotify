"""
spotify_add.py

dict를 가진 list 타입의 음악 리스트를 받아서, spotify 웹에서 좋아요에 추가함.

"""

import time
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

with open('vibe_crawl_data.txt', 'r', encoding="utf-8") as f:
    crawl_data = eval(f.read())

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://open.spotify.com/search")
input("self login and press ENTER")

for i in range(len(crawl_data)):
    song = crawl_data[i]['song']
    artist = crawl_data[i]['artist']

    driver.get(f"https://open.spotify.com/search/{song} {artist}")
    try:
        button = driver.get(
            '//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/button[1]')
        button.click()
        print(f"[+] {i:04}/{len(crawl_data):04} 음악 라이브러리에 추가 완료 {song} | {artist}")
    except selenium.common.exceptions.NoSuchElementException:
        print(f"[-] {i:04}/{len(crawl_data):04} spotify 검색 결과 없음: {song} | {artist}")
    except:
        print(f"[!] {i:04}/{len(crawl_data):04} 미확인 exception 발생")

