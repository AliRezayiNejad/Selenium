"""from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

resp = urlopen("https://tranco-list.eu/download_daily/6JZJX")
myzip = ZipFile(BytesIO(resp.read()))
for line in myzip.open('top-1m.csv').readlines():
    print(line.decode('utf-8'))"""

"""import csv
from io import TextIOWrapper
from zipfile import ZipFile

with ZipFile(r'D:\OEI\R2\Jason Polakis\tranco_6JZJX-1m.csv.zip') as zf:
    with zf.open('top-1m.csv', 'r') as infile:
        reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
        for row in reader:
            if int(row[0]) < 101:
                print(row)"""

import csv
from io import TextIOWrapper
from zipfile import ZipFile

from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
#import time
#from selenium.webdriver.common.by import By

#opt = webdriver.FirefoxOptions()
#opt.add_argument('-headless')
executable_path = Service('C:\geckodriver.exe')
driver = webdriver.Firefox(service = executable_path)

blockedWebsites = 0
totalCookieCount = 0
fullPathCount = 0
secureCount = 0
httpOnlyTrueCount = 0
partitionedCount = 0
sameSiteStrictCount = 0
sameSiteNoneCount = 0

exclude_keys = ['name', 'value', 'expiry']

with ZipFile(r'D:\OEI\R2\Jason Polakis\tranco_6JZJX-1m.csv.zip') as zf:
    with zf.open('top-1m.csv', 'r') as infile:
        reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
        for row in reader:
            if int(row[0]) < 101:
                url = 'https://' + row[1]
                try:
                    driver.get(url)
                    websiteCookieCount = len(driver.get_cookies())
                    print(row[1] + ' set ' + str(websiteCookieCount) + ' cookies.')
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
                        #print(row[1] + 'set ' + str(websiteCookieCount) + ' cookies.')
                except:
                    print(row[1] + ' is unreachable.')
                    blockedWebsites += 1
                    pass
                #time.sleep(2)
                #driver.close()
                #print(row)

print('Of the top 100 websites on the Tranco list, ' + str(blockedWebsites) + ' were blocked. The remaining have set ' + str(totalCookieCount) + ' cookies.')
#print('websiteCookieCount = ' + str(websiteCookieCount))
print(str(round((fullPathCount/totalCookieCount)*100,2)) + '% (' + str(fullPathCount) + ') of which have "/" as their "path" attribute.')
print(str(round((secureCount/totalCookieCount)*100,2)) + '% (' + str(secureCount) + ') of which have their "secure" attribute set to True.')
print(str(round((httpOnlyTrueCount/totalCookieCount)*100,2)) + '% (' + str(httpOnlyTrueCount) + ') of which have their "httpOnly" attribute set to True.')
print(str(round((partitionedCount/totalCookieCount)*100,2)) + '% (' + str(partitionedCount) + ') of which have their "partitioned" attribute set to True.')
print(str(round((sameSiteStrictCount/totalCookieCount)*100,2)) + '% (' + str(sameSiteStrictCount) + ') of which have their "sameSite" attribute set to "Strict", ' + str(round((sameSiteNoneCount/totalCookieCount)*100,2)) + '% (' + str(sameSiteNoneCount) + ') have it set to "None",' + ' and the remaining ' + str(round(((totalCookieCount - sameSiteNoneCount - sameSiteStrictCount)/totalCookieCount)*100,2)) + '% (' + str(totalCookieCount - sameSiteNoneCount - sameSiteStrictCount) + ' have it either maunally set or defaulting to "Lax".')
