import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

my_url = webdriver.Chrome()
click_n_input = my_url.get("https://suninjuly.github.io/selects1.html")

num1 = my_url.find_element(By.ID, 'num1').text
num2 = my_url.find_element(By.ID, 'num2').text
my_sum = str(int(num1) + int(num2))
print(my_sum)

select = Select(my_url.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(my_sum))

daite_clicknut = my_url.find_element(By.XPATH, "/html/body/div/form/button")
daite_clicknut.click()
sleep(7)
