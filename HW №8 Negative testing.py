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
user_password.send_keys("secret_sau")
print('Input password')

button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print('Click login button')

# print(driver.current_url)
# get_url = driver.current_url
# url = 'https://www.saucedemo.com/inventory.html'
# assert url == get_url, 'Ошибка: URL должен быть корректным'
# print('URL корректен')

warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warning_text = warning_text.text
string_warning_text = 'Epic sadface: Username and password do not match any user in this service'
assert value_warning_text ==  string_warning_text, 'Ошибка: Текст с ошибкой должен быть корректным'
print('Сообщение корректно')

error_button = driver.find_element(By.XPATH, "//button[@class='error-button']")
error_button.click()
print('Click Error Button')

# text_products = driver.find_element(By.XPATH, "//span[@class='title']")
# value_text_products = text_products.text
# assert value_text_products == "Products", 'Ошибка: Страница должна быть корректная'
# print('Заголовок корректен')