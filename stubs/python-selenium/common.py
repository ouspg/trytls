
import re
import sys


class SeleniumSSLTest(object):
    driver = None
    failing_titles = ()

    def __init__(self):
        if len(sys.argv) < 3:
            exit("Usage: %s <HOST> <PORT>" % sys.argv[0])
        elif len(sys.argv) > 3:
            print("UNSUPPORTED")
            exit(0)

        host = sys.argv[1]
        port = sys.argv[2]
        url = "https://" + host + ":" + port
        self.init_driver()
        self.run_test(url)

    def run_test(self, url):
        if self.driver is None:
            exit("No driver")
        self.driver.get_log('browser')
        self.driver.get(url)

        for t in self.failing_titles:
            if t in self.driver.title:
                logs = [x.get('message', '')
                        for x in self.driver.get_log('browser')]
                ssl_logs = filter(lambda x: re.search(
                    '(ssl|tls|https)', x, re.IGNORECASE), logs)
                print(''.join(ssl_logs))
                print("REJECT")
                break
        else:
            print("ACCEPT")
        self.driver.close()
