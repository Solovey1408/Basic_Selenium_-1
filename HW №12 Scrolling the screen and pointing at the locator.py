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
user_name.send_keys("standard_user")
print('Input login')

user_password = driver.find_element(By.XPATH, '//input[@id="password"]')
user_password.send_keys("secret_sauce")
print('Input password')

button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print('Click login button')

#Добавляем товары в корзину
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()


actions = ActionChains(driver)
element = driver.find_element(By.ID,'item_3_title_link')
actions.move_to_element(element).perform() #Cкролл до последнего элемента в корзине