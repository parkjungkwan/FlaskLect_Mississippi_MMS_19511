from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask_restful import reqparse

class KospiController:
    def __init__(self):
        pass

    def service(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str, required=True)
        args = parser.parse_args()
        print('입력된 URL : {}'.format(args.url))
        page = urlopen(args.url)
        soup = BeautifulSoup(page, 'html.parser')
        print(soup.prettify())
        kospi = soup.find('span', id = 'KOSPI_now')
        return kospi.string