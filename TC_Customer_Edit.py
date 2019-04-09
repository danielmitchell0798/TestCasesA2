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
       driver.get("http://127.0.0.1:8000/home")
       assert "Logged In"
       time.sleep(5)
       elem = driver.find_element_by_xpath("html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
       time.sleep(5)
       elem = driver.find_element_by_xpath("html/body/div/div/div/div[3]/table/tbody/tr[2]/td[12]/a").click()
       time.sleep(5)
       elem = driver.find_element_by_id("id_cust_name")
       elem.clear()
       elem.send_keys("Lillian Wells")
       elem = driver.find_element_by_id("id_organization")
       elem.clear()
       elem.send_keys("MIS")
       elem = driver.find_element_by_id("id_role")
       elem.clear()
       elem.send_keys("Professor")
       elem = driver.find_element_by_id("id_email")
       elem.clear()
       elem.send_keys("lwells@unomaha.edu")
       elem = driver.find_element_by_id("id_bldgroom")
       elem.clear()
       elem.send_keys("PKI Room 185")
       elem = driver.find_element_by_id("id_address")
       elem.clear()
       elem.send_keys("186 S 72nd St")
       elem = driver.find_element_by_id("id_account_number")
       elem.clear()
       elem.send_keys("393")
       elem = driver.find_element_by_id("id_city")
       elem.clear()
       elem.send_keys("Omaha")
       elem = driver.find_element_by_id("id_state")
       elem.clear()
       elem.send_keys("NE")
       elem = driver.find_element_by_id("id_zipcode")
       elem.clear()
       elem.send_keys("68102")
       elem = driver.find_element_by_id("id_phone_number")
       elem.clear()
       elem.send_keys("758-514-6325")
       time.sleep(5)
       elem.send_keys(Keys.RETURN)
       assert "Posted Edited Customer Entry"
       driver.get("http://127.0.0.1:8000/customer_list")

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()