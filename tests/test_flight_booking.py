from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
driver.get("https://blazedemo.com")

wait = WebDriverWait(driver, 10)

depart = wait.until(EC.presence_of_element_located((By.NAME, "fromPort")))
depart.send_keys("Boston")        

dest = wait.until(EC.presence_of_element_located((By.NAME, "toPort")))
dest.send_keys("London")          

time.sleep(1)

find_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']")))
find_btn.click()

choose = wait.until(EC.element_to_be_clickable((By.XPATH, "//table/tbody/tr[1]/td[1]/input")))
choose.click()

driver.find_element(By.ID, "inputName").send_keys("Arpita")
driver.find_element(By.ID, "address").send_keys("PESU")
driver.find_element(By.ID, "city").send_keys("Bangalore")
driver.find_element(By.ID, "state").send_keys("KA")
driver.find_element(By.ID, "zipCode").send_keys("560078")
driver.find_element(By.ID, "creditCardNumber").send_keys("123456789011")
driver.find_element(By.ID, "nameOnCard").send_keys("Arpita Laddha")

time.sleep(1)

purchase_btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
purchase_btn.click()

driver.save_screenshot("final_screenshot.png")

time.sleep(2)
driver.quit()
