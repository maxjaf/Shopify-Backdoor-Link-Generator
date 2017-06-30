import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlparse
#MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1

url = '' #input url of shopify product 
quantity = '' #input quantity of item you want to buy
size = '' #input item size in the same format as on the website

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
website = urlparse(url)

#build xml link
baseurl = 'https://'+website.netloc+'/cart/'
xml = url+'.xml'
print('looking for variants using link: {}'.format(xml))

#parse variant
xmlopen = urllib.request.urlopen(xml).read()
soup = BeautifulSoup(xmlopen, 'xml')
try:
    variant = soup.find(text=size).findPrevious('id').text
    print('variant {} found for size {}'.format(variant, size))

except AttributeError:
    print('Attribute Error: size could not be found')

#build BD link
try:
    BD = baseurl+variant+':'+quantity
    print('succesfully created backdoor link: {}'.format(BD))
    
except NameError:
     print('Name Error: size could not be found')

#open link
print('opening backdoor link')
driver = webdriver.Chrome()
driver.get(BD)
print('follow @MJsneaks1 on twitter')
#MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1MJsneaks1


         


