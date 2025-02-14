import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome( # webdriver.Chrome — команда, которая запускает Chrome браузер.
    options=options, # options=options — мы передаем настройки (options).
    service=ChromeService(ChromeDriverManager().install())
)

#Ввод переменной с адресом URL страницы, которую нам нужно открыть
base_url = 'https://www.saucedemo.com/'

# Открываем указанную веб-страницу
driver.get(base_url)

# Устанавливаем разрешение окна браузера
driver.set_window_size(1920, 1080)

#Установка времени, при котором браузер остается открытым
time.sleep(10)

#Закрываем браузер
driver.close()


from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#Ввод переменной с адресом URL страницы, которую нам нужно открыть
base_url = 'https://www.saucedemo.com/'

# Открываем указанную веб-страницу
driver.get(base_url)

# Устанавливаем разрешение окна браузера
driver.set_window_size(1920, 1080)

#Установка времени, при котором браузер остается открытым
time.sleep(10)

#Закрываем браузер
driver.close()


from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

edge_options = EdgeOptions()

edge_driver_path = "C:\edgedriver_win64\msedgedriver.exe"

# Создание экземпляра драйвера Internet Explorer
driver = webdriver.Edge(options=edge_options,
                        service=EdgeService(executable_path=edge_driver_path)
                        )

#Ввод переменной с адресом URL страницы, которую нам нужно открыть
base_url = 'https://www.saucedemo.com/'

# Открываем указанную веб-страницу
driver.get(base_url)

# Устанавливаем разрешение окна браузера
driver.set_window_size(1920, 1080)

#Установка времени, при котором браузер остается открытым
time.sleep(10)

#Закрываем браузер
driver.quit()