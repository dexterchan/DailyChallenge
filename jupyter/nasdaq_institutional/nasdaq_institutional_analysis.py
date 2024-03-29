from bs4 import BeautifulSoup
from pandas.core import indexing
from pandas.core.frame import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from typing import List, Dict
from collections import defaultdict
import backoff
import time
max_trial = 10


class Page:
    def __init__(self, bttn) -> None:
        self.bttn = bttn
        self.pagenum = int(bttn.text)

    def distance(self, targetPage: int) -> int:
        return targetPage - self.pagenum

    @backoff.on_exception(
        backoff.expo, Exception, max_tries=max_trial, jitter=backoff.full_jitter
    )
    def select(self) -> None:
        self.bttn.click()


class Nasdaq_Institution_Page_Parser:
    def __init__(self) -> None:
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        self.url_template = 'https://www.nasdaq.com/market-activity/stocks/{security}/institutional-holdings'
        options = Options()
        options.add_argument("--window-size=1920,1080")
        # Headless not working for click action
        # options.add_argument("--start-maximized")
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        options.add_argument('user-agent={0}'.format(user_agent))
        prefs = {
            # "profile.managed_default_content_settings.images": 2,
            # "profile.default_content_setting_values.notifications": 2,
            # "profile.managed_default_content_settings.stylesheets": 2,
            # "profile.managed_default_content_settings.cookies": 2,
            # "profile.managed_default_content_settings.javascript": 1,
            # "profile.managed_default_content_settings.plugins": 1,
            # "profile.managed_default_content_settings.popups": 2,
            # "profile.managed_default_content_settings.geolocation": 2,
            # "profile.managed_default_content_settings.media_stream": 2,
        }
        options.add_experimental_option("prefs", prefs)
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)

    def close(self) -> None:
        if self.driver is not None:
            self.driver.close()

    @backoff.on_exception(
        backoff.expo, Exception, max_tries=max_trial, jitter=backoff.full_jitter
    )
    def load_pages_range(self, security: str, page_start: int = 1, page_end: int = 0):
        self.driver.get(self.url_template.format(security=security))

        page_details = self._load_soup()
        num_of_pages = page_details["num_of_pages"]
        print(f"Total number of pages: {num_of_pages}")
        if page_end <= 0 or page_end > num_of_pages:
            page_end = num_of_pages
        page_start = 1 if page_start < 1 or page_start > num_of_pages else page_start

        # navigate to page_start
        current_page = self._get_current_page()
        if current_page != page_start:
            self._go_to_page(page_num=page_start)
            time.sleep(1)

        df: pd.DataFrame = pd.DataFrame()
        for p in range(page_start, page_end+1):
            print(f"loading page {p}")
            page_details = self._load_soup()
            soup = page_details["soup"]
            column_names = page_details["columns"]
            newdf: pd.DataFrame = self._load_to_dataframe(
                soup=soup, column_list=column_names
            )
            #pd.concat(df, newdf)
            df = pd.concat([df, newdf], ignore_index=True)
            if p <= page_end-1:
                self._go_to_page(page_num=p+1)
            time.sleep(1)

        return df

    @backoff.on_exception(
        backoff.expo, Exception, max_tries=max_trial, jitter=backoff.full_jitter
    )
    def load_page(self, security: str, page: int) -> pd.DataFrame:
        self.driver.get(self.url_template.format(security=security))

        page_details = self._load_soup()
        num_of_pages = page_details["num_of_pages"]
        print(f"Total number of pages: {num_of_pages}")
        if page < 1 and page > num_of_pages:
            raise Exception(f"Page should be between {1} and {num_of_pages}")
        current_page = self._get_current_page()
        if current_page != page:
            self._go_to_page(page_num=page)
            time.sleep(1)
            page_details = self._load_soup()

        soup = page_details["soup"]
        column_names = page_details["columns"]

        df: pd.DataFrame = self._load_to_dataframe(
            soup=soup, column_list=column_names
        )

        return df

    def _load_soup(self) -> Dict:
        html = self.driver.page_source
        soup = BeautifulSoup(html)
        column_names = self._list_column_names(soup=soup)
        num_of_pages = self._get_number_of_pages(soup=soup)

        return {
            "soup": soup,
            "columns": column_names,
            "num_of_pages": num_of_pages
        }

    def _go_to_page(self, page_num: int) -> None:
        current_page = self._get_current_page()
        print(f"We are at page {current_page}, load page {page_num}")
        if current_page == page_num:
            return

        pageList: List[Page] = []
        for bttn in self.driver.find_elements_by_tag_name("button.pagination__page"):
            pageList.append(Page(bttn=bttn))

        closestPage: Page = None
        page_distance = 100000
        for p in pageList:
            abs_distance = abs(p.distance(page_num))
            if abs_distance < page_distance:
                closestPage = p
                page_distance = abs_distance

        print(
            f"Going to press {closestPage.pagenum} with distance {page_distance}")
        # Press the button
        if closestPage is not None:
            closestPage.select()

        return self._go_to_page(page_num=page_num)

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
        print("Find number of pages:")
        for bttn in soup.find_all("button", class_="pagination__page"):
            print(f"Got {int(bttn.text)}")
            max_page = max(max_page, int(bttn.text))
        return max_page

    def _get_current_page(self, ) -> int:
        button = self.driver.find_element_by_tag_name(
            "button.pagination__page--active")
        return int(button.text)

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
