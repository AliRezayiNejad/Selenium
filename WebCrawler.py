"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

executable_path = Service('C:\geckodriver.exe')
opt = webdriver.FirefoxOptions()
opt.add_argument('-headless')
driver = webdriver.Firefox(service=executable_path, options=opt)

driver.get('http://www.gutenberg.org/ebooks/search/%3Fsort_order%3Drelease_date')"""

"""books = (driver.find_elements(By.CLASS_NAME, "booklink"))
print(len(books))
print(books[0].text)
#print(books[-1].text)

name = books[0].find_elements(By.CLASS_NAME, "title")[0].text
author = books[0].find_elements(By.CLASS_NAME, "subtitle")[0].text
date = books[0].find_elements(By.CLASS_NAME, "extra")[0].text
print()
print(name)
print(author)
print(date)

name = books[-1].find_elements(By.CLASS_NAME, "title")[0].text
author = books[-1].find_elements(By.CLASS_NAME, "subtitle")[0].text
date = books[-1].find_elements(By.CLASS_NAME, "extra")[0].text
print()
print(name)
print(author)
print(date)"""

"""for book in books:
    try:
        name = book.find_elements(By.CLASS_NAME, "title")[0].text
        try:
            author = book.find_elements(By.CLASS_NAME, "subtitle")[0].text
        except:
            author = 'Not availbale'
        try:
            date = book.find_elements(By.CLASS_NAME, "extra")[0].text
        except:
            date = 'Not availbale'
        print('name:', name)
        print('author :', author)
        print('date :', date)
        print('_'*100)
    except:
        pass

driver.find_elements(By.CLASS_NAME, "statusline")
driver.find_elements(By.CLASS_NAME, "statusline")[0].text
driver.find_elements(By.CLASS_NAME, "statusline")[1].text

statusline = driver.find_elements(By.CLASS_NAME, "statusline")[0]
next_button = statusline.find_elements(By.TAG_NAME, "a")
next_button

print(next_button[0].text)

next_button[0].click()"""

#print(next_button[0].text)

"""count = 0
while True:
    if count == 5:
        break
    count += 1
    print('page ',count)
    books = (driver.find_elements(By.CLASS_NAME, "booklink"))
    
    for book in books:
        try:
            name = book.find_elements(By.CLASS_NAME, "title")[0].text
            try:
                author = book.find_elements(By.CLASS_NAME, "subtitle")[0].text
            except:
                author = 'Not available'
            try:
                date = book.find_elements(By.CLASS_NAME, "extra")[0].text
            except:
                date = 'Not available'
            print('name:', name)
            print('author :', author)
            print('date :', date)
            print('_'*100)
        except:
            pass
        
    #driver.find_elements_by_class_name('statusline')[0].find_elements_by_tag_name('a')[-1].click()
    driver.find_elements(By.CLASS_NAME, "statusline")[0].find_elements(By.TAG_NAME, "a")[-1].click()
    print('|'*100)"""


"""count = 0
while True:
    if count == 5:
        break
    count += 1
    print('page ',count)
    books = driver.find_elements(By.CLASS_NAME, "booklink")
    
    for book in books[:2]:
        name = book.find_elements(By.CLASS_NAME, "title")[0].text
        try:
            author = book.find_elements(By.CLASS_NAME, "subtitle")[0].text
        except:
                author = 'Not available'
        try:
            date = book.find_elements(By.CLASS_NAME, "extra")[0].text
        except:
                date = 'Not available'
        print('name:', name)
        print('author :', author)
        print('date :', date)
        print('_'*100)
        
    driver.find_elements(By.CLASS_NAME, "statusline")[0].find_elements(By.TAG_NAME, "a")[-1].click()
    print('|'*100)"""

"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

executable_path = Service('C:\geckodriver.exe')
opt = webdriver.FirefoxOptions()
opt.add_argument('-headless')
driver = webdriver.Firefox(service = executable_path, options = opt)

driver.get('https://respecta.is/')
#driver.get('http://www.gutenberg.org/ebooks/search/%3Fsort_order%3Drelease_date')

releases = driver.find_elements(By.CLASS_NAME, "publication")
for release in releases:
        try:
            category = release.find_element(By.CLASS_NAME, "category").text
            title = release.find_elements(By.TAG_NAME, "a")[1].text
            #statusline = driver.find_elements(By.CLASS_NAME, "statusline")[0]
            #next_button = statusline.find_elements(By.TAG_NAME, "a")
            #try:
                #author = book.find_elements(By.CLASS_NAME, "subtitle")[0].text
            #except:
                #author = 'Not available'
            #try:
                #date = book.find_elements(By.CLASS_NAME, "extra")[0].text
            #except:
                #date = 'Not available'
            if category == "Albums":
                print('Artist: ', title.partition(" - ")[0])
                print('Title: ', title.partition(" - ")[2])
                print('Album Type: Studio Album')
                #print('date :', date)
                print('_'*100)
            if category == "Mixtapes":
                print('Artist: ', title.partition(" - ")[0])
                print('Title: ', title.partition(" - ")[2])
                print('Album Type: Mixtape')
                #print('date :', date)
                print('_'*100)
        except:
            pass
    #print(release.text)"""

from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.common.by import By

opt = webdriver.FirefoxOptions()
opt.add_argument('-headless')

executable_path = Service('C:\geckodriver.exe')
driver = webdriver.Firefox(service = executable_path, options = opt)

url = "https://news.ycombinator.com/"
driver.get(url)
time.sleep(2)

#elements = driver.find_elements_by_css_selector(".storylink")
fullElements = driver.find_elements(By.CSS_SELECTOR, ".titleline a")
sitebitComhead = driver.find_elements(By.CSS_SELECTOR, ".sitebit.comhead a")
elements = [i for i in fullElements if i not in sitebitComhead]
#elements = driver.find_elements(By.CLASS_NAME("athing"))
#elements = driver.find_elements(By.CLASS_NAME, "titleline")
#elements = driver.find_elements(By.CSS_SELECTOR, "div#list-all div.titleline > a")

storyTitles = [el.text for el in elements]
storyUrls = [el.get_attribute("href") for el in elements]

temp = driver.find_elements(By.CSS_SELECTOR, ".score")
scores = [el.text for el in temp]

print(storyTitles)
print()
print(storyUrls)
print()
#print(storyTitles[0])
#print(storyUrls[0])
print(scores)