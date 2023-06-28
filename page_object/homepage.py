from selenium import webdriver
from selenium.webdriver.common.by import By

class Home:
    #find the login button
    loginLink_xpath="// a[text() = 'Login']"

    #creating a default constructor to initialize the datamembers
    def __init__(self,driver):
        self.driver=driver

    #defining a function to click on login link
    def clickOnLoginLink(self):
        self.driver.find_element(By.XPATH, self.loginLink_xpath).click()
        #in the above functions we have used self bcz functions are present in a class Home.
        #we can avoid self if the functions are not written in class.

    #find the register button
    register_xpath="//a[@id='registerlink']"
    def clickOnRegisterLink(self):
        self.driver.find_element(By.XPATH,self.register_xpath).click()

    # find the register button
    dropdown_xpath = "// a[text() = 'DropDowns / CheckBox']"
    def clickOnDropdownLink(self):
            self.driver.find_element(By.XPATH, self.dropdown_xpath).click()


    # find the register button
    alert_xpath = "//a[text()='Javascript Alerts']"
    def clickOnAlertLink(self):
        self.driver.find_element(By.XPATH, self.alert_xpath).click()

