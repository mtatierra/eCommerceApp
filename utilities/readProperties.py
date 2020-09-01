import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get('common info','baseUrl')
        return url

    @staticmethod
    def getUserName():
        userName = config.get('common info','userName')
        return userName

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password
