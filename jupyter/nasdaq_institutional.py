#!/usr/bin/env python
# coding: utf-8

# In[ ]:


stock="aapl"


# In[ ]:


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()  
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
chrome_options.add_argument("--headless")
chrome_options.add_argument('user-agent={0}'.format(user_agent))
driver = webdriver.Chrome(options=chrome_options)


# In[ ]:


driver.get(f'https://www.nasdaq.com/market-activity/stocks/{stock}/institutional-holdings')


# In[ ]:


html = driver.page_source
soup = BeautifulSoup(html)


# In[ ]:


#list the columns name
column_list = []
column_table_begin = None
for col in soup.find_all("span", class_="institutional-holdings__columnheader-text"):
    if col.text == "OWNER NAME":
        column_table_begin = col.parent.parent.parent
column_table_begin        
for col in column_table_begin.find_all("span", class_="institutional-holdings__columnheader-text"):
    column_list.append(col.text)
column_list


# In[ ]:


# Get number of pages
max_page = 0
for bttn in soup.find_all("button", class_="pagination__page"):
    max_page = max(max_page, int(bttn.text))


# In[ ]:


import pandas as pd
from collections import defaultdict
from typing import List
def load_to_dataframe(soup, column_list=List[str]) -> pd.DataFrame:
    temp_data = defaultdict(list)
    for row in soup.find_all("a", class_="firstCell"):
        #v = row.find_next("a", class_="firstCell")
        # Get the first column
        v_row = (row.parent.parent)
        inx = 0

        for cols in v_row.find_all("td", class_="institutional-holdings__cell institutional-holdings__cell--heading"):
            temp_data[column_list[inx]].append(cols.text)
            inx += 1
    df = pd.DataFrame(data=temp_data )
    df[column_list[len(column_list)-1]] = df[column_list[len(column_list)-1]].map(lambda x: float(x.strip('$').replace(",","")))
    df[column_list[2]] = df[column_list[2]].map(lambda x: float(x.strip('$').replace(",","")))
    df[column_list[3]] = df[column_list[3]].map(lambda x: float(x.replace(",","")))
    df[column_list[4]] = df[column_list[4]].map(lambda x: float(x[:-1])/100)
    return df
df = load_to_dataframe(soup=soup, column_list=column_list)


# In[ ]:


df.to_csv(f"nasdaq.institution.selenium.{stock}.csv", index=False)
df


# In[ ]:



bttn2 = None
for bttn in soup.find_all("button", class_="pagination__page"):
    print(bttn.text)
    if bttn.text == "2":
        bttn2 = bttn


# In[ ]:


try:
    buttons = driver.find_elements_by_tag_name("button.pagination__page")
    buttons[0].click()
except Exception as ex:
    print(f"exception:{ex}")


# In[ ]:


max_page


# In[ ]:



html = driver.page_source
soup = BeautifulSoup(html)


# In[ ]:


with open ("page.txt", "w") as f:
    f.write(soup.text)


# In[ ]:


with open("page.html", "w") as f:
    f.write(str(soup))


# In[ ]:


from collections import defaultdict

temp_data = defaultdict(list)


# In[ ]:


driver.close()


# In[ ]:


float("-12")


# In[ ]:


"12%"[:-1]


# In[ ]:




