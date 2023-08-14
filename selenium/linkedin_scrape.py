from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.linkedin.com/in/leifchristianrosendo/"
driver = webdriver.Chrome()
driver.get(url)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="ember110"]/div[3]/div/div/div/span[1]'))
)

print(element.text)
input()
# element = driver.find_element(By.XPATH, "//*[@id="ember110"]/div[3]/div/div/div/span[1]")
