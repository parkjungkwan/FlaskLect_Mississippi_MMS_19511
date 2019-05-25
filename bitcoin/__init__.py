from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from fbprophet import Prophet
from urllib.request import urlopen



"""
from urllib2 import Request, urlopen
import json
from pandas.io.json import json_normalize

path1 = '42.974049,-81.205203|42.974298,-81.195755'
request=Request('http://maps.googleapis.com/maps/api/elevation/json?locations='+path1+'&sensor=false')
response = urlopen(request)
elevations = response.read()
data = json.loads(elevations)
json_normalize(data['results'])
"""
if __name__ == '__main__':
    # driver = webdriver.Chrome('chromedriver')
    # driver.implicitly_wait(30)
    # url = 'https://bitcoincharts.com/charts/korbitKRW#rg730ztgSzm1g10zm2g25zv'
    # driver.get(url)
    # xpath = """//*[@id="content_chart"]/div/div[2]/a"""
    # variable = driver.find_element_by_xpath(xpath)
    # driver.execute_script("return arguments[0].scrollIntoView();", variable)
    # variable.click()
    # 그 메뉴가 보일 때까지 스크롤해서 내려가서 클릭하라
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    # table = pd.read_json(soup.prettify())
    # print(str(table))


    url = "https://bitcoincharts.com/charts/chart.json?m=korbitKRW&SubmitButton=Draw&r=730&i=&c=0&s=&e=&Prev=&Next=&t=S&b=&a1=&m1=10&a2=&m2=25&x=0&i1=&i2=&i3=&i4=&v=1&cv=0&ps=0&l=0&p=0&"
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    # print(soup.prettify())
    df = pd.read_json(soup.prettify())
    print(df)



