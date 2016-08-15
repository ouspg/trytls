from selenium import webdriver
import re
import sys

driver = webdriver.Firefox(capabilities={'acceptSslCerts': False})
#driver = webdriver.Chrome(desired_capabilities={'acceptSslCerts': False})
driver.get_log('browser')

host = sys.argv[1]
port = sys.argv[2]

failing_titles = ('Problem loading page',
                  'Insecure Connection',
                  'failed to load',
                  'is not private')

driver.get("https://" + host + ":" + port)

for t in failing_titles:
    if t in driver.title:
        logs = [x.get('message', '') for x in driver.get_log('browser')]
        ssl_logs = filter(lambda x: re.search(
            '(ssl|tls|https)', x, re.IGNORECASE), logs)
        print(''.join(logs))
        print("REJECT")
        break
else:
    print("ACCEPT")

driver.close()
