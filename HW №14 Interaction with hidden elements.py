import time

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
user_name.send_keys("standard_user")
print('Input login')

user_password = driver.find_element(By.XPATH, '//input[@id="password"]')
user_password.send_keys("secret_sauce")
print('Input password')

button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print('Click login button')

#Проверяем страницу каталога
get_url = driver.current_url
url = 'https://www.saucedemo.com/inventory.html'
assert url == get_url, 'Ошибка: URL каталога должен быть корректным'
print('URL каталога корректен')

hidden_menu = driver.find_element(By.ID,'react-burger-menu-btn')
hidden_menu.click()

time.sleep(1)

logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
logout_button.click()

#Проверяем страницу авторизации
get_url = driver.current_url
assert base_url == get_url, 'Ошибка: URL страницы авторизации должен быть корректным'
print('URL страницы авторизации корректен')