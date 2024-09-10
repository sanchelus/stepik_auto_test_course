import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
my_url = browser.get("https://suninjuly.github.io/execute_script.html")

my_number = browser.find_element(By.ID, "input_value").text
my_number = calc(int(my_number))

answer = browser.find_element(By.ID, "answer")
answer.send_keys(my_number)

check_box = browser.find_element(By.ID, "robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", check_box)
check_box.click()

robotsRule = browser.find_element(By.ID, "robotsRule")
robotsRule.click()
submit_button = browser.find_element(By.XPATH,"/html/body/div/form/button")
submit_button.click()

sleep(6)