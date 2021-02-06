"""
artists_search.py

가수명만으로 검색했을 때 검색이 얼만큼 되는가?

"""

import time
from selenium import webdriver
import selenium.common.exceptions

with open('vibe_crawl_data.txt', 'r', encoding="utf-8") as f:
    filedata = f.read()

data = eval(filedata)
artists = []

for x in data:
    artists.append(x['artist'])

artists = set(artists)

success = 0
fail = 0
error = 0

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://open.spotify.com/search/")

for x in artists:
    try:
        driver.get("https://open.spotify.com/search/"+x)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="searchPage"]/div/div/h1')
        print('[-]',end='|') # 미발견
        fail += 1
        
    except selenium.common.exceptions.NoSuchElementException:
        print('[+]',end='|') # 발견
        success += 1
        
    except:
        print('[!]',end='|') # 예상치 못한 오류
        error += 1
    
    finally:
        print(x)

print("\n\n==============================")
print("success",success)
print("fail",fail)
print("error",error)

