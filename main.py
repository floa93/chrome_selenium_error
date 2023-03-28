from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.accept_insecure_certs = True
chrome_options.add_argument('--headless')
chrome_options.add_argument('--allow-insecure-localhost')

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   options=chrome_options,
)

try:
    driver.get("http://10.65.194.148:8082")
    for x in range(999999999):
        print(x)

        assert "Index" in driver.title
        elem = driver.find_element(By.ID, "open")
        elem.click()
        time.sleep(0.1)
        driver.switch_to.window(driver.window_handles[-1])

        assert "Popup" in driver.title
        time.sleep(0.1)
        elem = driver.find_element(By.ID, "close")
        elem.click()
        driver.switch_to.window(driver.window_handles[-1])

        assert "Second" in driver.title
        elem = driver.find_element(By.ID, "back")
        elem.click()
        time.sleep(0.1)

        assert "Index" in driver.title

    print('Finish')
    driver.quit()
except Exception as e:
    driver.quit()
    print(e.msg)
