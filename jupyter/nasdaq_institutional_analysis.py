from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from typing import List

class Nasdaq_Institution_Page_Parser:
    def __init__(self) -> None:
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        self.url_template = 'https://www.nasdaq.com/market-activity/stocks/{stock}/institutional-holdings'
        chrome_options = Options()  
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        self.driver = webdriver.Chrome(options=chrome_options)

    def load_details(self, security:str) -> pd.DataFrame:
        self.driver.get(f'https://www.nasdaq.com/market-activity/stocks/{security}/institutional-holdings')
        html = self.driver.page_source
        soup = BeautifulSoup(html)
        column_names = self._list_column_names(soup=soup)
        pass

    def _list_column_names(self, soup) -> List[str]:
        #list the columns name
        column_list = []
        column_table_begin = None
        for col in soup.find_all("span", class_="institutional-holdings__columnheader-text"):
            if col.text == "OWNER NAME":
                column_table_begin = col.parent.parent.parent
        column_table_begin        
        for col in column_table_begin.find_all("span", class_="institutional-holdings__columnheader-text"):
            column_list.append(col.text)
        return column_list