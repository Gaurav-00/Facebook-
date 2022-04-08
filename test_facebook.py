import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setUp():
    global username,driver,password
    username = input("ENter a username to login-:")
    password = input("ENter a password-:")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_login(setUp):
    driver.get("https://www.facebook.com/")
    driver.find_element_by_name("email").send_keys(username)  # to searh a  word in google
    time.sleep(3)

    driver.find_element_by_name("pass").send_keys(password)

    time.sleep(3)

    driver.find_element_by_name("login").click()
    time.sleep(5)  # time is given to hold for 5 sec


