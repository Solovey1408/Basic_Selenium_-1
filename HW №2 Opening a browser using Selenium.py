import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions


#Блок Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)
time.sleep(10)
driver.close()


#Блок Firefox
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)
time.sleep(10)
driver.close()


#Блок Microsoft Edge
edge_options = EdgeOptions()
edge_driver_path = "C:\\edgedriver_win64\\msedgedriver.exe"
driver = webdriver.Edge(
    options=edge_options,
    service=EdgeService(executable_path=edge_driver_path)
)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)
time.sleep(10)
driver.quit()