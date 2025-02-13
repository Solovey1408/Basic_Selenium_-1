from selenium import webdriver # Импортируем инструмент webdriver внутри Selenium для запуска и управления браузером
from selenium.webdriver.chrome.service import Service as ChromeService  # Импортируем еще один инструмент
# Service внутри Selenium для настройки бразуера, даем ему имя ChromeService
from webdriver_manager.chrome import ChromeDriverManager # Импортируем инструмент webdriver_manager.chrome
# который, автоматически загружает правильную версию программы ChromeDriver для вашего компьютера.
# ChromeDriver нужен, чтобы Selenium мог "говорить" с браузером Chrome.

#Здесь мы создаем объект options, который будет содержать настройки для нашего браузера Chrome.
options = webdriver.ChromeOptions()
# ChromeOptions — это специальный класс, который позволяет нам задать правила для работы браузера
# (например, сделать его полным экраном или оставить открытым после выполнения скрипта).

#Эта строка добавляет особую настройку, чтобы браузер не закрывался автоматически после завершения работы программы.
# "detach" — это название настройки. True — значение, которое говорит: "Да, оставь браузер открытым".
options.add_experimental_option("detach", True)

# Здесь мы создаем переменную driver
driver = webdriver.Chrome( # webdriver.Chrome — команда, которая запускает Chrome браузер.
    options=options, # options=options — мы передаем настройки (options).
    service=ChromeService(ChromeDriverManager().install())
)
# service=ChromeService(ChromeDriverManager().install()) — здесь мы говорим Selenium, как подключиться к ChromeDriver.
# ChromeDriverManager().install() — эта часть автоматически скачивает правильную версию ChromeDriver для вашего компьютера.
# ChromeService(...) — это служба, которая настраивает работу ChromeDriver.
# Базовый URL для тестирования
base_url = 'https://www.saucedemo.com/'

# Открываем указанную веб-страницу
driver.get(base_url)

# Устанавливаем разрешение окна браузера
driver.set_window_size(1920, 1080)