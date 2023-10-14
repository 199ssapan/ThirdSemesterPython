from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)
driver.get("https://www.pitomec.ru/")
time.sleep(1)
loginto = driver.find_element(By.XPATH, "//*[@id=\"header\"]/div[3]/table/tbody/tr[1]/td/a")
loginto.click()
time.sleep(1)
email = driver.find_element(By.XPATH, "//*[@id=\"loginForm\"]/small/input[1]")
email.send_keys("0f_f0")
time.sleep(1)
password = driver.find_element(By.XPATH, "//*[@id=\"loginForm\"]/small/input[2]")
password.send_keys("kliker")
time.sleep(1)
login_button = driver.find_element(By.XPATH, "//*[@id=\"loginForm\"]/small/input[3]")
login_button.click()
driver.get("https://www.pitomec.ru/forum")

all_tables = driver.find_elements(By.TAG_NAME, "table")

print(all_tables[2].text)
time.sleep(1)
driver.close()