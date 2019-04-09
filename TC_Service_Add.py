import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class MFS_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://127.0.0.1:8000/home")
       assert "Logged In"
       time.sleep(5)
       elem = driver.find_element_by_xpath("html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
       time.sleep(5)
       elem = driver.find_element_by_xpath("html/body/div/div/div/div[3]/div/a/span").click()
       time.sleep(5)
       elem = Select(driver.find_element_by_id('id_cust_name'))
       elem.select_by_visible_text('Lillian Wells')
       elem = driver.find_element_by_id("id_service_category")
       elem.send_keys("Taffy")
       elem = driver.find_element_by_id("id_description")
       elem.send_keys("We need some taffy for children at an event we are hosting.")
       elem = driver.find_element_by_id("id_location")
       elem.send_keys("1500 Alfred Circle")
       elem = driver.find_element_by_id("id_service_charge")
       elem.send_keys("47.36")
       time.sleep(5)
       elem.send_keys(Keys.RETURN)
       assert "Posted Service Entry"
       driver.get("http://127.0.0.1:8000/service_list")

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()