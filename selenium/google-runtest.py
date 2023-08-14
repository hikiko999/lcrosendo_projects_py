from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.google.com" 

driver = webdriver.Chrome()
# driver.implicitly_wait(3.21)

# First Page

driver.get(url)

element = driver.find_element(By.ID, "APjFqb")
element.send_keys("Random Text")
element.send_keys(Keys.RETURN)

# Second Page

url = driver.current_url
driver.get(url)

# element = driver.find_element(By.ID, "APjFqb")
# element.clear()

# wait = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME, "LC20lb.MBeuO.DKV0Md"))
# )
# print(wait)
# print("***")
# print(type(wait))
# print("=========================")
# element = driver.find_elements(By.CLASS_NAME, "LC20lb.MBeuO.DKV0Md")
# print(element)
# print("***")
# print(type(element))

element = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "LC20lb.MBeuO.DKV0Md")) # Space = (.)
)

for i in element:
    print(i.text)

# for i in element:
#     print(i.text)

# driver.find_element(By.CLASS_NAME, "gLFyf")
# element.clear()
# element.send_keys("Second Random")

# search_results = driver.find_elements(By.CLASS_NAME, "LC20lb MBeuO DKV0Md")
# print(search_results)

input()

# text = driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[5]/div[3]/div/div/div/span[1]')
# print(text)