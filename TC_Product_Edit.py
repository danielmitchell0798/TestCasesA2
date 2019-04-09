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
       elem = driver.find_element_by_xpath("html/body/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a").click()
       time.sleep(5)
       elem = driver.find_element_by_xpath("html/body/div/div/div/div[3]/table/tbody/tr[3]/td[7]/a").click()
       time.sleep(5)
       elem = Select(driver.find_element_by_id('id_cust_name'))
       elem.select_by_visible_text('Lillian Wells')
       elem = driver.find_element_by_id("id_product")
       elem.clear()
       elem.send_keys("Cupcakes")
       elem = driver.find_element_by_id("id_p_description")
       elem.clear()
       elem.send_keys("Red Velvet")
       elem = driver.find_element_by_id("id_quantity")
       elem.clear()
       elem.send_keys("60")
       elem = driver.find_element_by_id("id_charge")
       elem.clear()
       elem.send_keys("42.58")
       time.sleep(5)
       elem.send_keys(Keys.RETURN)
       assert "Posted Product Entry"
       driver.get("http://127.0.0.1:8000/product_list")

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()