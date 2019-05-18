from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask_restful import reqparse

class StockTickerController:
    def __init__(self):
        pass

    def service(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ticker', type=str, required=True)
        args = parser.parse_args()
        print('입력된 종목코드 : {}'.format(args.ticker))
        url = 'https://finance.naver.com/item/sise_day.nhn?code='+args.ticker
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        print(soup.prettify())
        # price = soup.find('span', id = 'KOSPI_now')
        return ''