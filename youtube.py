# from selenium import webdriver
# import time
# import random

# async def view_video(view_times, link, watch_time):
#     try:        
#         driver = webdriver.Chrome("./chromedriver.exe")
#         driver.maximize_window()
#         for i in range(view_times):
#             driver.get(link)
#             sleep_time = random.randint(50, 120 + watch_time)
#             time.sleep(sleep_time)
#             driver.quit()
#     except: pass
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

executor = ThreadPoolExecutor(10)


def scrape(url, *, loop, sleep_time):
    loop.run_in_executor(executor, scraper, url, sleep_time)


def scraper(url, sleep_time):
    try:
        driver = webdriver.Chrome("./chromedriver.exe")
        driver.get(url)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[33]/div[2]/div[1]/button")))
        element.click()
        sleep(sleep_time)
    finally:    
        driver.quit()

def view_video(url, sleep_time): 
    loop = asyncio.get_event_loop()
    scrape(url, loop=loop, sleep_time=sleep_time)

    loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))

if __name__ == '__main__':
    view_video('https://www.youtube.com/watch?v=KjgluLOMa0k', 3000)


 