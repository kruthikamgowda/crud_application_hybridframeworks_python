import time

from page_object.Login import Login
from page_object.Register import Register
from utilities import Excelutils
from utilities.customlogger import LogGen
from utilities.readproperty import ReadConfig


class Test_004_DDT_Valid_Login:
    baseURL = ReadConfig.getApplicationUrl()
    #PATH OF TH E EXCEL SHEET
    path=".//testdata/LoginData.xlsx"

    #call the logger() to create the register logs
    logger=LogGen.logGen()

    def test_login_ddt(self,setup):
         #always mention testcase name or id or the class number
         self.logger.info("\n*************** Test_004_DDT_Valid_Login***************\n")
         self.logger.info("*******************Verifying both valid and invalid login deatils******")
         self.driver=setup
         self.driver.get("http://127.0.0.1:5000/login")
         #reference variable of Login POM class
         self.lp=Login(self.driver)#to intialize the members of pom class

         #fetch the data from the excel sheet
         self.rows=Excelutils.getRowCount(self.path,"Sheet1")

         result_list=[] #empty list
         for row in range(2,self.rows+1):
             self.username=Excelutils.readdata(self.path,"Sheet1",row,1)
             self.passowrd=Excelutils.readdata(self.path,"Sheet1",row,2)
             #now we need to read the expected result from the excel sheet to compare the result
             self.expected_result=Excelutils.readdata(self.path,"Sheet1",row,3)
             self.lp.clickOnUsernameofLogin(self.username)
             time.sleep(3)
             self.lp.clickOnPasswordofLogin(self.passowrd)
             time.sleep(3)
             self.lp.clickOnSigninButton()
             time.sleep(3)

             #now after login it will navigate to dashboard page we need to verify the tille of dashboardpage
             actual_title=self.driver.title
             expected_title="FLASK-CRUD_APP_Dashboard_page."
             if actual_title==expected_title:
                 if self.expected_result=="pass":
                     self.logger.info("***************Login Test is passsed")
                     result_list.append("pass")
                     #now come back to login page  y clicking on Register link
                     time.sleep(1)
                     self.driver.back()
                     time.sleep(0.5)


                 elif self.expected_result=="fail":
                     self.logger.error("**************Invalid login is passed********")

                     result_list.append("fail")
                     #you will be in dashboardpage
                     if(self.driver.title==expected_title):
                         self.driver.back()

             elif actual_title!=expected_title:
                  if self.expected_result=="fail":
                     self.logger.error("**********valid login has failed******")
                     result_list.append("fail")

         if "fail" not in result_list:
             self.logger.info("***********Valid login test  DDT test Passed ************")
             #self.logger.info("\n**********Test_003_DDT_Register**************\n")
             self.driver.close()
             assert True

         else:
             self.logger.info()