import time
import datetime
import os #Импорт модуля os для работы с файлами в системе

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless") #Браузер открывается в headless режиме

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys("cook_user")
print('Input login')

user_password = driver.find_element(By.XPATH, '//input[@id="password"]')
user_password.send_keys("spicy_sauce")
print('Input password')

time.sleep(3)
user_name.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
user_name.send_keys(Keys.DELETE)
time.sleep(1)
user_name.send_keys("standard_user")
time.sleep(1)
user_password.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
user_password.send_keys(Keys.DELETE)
time.sleep(1)
user_password.send_keys("secret_sauce")

button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print('Click login button')