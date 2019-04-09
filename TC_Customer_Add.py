import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
       driver.get("http://127.0.0.1:8000/admin")
       assert "Logged In"
       time.sleep(5)
       elem = driver.find_element_by_xpath("html/body//div[2]/table/tbody/tr[1]/td[1]/a").click()
       time.sleep(5)
       elem = driver.find_element_by_id("id_cust_name")
       elem.send_keys("Lillian Wells")
       elem = driver.find_element_by_id("id_organization")
       elem.send_keys("MIS")
       elem = driver.find_element_by_id("id_role")
       elem.send_keys("Professor")
       elem = driver.find_element_by_id("id_email")
       elem.send_keys("lwells@unomaha.edu")
       elem = driver.find_element_by_id("id_bldgroom")
       elem.send_keys("PKI Room 162")
       elem = driver.find_element_by_id("id_address")
       elem.send_keys("185 S 72nd St")
       elem = driver.find_element_by_id("id_account_number")
       elem.send_keys("623")
       elem = driver.find_element_by_id("id_city")
       elem.send_keys("Omaha")
       elem = driver.find_element_by_id("id_state")
       elem.send_keys("NE")
       elem = driver.find_element_by_id("id_zipcode")
       elem.send_keys("68102")
       elem = driver.find_element_by_id("id_phone_number")
       elem.send_keys("555-555-5555")
       time.sleep(5)
       elem.send_keys(Keys.RETURN)
       assert "Posted Customer Entry"
       driver.get("http://127.0.0.1:8000/admin")

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()