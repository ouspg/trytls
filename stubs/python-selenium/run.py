from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get_log('browser')

import sys

host = sys.argv[1]
port = sys.argv[2]

driver.get("https://" + host + ":" + port)
if 'Problem loading page' or 'Insecure connection' in driver.title:
    logs=driver.get_log('browser')
    print(''.join([x.get('message','') for x in logs]))
    print("VERIFY FAILURE")
else:
    print("VERIFY SUCCESS")

driver.close()
