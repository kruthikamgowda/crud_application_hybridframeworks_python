#Scripts
from utilities.customlogger import LogGen
from utilities.readproperty import ReadConfig
import pytest
from selenium import webdriver
from page_object.homepage import Home

#creating a  class
class Test_001_login:
    baseURL = ReadConfig.getApplicationUrl()
    logger=LogGen.logGen()
    #defining a function to check home page is displayed or not
    def test_home_page_title(self, setup):
        self.logger.info("***************Test_001_login**************")
        self.logger.info("***************Verifying_Homepage_title**************")
        self.driver = setup
        # launch the browser
        self.driver.get(self.baseURL)
        # get the title of the login page.
        actual_home_page_title = self.driver.title

        # compare the title
        if actual_home_page_title == "FLASK-CRUD_APP_home_page.":
            assert True
            # close the browser
            self.logger.info("***************Home page title is matched**************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" +"test_home_page_title.png")
            # close the browser
            self.logger.info("***************Home page title did not matched**************")
            self.driver.close()
            assert False

   # function to perform the click on login and test title of login page.

    def test_login_page_open(self, setup):
        self.logger.info("***************Verifying_Loginpage_title**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # make an object of the Home class.
        self.hp = Home(self.driver)
        # now call the methods from the Home class to perform the clicking on  login link.
        self.hp.clickOnLoginLink()
        # after navigation to the login page. get the title of the login page.
        actual_login_title = self.driver.title

        # compare the title of the page.
        if actual_login_title == "FLASK-CRUD_APP_login_page.":
            assert True
            self.logger.info("***************Login page title is matched**************")
            # close the browser
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login_page_open.png")
            # close the browser
            self.driver.close()
            self.logger.info("***************Login page title matched**************")
            assert False


    def test_Register_page_open(self, setup):
        self.logger.info("***************Verifying_Registerpage_title**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # make an object of the Home class.
        self.hp = Home(self.driver)
        # now call the methods from the Home class to perform the clicking on register link.
        self.hp.clickOnRegisterLink()
        # after navigation to the login page. get the title of the login page.
        actual_register_title = self.driver.title

        # compare the title of the page.
        if actual_register_title == "FLASK-CRUD_APP_register_page.":
            assert True
            self.logger.info("***************Register page title is matched**************")
            # close the browser
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_Register_page_open.png")
            # close the browser
            self.driver.close()
            self.logger.info("***************Login page title matched**************")
            assert False

    def test_Dropdown_page_open(self, setup):
        self.logger.info("***************Verifying_Dropdownpage_title**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # make an object of the Home class.
        self.hp = Home(self.driver)
        # now call the methods from the Home class to perform the clicking on register link.
        self.hp.clickOnDropdownLink()
        # after navigation to the login page. get the title of the login page.
        actual_dropdown_title = self.driver.title

        # compare the title of the page.
        if actual_dropdown_title == "FLASK-CRUD_APP_dropdown_checkbox_page.":
            assert True
            self.logger.info("***************Dropdown page title is matched**************")
            # close the browser
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_Dropdown_page_open.png")
            # close the browser
            self.driver.close()
            self.logger.info("***************Dropdown page title matched**************")
            assert False

    def test_Alert_page_open(self, setup):
        self.logger.info("***************Verifying_Alert_page_title**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # make an object of the Home class.
        self.hp = Home(self.driver)
        # now call the methods from the Home class to perform the clicking on alert link.
        self.hp.clickOnAlertLink()
        # after navigation to the login page. get the title of the login page.
        actual_Alert_title = self.driver.title

        # compare the title of the page.
        if actual_Alert_title == "FLASK-CRUD_APP_alerts_page.":
            assert True
            self.logger.info("***************Alert page title is matched**************")
            # close the browser
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_Alert_page_open.png")
            # close the browser
            self.driver.close()
            self.logger.info("***************Alert page title matched**************")
            assert False