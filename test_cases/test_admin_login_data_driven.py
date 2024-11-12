import time

import pytest
from selenium import webdriver
#from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils

from base_pages.Login_Admin_Page import Login_Admin_Page
from selenium.webdriver.chrome.options import Options


class Test_02_Admin_Login_data_driven:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = "/Users/admin/PycharmProjects/nopcommerce/test_data/admin_login_data.xlsx"
    status_list = []

    def test_valid_admin_login(self,setup):
        self.logger.info("**********test_valid_admin_login_data_driven**********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.login = Login_Admin_Page(self.driver)
        self.rows = excel_utils.get_row_count(self.path,"Sheet1")
        for r in range(2,self.rows+1):
            self.username = excel_utils.read_data(self.path,"Sheet1",r,1)
            self.password = excel_utils.read_data(self.path, "Sheet1", r,2 )
            self.exp_login = excel_utils.read_data(self.path, "Sheet1", r, 3)
            self.login.enter_username(self.username)
            self.login.enter_password(self.password)
            self.login.click_login()
            time.sleep(4)
            act_title = self.driver.title
            exp_title = "Dashboard"

            if act_title == exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("Test data is passed ")
                    self.status_list.append("Pass")
                    self.login.click_logout()
                elif self.exp_login == "No":
                    self.logger.info("Test data is failed")
                    self.status_list.append("Fail")
                    self.login.click_logout()
            elif act_title != exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("Test data is failed")
                    self.status_list.append("Fail")
                elif self.exp_login == "No":
                    self.logger.info("Test data is passed ")
                    self.status_list.append("Pass")
        print("status list is ",self.status_list)
        if "Fail" in self.status_list:
            self.logger.info("Test admin data driven is failed")
        else:
            self.logger.info("testcase is passed")

















