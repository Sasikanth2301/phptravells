from selenium.webdriver.common.by import By


class Login_Admin_Page:

    textbox_username_id = "email"
    textbox_password_id = "password"
    button_login_xpath = "//button[@id='submit']"
    button_logout_xpath = "//a[@id='dropdownUser1']"
    Logout_link_text = "Logout"


    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.button_logout_xpath).click()
        self.driver.find_element(By.LINK_TEXT,self.Logout_link_text).click()



