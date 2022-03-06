import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from resources.credentials import Constantinope as cndemo
from selenium.webdriver.chrome.options import Options
from resources.locators import common_locators as cl
import time

def setup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome( options=options) #ChromeDriverManager().install(),
    driver.maximize_window()
    driver.get(cndemo.dhakatribune)

    wait = WebDriverWait(driver, 10)
    var = driver.title

    latest_news =  wait.until(EC.presence_of_all_elements_located((By.XPATH, cl.latest_news_body_xpath)))
    scrolltohighest = wait.until(EC.presence_of_element_located((By.XPATH, cl.scroll_to_highest_read)))
    driver.execute_script("arguments[0].scrollIntoView()", scrolltohighest)
    news =  wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, cl.highest_read)))
    highest_news_sliced = news[1:6:]
    highest_news_share_sliced =  news[6::]

    all_news = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, cl.all_news_class)))
    all_news_sliced = all_news[12:79:]

    with open('Latest News.txt', 'w', encoding="utf-8") as f:
        f.write(var)
        f.write("NEWS LATEST 2022 \n")
        for i in  latest_news:
            f.write(i.text + "\n")
    
    with open('Updated Highest Read News.txt', 'w', encoding="utf-8") as f:  
        f.write("UPDATED HIGHEST READ NEWS 2022 \n")
        for i in  highest_news_sliced:
            f.write("\n")
            f.write(i.text)
    
    with open('Updated Highest Share News.txt', 'w', encoding="utf-8") as f:
        f.write("UPDATED HIGHEST SHARED NEWS 2022 \n")
        for i in  highest_news_share_sliced:
            f.write("\n")
            f.write(i.text)

    with open('Updated All News.txt', 'w', encoding="utf-8") as f:
        f.write("UPDATED ALL NEWS 2022 \n")
        for i in  all_news_sliced:
            f.write("\n")
            f.write(i.text)

    return driver


def teardown():
    driver.close()
    driver.quit()
    return teardown

setup()
teardown()
