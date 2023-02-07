import csv
from io import TextIOWrapper
from zipfile import ZipFile

from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.common.by import By

#opt = webdriver.FirefoxOptions()
#opt.add_argument('-headless')
executable_path = Service('C:\geckodriver.exe')
driver = webdriver.Firefox(service = executable_path)

url = 'https://www.google.com/'
#url = 'https://www.microsoft.com/en-us/'
#url = 'https://respecta.is'
driver.get(url)

exclude_keys = ['name', 'value', 'expiry']

totalCookieCount = 0
fullPathCount = 0
secureCount = 0
httpOnlyTrueCount = 0
partitionedCount = 0
sameSiteStrictCount = 0
sameSiteNoneCount = 0

websiteCookieCount = len(driver.get_cookies())
for cookie in driver.get_cookies():
    totalCookieCount += 1
    if cookie.get('path') == '/':
        fullPathCount += 1
    if cookie.get('secure') == True:
        secureCount += 1
    if cookie.get('httpOnly') == True:
        httpOnlyTrueCount += 1
    if cookie.get('partitioned') == True:
        partitionedCount += 1
    if cookie.get('sameSite') == 'Strict':
        sameSiteStrictCount += 1
    elif cookie.get('sameSite') == 'None':
        sameSiteNoneCount += 1
    #else:
    new_d = {k: cookie[k] for k in set(list(cookie.keys())) - set(exclude_keys)}
        #print(attribute)
    print(new_d)

print('totalCookieCount = ' + str(totalCookieCount))
print('websiteCookieCount = ' + str(websiteCookieCount))
print('fullPathCount = ' + str(fullPathCount))
print('secureCount = ' + str(secureCount))
print('httpOnlyTrueCount = ' + str(httpOnlyTrueCount))
print('partitionedCount = ' + str(partitionedCount))
print('sameSiteStrictCount = ' + str(sameSiteStrictCount))
print('sameSiteNoneCount = ' + str(sameSiteNoneCount))