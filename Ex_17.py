


# from bs4 import BeautifulSoup
# import urllib.request

# response = urllib.request.urlopen('https://www.nytimes.com/')

# soup = BeautifulSoup(response, 'lxml')
# for heading in soup.find_all('h3'):
#     print(heading.get_text())


#Rozwiązanie znalezione, nie autorskie
import requests
r = requests.get('https://www.nytimes.com/', auth=('user', 'pass'))


r.headers['content-type']


print(r.url)