from bs4 import BeautifulSoup
import requests
import pandas as pd

# Put everything together inside a For-Loop
company_name = []
company_info = []

# website in variable 
website = 'https://goodinfo.tw/tw/StockList.asp?MARKET_CAT=%E5%85%A8%E9%83%A8&INDUSTRY_CAT=%E8%B3%87%E8%A8%8A%E6%9C%8D%E5%8B%99%E6%A5%AD&SHEET=%E4%BA%A4%E6%98%93%E7%8B%80%E6%B3%81&SHEET2=%E6%97%A5&RPT_TIME=%E6%9C%80%E6%96%B0%E8%B3%87%E6%96%99'

# request to website 
response = requests.get(website, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
})

# soup object 
soup = BeautifulSoup(response.content, 'html.parser')

# results
results = soup.find('table',{'class':'r10 b1 p4_1'})

# Create column name
columns = [th.text.replace('\n', '') for th in results.find('tr').find_all('th')]

# loop through 
trs = results.find_all('tr')[1:]
rows = list()
for tr in trs:
    rows.append([td.text.replace('\n', '').replace("\xa0",'') for td in tr.find_all('td')])

for tr in trs:
    rows.append(tr.find('td').get_text())

# dictionary
company_detail = pd.DataFrame(data = rows, columns = columns)

# Output in Excel
company_detail.to_excel('TechCompanies.xlsx', index = False)