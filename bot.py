#A python bot using Selenium, which enter OpenSea and automatically Refresh metadatas of NFTs.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

option = webdriver.ChromeOptions()
browser  = webdriver.Chrome(ChromeDriverManager().install())
id = 1
for i in range(201):
    browser.get('https://opensea.io/assets/ethereum/0x959e0667313051f573927c0ca8ae091b077da6a0/' + str(id))
    time.sleep(2)
    browser.find_element_by_xpath("/html//main[@id='main']/div/div/div[@class='item--container']//section[@class='item--header']//div[@class='item--collection-toolbar-wrapper']/div/button[1]").click()
    time.sleep(1)
    id = id+1

