from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Browser:
    driver: WebDriver = webdriver.Chrome()
    driver.maximize_window()
