import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class WaitTest(unittest.TestCase):
    
    def setUp(self):
        self.url = "https://google.com"
        self.driver = webdriver.Chrome()

    def test_wait(self):
        url = self.url
        driver = self.driver
        for i in range(5,0,-1):
            driver.implicitly_wait(i)
            driver.get(url)
            element = driver.find_element(By.ID, "APjFqb")
            print(f"Wait Time: {i} :: Sucessful")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
