from common import SeleniumSSLTest
from selenium import webdriver


class FirefoxSSLTest(SeleniumSSLTest):
    failing_titles = ('Problem loading page',
                      'Insecure Connection',
                      'failed to load',
                      'is not private')

    def init_driver(self):
        self.driver = webdriver.Firefox(capabilities={'acceptSslCerts': False})


FirefoxSSLTest()
