import configparser

config = configparser.rawConfigParser(
)
config.read('.\\configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def Password():
        password = config.get('common info', 'password')
        return password
