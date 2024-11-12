import time

import pytest
from selenium import webdriver
#from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

from base_pages.Login_Admin_Page import Login_Admin_Page
from selenium.webdriver.chrome.options import Options


class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()


    def test_title_verification(self,setup):
        self.logger.critical("**********Test_01_Admin_Login**********")
        self.logger.info("**********Verfication of title**********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        actual_title = self.driver.title
        exp_title = "Login"
        if actual_title == exp_title:
            self.logger.info("**********title matched**********")
            assert True
            self.driver.close()
        else:
            self.logger.info("**********title doesn't matched**********")
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):
        self.logger.info("**********test_valid_admin_login**********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.login = Login_Admin_Page(self.driver)
        self.login.enter_username(self.username)
        self.login.enter_password(self.password)
        self.login.click_login()
        act_dashboard_text = self.driver.find_element(By.XPATH,"//div/p").text
        if act_dashboard_text == "Dashboard":
            self.logger.info("**********text matched**********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("/Users/admin/PycharmProjects/nopcommerce/screenshots/test_valid_admin_login.png")
            self.driver.close()
            assert False



    def test_invalid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.login = Login_Admin_Page(self.driver)
        self.login.enter_username(self.invalid_username)
        self.login.enter_password(self.password)
        self.login.click_login()
        time.sleep(5)
        error_msg = self.driver.find_element(By.XPATH,"//div/h4").text
        if error_msg == "Invalid Login":
            self.logger.info("**********popup matches successfully**********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False



# for parllel execution of testcases we use ( pytest- xdist) plugin
# command we use is pytest -s -v ./test_cases/test_admin_login.py -n 3






