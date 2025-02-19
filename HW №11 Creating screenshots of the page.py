import time
import datetime
import os #Импорт модуля os для работы с файлами в системе

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless") #Браузер открывается в headless режиме

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys("standard_user")
print('Input login')

user_password = driver.find_element(By.XPATH, '//input[@id="password"]')
user_password.send_keys("secret_sauce")
print('Input password')

button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print('Click login button')

time.sleep(2)

now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
name_screenshot = 'screenshot' + now_date + '.png' #Создание структуры имени файла скриншота

path_screenshots = 'C:\\Users\\songf\\Desktop\\EduIT\\BasicPython\\1\\Basic_Selenium_-1\\screenshots'

if not os.path.exists(path_screenshots): #Условие если папки со скриншотами нету
    os.makedirs(path_screenshots) # Создание папки screenshots

driver.save_screenshot(name_screenshot)