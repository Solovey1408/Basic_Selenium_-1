import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


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
user_name.send_keys('standard_user')
print('Input Login')

time.sleep(3)

user_name.send_keys(Keys.CONTROL + 'a')
user_name.send_keys(Keys.BACKSPACE)

password = driver.find_element(By.XPATH, '//input[@id ="password"]')
password.send_keys('secret_sauce')
print('Input Password')

time.sleep(3)

password.send_keys(Keys.CONTROL + 'a')
password.send_keys(Keys.BACKSPACE)

button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print('Click login button')