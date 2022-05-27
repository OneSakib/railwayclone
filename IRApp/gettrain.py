import requests
from bs4 import BeautifulSoup


def get(f='saharanpur', t='chandigarh'):
    t = t.replace(' ', '-').lower()
    f = f.replace(' ', '-').lower()
    url = f'https://www.trainspnrstatus.com/trains/{f}-{t}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    card_header = soup.find('h1', class_='h1s').text
    table = soup.find('table')
    data = []
    for row in table:
        for cell in row.find_all('td'):
            data.append(cell.text)

    data = data[1:]
    return {'name': card_header, 'data': data}


def pnr_status(pnr_no):
    print(pnr_no, type(pnr_no))
    url = 'https://www.goibibo.com/trains/view/pnr-result/?hquery={%22pnr%22:%22' + pnr_no.strip() + '%22,%22hashid%22:%20%2243e723cb-7b8d-432c-8183-1e98d260bfcc%22}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    heading = soup.find('h2', class_='heading').text
    soup = BeautifulSoup(r.content, 'html.parser')
    broad_time = soup.find_all('span', class_='append-bottom5')
    train_info = [i.text for i in broad_time]
    return {'boarding': [train_info[2], train_info[3], train_info[4], train_info[5]],
            'destination': [train_info[6], train_info[7], train_info[8], train_info[9]], 'heading': heading}
