import configparser
config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
        #there is no need of self because we are used @staticmethod
    def getApplicationUrl():
        url=config.get("common info","baseURL")
        return url

    @staticmethod
    def getApplicationusername():
        username=config.get("common info","username")
        return username

    @staticmethod
    def getApplicationpassword():
        password = config.get("common info", "password")
        return password