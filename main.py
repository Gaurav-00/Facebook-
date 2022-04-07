import time

from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started")
driver.maximize_window()
driver.get("https://www.facebook.com/")
#driver.find_element_by_name("login").send_keys("login") #to searh a  word in google
username=input("ENter a username-:")
password=input("ENter a password-:")
driver.find_element_by_name("email").send_keys(username) #to searh a  word in google
time.sleep(3)

driver.find_element_by_name("pass").send_keys(password)

time.sleep(3)

driver.find_element_by_name("login").click()
time.sleep(5)   #time is given to hold for 5 sec

driver.close()
print("testcase successfully completed")



