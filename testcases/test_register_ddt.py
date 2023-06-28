import time

from page_object.Register import Register
from utilities import Excelutils
from utilities.customlogger import LogGen
from utilities.readproperty import ReadConfig


class Test_003_DDT_Register:
    baseURL = ReadConfig.getApplicationUrl()
    #PATH OF TH E EXCEL SHEET
    path=".//testdata/RegistrationData.xlsx"

    #call the logger() to create the register logs
    logger=LogGen.logGen()

    def test_register_ddt(self,setup):
         #always mention testcase name or id or the class number
         self.logger.info("\n*************** Test_003_DDT_Register***************\n")
         self.logger.info("*******************Verifying Registeration process******")
         self.driver=setup
         self.driver.get("http://127.0.0.1:5000/register")
         #reference variable of Register POM class
         self.rp=Register(self.driver)#to intialize the members of pom class

         #fetch the data from the excel sheet
         self.rows=Excelutils.getRowCount(self.path,"Sheet1")

         result_list=[] #empty list
         for row in range(2,self.rows+1):
             self.username=Excelutils.readdata(self.path,"Sheet1",row,1)
             self.passowrd=Excelutils.readdata(self.path,"Sheet1",row,2)
             #now we need to read the expected result from the excel sheet to compare the result
             self.expected_result=Excelutils.readdata(self.path,"Sheet1",row,3)
             self.rp.clickOnUsername(self.username)
             time.sleep(3)
             self.rp.clickOnPassword(self.passowrd)
             time.sleep(3)
             self.rp.clickOnRegisterButton()
             time.sleep(3)

             #now after register it will navigate to login page we need to verify the tille of loginpage
             actual_title=self.driver.title
             expected_title="FLASK-CRUD_APP_login_page."
             if actual_title==expected_title:
                 if self.expected_result=="pass":
                     self.logger.info("***************Register Test is passsed")
                     #now come back to register page  y clicking on Register link
                     self.rp.clickOnRegisterLink()
                     result_list.append("pass")
                 else:
                     self.logger.error("**************Registration Failed********")
                     self.rp.clickOnRegisterLink()
                     result_list.append("fail")

             elif actual_title!=expected_title:

                     self.logger.error("***********failed****************")
                     result_list.append("Fail")


             self.logger.info("***********End of Register DDT Passed ************")
             self.logger.info("\n**********Test_003_DDT_Register**************\n")