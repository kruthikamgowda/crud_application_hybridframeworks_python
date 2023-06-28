#Scripts
from page_object.Register import Register
from page_object.Login import Login
from utilities.customlogger import LogGen
from utilities.readproperty import ReadConfig
from page_object.Dashboard import Dashboard
import pytest
from selenium import webdriver
from page_object.homepage import Home

#creating a  class
class Test_002_Register:
    baseURL = ReadConfig.getApplicationUrl()
    user = ReadConfig.getApplicationusername()
    pwd = ReadConfig.getApplicationpassword()
    logger=LogGen.logGen()
    #defining a function to check home page is displayed or not
    def test_home_page_title(self, setup):
        self.logger.info("***************Test_002_Register**************")
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

        else:
            self.driver.save_screenshot(".\\screenshots\\" +"test_home_page_title.png")
            # close the browser
            self.logger.info("***************Home page title did not matched**************")

            assert False
        self.hp=Register(self.driver)
        self.hp.clickOnRegisterLink()
        self.hp.clickOnUsername(self.user)
        self.hp.clickOnPassword(self.pwd)
        self.hp.clickOnRegisterButton()
        actual_login_page_title = self.driver.title
        if actual_login_page_title == "FLASK-CRUD_APP_login_page.":
            assert True
            # close the browser
            self.logger.info("***************Login page title is matched**************")
            #self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_home_page_title.png")
            # close the browser
            self.logger.info("***************Login page title did not matched**************")
            #self.driver.close()
            assert False

        # self.rp.clickOnRegisterButton()

        self.hp1=Login(self.driver)
        self.hp1.clickOnUsernameofLogin(self.user)
        self.hp1.clickOnPasswordofLogin(self.pwd)
        self.hp1.clickOnSigninButton()
        actual_dashboard_page_title = self.driver.title
        if actual_dashboard_page_title == "FLASK-CRUD_APP_Dashboard_page.":
            assert True
            # close the browser
            self.logger.info("***************Dashboard page title is matched**************")
            #self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_home_page_title.png")
            # close the browser
            self.logger.info("***************Login page title did not matched**************")
            #self.driver.close()
            assert False
        actual_dashboard_page_title = self.driver.title
        self.hp2=Dashboard(self.driver)
        self.hp2.clickaddemployee()
        self.hp2.clickaddemployeename()
        self.hp2.scroll()
        self.hp2.clickaddemployeemail()
        self.hp2.clickOnaddempphone()
        self.hp2.clickOnaddempaddress()
        self.hp2.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.hp2.clickOnaddempafter()

        if actual_dashboard_page_title == "FLASK-CRUD_APP_Dashboard_page.":
            assert True
            # close the browser
            self.logger.info("***************Dashboard page title is matched**************")
            #self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_home_page_title.png")
            # close the browser
            self.logger.info("***************Login page title did not matched**************")
            #self.driver.close()
            assert False

