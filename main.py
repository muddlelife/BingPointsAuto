from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
import time
import random
from tqdm import tqdm


def init_browser(keyword):
    edge_options = EdgeOptions()
    service = EdgeService(executable_path="./msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=edge_options)
    try:
        driver.get("https://cn.bing.com")
        time.sleep(random.randint(2, 10))
        search_box = driver.find_element(By.NAME, "q")
        time.sleep(random.randint(2, 10))
        search_box.send_keys(keyword)
        search_box.submit()
        time.sleep(random.randint(2, 10))
    except Exception as e:
        print(e)
    return driver



def bing_search(driver, keyword):
    try:
        element = driver.find_element(By.XPATH, '//*[@id="sb_form_q"]')
        element.clear()
        time.sleep(random.randint(2, 4))
        element.send_keys(keyword)
        time.sleep(random.randint(1, 3))
        element.submit()
        time.sleep(random.randint(3, 5))
    except Exception as e:
        print(e)


if __name__ == "__main__":

    with open(r'关键词.txt','r') as file:
        keyword_list = [i.split('\n')[0] for i in file.readlines()]

    keyword  = random.choice(keyword_list)
    edge_driver = init_browser(keyword)

    for i in tqdm(range(1000), desc="bing searches", unit="search"):
        bing_search(edge_driver,random.choice(keyword_list))
        time.sleep(random.randint(3, 5))
