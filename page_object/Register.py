from selenium import webdriver
from selenium.webdriver.common.by import By

class Register:
    #find the register button
    registerLink_xpath="// a[text() = 'Register']"

    #creating a default constructor to initialize the datamembers
    def __init__(self,driver):
        self.driver=driver

    #defining a function to click on login link
    def clickOnRegisterLink(self):
        self.driver.find_element(By.XPATH, self.registerLink_xpath).click()
        #in the above functions we have used self bcz functions are present in a class Home.
        #we can avoid self if the functions are not written in class.

    #find the username textfield
    register_username_xpath="//input[@id='exampleInputEmail1']"
    def clickOnUsername(self,username):
        self.driver.find_element(By.XPATH,self.register_username_xpath).send_keys(username)

    # find the password textfield
    register_password_xpath = "//input[@id='exampleInputPassword1']"
    def clickOnPassword(self,password):
            self.driver.find_element(By.XPATH, self.register_password_xpath).send_keys(password)


    # find the register button
    register_button_xpath="//button[text()='Register']"
    def clickOnRegisterButton(self):
        self.driver.find_element(By.XPATH, self.register_button_xpath).click()

