import requests
from bs4 import BeautifulSoup
from time import sleep
for each in range(1,6):
    url_link = 'https://alta.ge/notebooks-page-{}.html'.format(each)
    request = requests.get(url_link)
    print(request)
    text = request.text

    soup = BeautifulSoup(text, 'html.parser')
    x = soup.find('div', {'class': 'grid-list'})
    f = open('content.csv', 'a')
    for i in x.find_all('div'):
        try:
            notebook = i.find('a', {'class': 'product-title'})
            print(notebook.text)

            f.write(notebook.text + '\n')
        except:
            continue
    sleep(20)