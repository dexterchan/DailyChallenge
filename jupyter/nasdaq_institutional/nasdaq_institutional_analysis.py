from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from typing import List
from collections import defaultdict
import backoff

max_trial = 5


class Nasdaq_Institution_Page_Parser:
    def __init__(self) -> None:
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        self.url_template = 'https://www.nasdaq.com/market-activity/stocks/{stock}/institutional-holdings'
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        self.driver = webdriver.Chrome(options=chrome_options)

    @backoff.on_exception(
        backoff.expo, Exception, max_tries=max_trial, jitter=backoff.full_jitter
    )
    def load_details(self, security: str, page: int) -> pd.DataFrame:
        self.driver.get(
            f'https://www.nasdaq.com/market-activity/stocks/{security}/institutional-holdings')
        html = self.driver.page_source
        soup = BeautifulSoup(html)
        column_names = self._list_column_names(soup=soup)

        num_of_pages = self._get_number_of_pages(soup=soup)

        df: pd.DataFrame = self._load_to_dataframe(
            soup=soup, column_list=column_names
        )

        return df

    def _list_column_names(self, soup) -> List[str]:
        # list the columns name
        column_list = []
        column_table_begin = None
        for col in soup.find_all("span", class_="institutional-holdings__columnheader-text"):
            if col.text == "OWNER NAME":
                column_table_begin = col.parent.parent.parent
        column_table_begin
        for col in column_table_begin.find_all("span", class_="institutional-holdings__columnheader-text"):
            column_list.append(col.text)
        return column_list

    def _get_number_of_pages(self, soup) -> int:
        max_page = 0
        for bttn in soup.find_all("button", class_="pagination__page"):
            max_page = max(max_page, int(bttn.text))

    def _load_to_dataframe(self, soup, column_list=List[str]) -> pd.DataFrame:
        temp_data = defaultdict(list)
        for row in soup.find_all("a", class_="firstCell"):
            #v = row.find_next("a", class_="firstCell")
            # Get the first column
            v_row = (row.parent.parent)
            inx = 0

            for cols in v_row.find_all("td", class_="institutional-holdings__cell institutional-holdings__cell--heading"):
                temp_data[column_list[inx]].append(cols.text)
                inx += 1
        df = pd.DataFrame(data=temp_data)

        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        try:
            df[column_list[len(column_list)-1]] = df[column_list[len(column_list)-1]
                                                     ].map(lambda x: float(x.strip('$').replace(",", "")))
            df[column_list[2]] = df[column_list[2]].map(
                lambda x: float(x.strip('$').replace(",", "")))
            df[column_list[3]] = df[column_list[3]].map(
                lambda x: float(x.replace(",", "")))
            df[column_list[4]] = df[column_list[4]].map(
                lambda x: float(x[:-1])/100 if is_number(x[:-1]) else 0)
        except Exception as e:
            return df
        return df
