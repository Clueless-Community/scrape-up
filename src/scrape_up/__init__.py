import pandas as pd
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import chromedriver_binary
import string
# from selenium.webdriver.chrome.options import Options

pd.options.display.float_format = '{:.0f}'.format
# Options = Options()
# Options.add_argument('--headless=new')
# Options.headless = True

class YahooFinance:
    """
    Scrapes the data from the YahooFinance listed Stocks
    like 'APPL' by just searching that we can get the the information available about the APPLE Stock.
    """
    def __init__(self,ticker):
        self.ticker = ticker
        self.financial_url = f"https://finance.yahoo.com/quote/{self.ticker}/financials?p={self.ticker}"
        self.historical_data_url = f"https://finance.yahoo.com/quote/{self.ticker}/history?p={self.ticker}" 
        self.profile_url = f"https://finance.yahoo.com/quote/{self.ticker}/profile?p={self.ticker}"
        self.summary_url = f"https://finance.yahoo.com/quote/{self.ticker}/profile?p={self.ticker}"
        self.statistics_url = f"https://finance.yahoo.com/quote/{self.ticker}/key-statistics?p={self.ticker}"
        self.holder_url = f"https://finance.yahoo.com/quote/{self.ticker}/holders?p={self.ticker}"
        self.driver = webdriver.Chrome()
    def get_financial_data(self):
        self.driver.get(self.financial_url)
        html = self.driver.execute_script('return document.body.innerHTML;')
        soup = BeautifulSoup(html,'lxml')
        features = soup.find_all('div', class_='D(tbr)')
        headers = []
        temp_list = []
        # label_list = []
        final = []
        index = 0
        for item in features[0].find_all('div', class_='D(ib)'):
            headers.append(item.text)
        while index <= len(features)-1:
            temp = features[index].find_all('div', class_='D(tbc)')
            for line in temp:
                temp_list.append(line.text)
            final.append(temp_list)
            temp_list = []
            index+=1
        df = pd.DataFrame(final[1:])
        df.columns = headers
        return df
    def get_historical_data(self):
        self.driver.get(self.historical_data_url)
        html = self.driver.execute_script('return document.body.innerHTML;')
        soup = BeautifulSoup(html,'lxml')
        table = soup.find_all("table", attrs={"class": "W(100%)"})
        historical_table = table[0]
        body = historical_table.find_all('tr')
        head = body[0]
        body_rows = body[1:]
        headings = []
        for item in head.find_all('th'):
            item = (item.text).rstrip("\n")
            headings.append(item)
        all_rows = []
        for row_num in range(len(body_rows)):
            row = [] 
            for row_item in body_rows[row_num].find_all("td"):
                aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
                row.append(aa)
            all_rows.append(row)
        df = pd.DataFrame(data=all_rows)
        df.columns = headings
        return df
# v = YahooFinance('TSLA')
# data = v.get_historical_data()
# print(data)
# print()