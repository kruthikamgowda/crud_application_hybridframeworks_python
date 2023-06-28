from selenium import webdriver
from selenium.webdriver.common.by import By

class Dashboard:

    # creating a default constructor to initialize the datamembers
    def __init__(self, driver):
        self.driver = driver
    #find the addnewemployee
    addemployee_xpath="//a[text()='Add New Employee']"
    def clickaddemployee(self):
        self.driver.find_element(By.XPATH,self.addemployee_xpath).click()

    # find the addnewemployee
    addemployeename_xpath = "//input[@id='name']"
    def clickaddemployeename(self):
            self.driver.find_element(By.XPATH, self.addemployeename_xpath).send_keys("scott")

    # find the email textfield
    add_email_xpath = "//input[@id='email']"
    def clickaddemployeemail(self):
            self.driver.find_element(By.XPATH, self.add_email_xpath).send_keys("scott@gmail.com")


    # find the phone textfield
    add_phone_xpath="//input[@id='phone']"
    def clickOnaddempphone(self):
        self.driver.find_element(By.XPATH, self.add_phone_xpath).send_keys("345672")

    # find the phone textfield

    add_address_xpath = "//input[@id='address']"
    def clickOnaddempaddress(self):
        self.driver.find_element(By.XPATH, self.add_address_xpath).send_keys("banglore")

    add_empafter_xpath = "//button[text()='Add Employee']"

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def clickOnaddempafter(self):
        self.driver.find_element(By.XPATH, self.add_empafter_xpath).click()

