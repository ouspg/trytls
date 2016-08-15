from common import SeleniumSSLTest
from selenium import webdriver


class ChromeSSLTest(SeleniumSSLTest):
    failing_titles = ('Problem loading page',
                      'Insecure Connection',
                      'failed to load',
                      'is not private')

    def init_driver(self):
        self.driver = webdriver.Chrome(
            desired_capabilities={'acceptSslCerts': False})


ChromeSSLTest()
