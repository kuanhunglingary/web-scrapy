# Web Scraping BeautifulSoup Building

# importing module
from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import load_workbook

# Put everything together inside a For-Loop

building_name = []
building_info = []

# Web Scraping BeautifulSoup Building Changhua

for i in range (1,4):
    
    # website in variable
    website1 = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e5%bd%b0%e5%8c%96%e7%b8%a3&a2=&q=' 

    # request to website
    response = requests.get(website1,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', sheet_name = 'building', index = False, header = False)

# Web Scraping BeautifulSoup Building Chiayi City 

for i in range (1,4):
    
    # website in variable
    website2 = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e5%98%89%e7%be%a9%e5%b8%82&a2=&q=' 

    # request to website
    response = requests.get(website2,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Chiayi Couty 

# website in variable
website3 = 'http://group.lifego.tw/Litem.aspx?t=1041&a1=%e5%98%89%e7%be%a9%e7%b8%a3&a2='

# request to website
response = requests.get(website3,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
})
    
# soup object
soup = BeautifulSoup(response.content, 'html.parser')
    
# results
results = soup.find_all('div',{'class':'product-info'})
    
# loop through results
for result in results:
       
    # building name
    building_name.append(result.find('font').get_text())
      
    # building info
    building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Hsinchu

for i in range (1,7):
    
    # website in variable
    website4 = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e6%96%b0%e7%ab%b9%e7%b8%a3&a2=&q=' 

    # request to website
    response = requests.get(website4,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building HsinchuCity 

for i in range (1,8):
    
    # website in variable
    website5 = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e6%96%b0%e7%ab%b9%e5%b8%82&a2=&q=' 

    # request to website
    response = requests.get(website5,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Hualinen

for i in range (1,2):
    
    # website in variable
    website6 = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e8%8a%b1%e8%93%ae%e7%b8%a3&a2=&q=' 

    # request to website
    response = requests.get(website6,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Kaohsiung

for i in range (1,21):
    
    # website in variable
    website7 = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e9%ab%98%e9%9b%84%e5%b8%82&a2=&q=' 

    # request to website
    response = requests.get(website7,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Keelung

for i in range (1,6):
    
    # website in variable
    website8 = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e5%9f%ba%e9%9a%86%e5%b8%82&a2=&q=' 

    # request to website
    response = requests.get(website8,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Kinmen

# website in variable
website9 = 'http://group.lifego.tw/Litem.aspx?t=1041&a1=%e9%87%91%e9%96%80%e7%b8%a3&a2='

# request to website
response = requests.get(website9,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
})
    
# soup object
soup = BeautifulSoup(response.content, 'html.parser')
    
# results
results = soup.find_all('div',{'class':'product-info'})
    
# loop through results
for result in results:
       
    # building name
    building_name.append(result.find('font').get_text())
      
    # building info
    building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Miaoli

for i in range (1,3):
    
    # website in variable
    website = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e8%8b%97%e6%a0%97%e7%b8%a3&a2=&q=' 

    # request to website
    response = requests.get(website,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Nantou

for i in range (1,2):
    
    # website in variable
    website = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e5%8d%97%e6%8a%95%e7%b8%a3&a2=&q=' 

    # request to website
    response = requests.get(website,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building NewTaipei

for i in range (1,21):
    
    # website in variable
    website = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e6%96%b0%e5%8c%97%e5%b8%82&a2=&q=' 

    # request to website
    response = requests.get(website,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Penghu

# website in variable
website = 'http://group.lifego.tw/Litem.aspx?t=1041&a1=%e6%be%8e%e6%b9%96%e7%b8%a3&a2='

# request to website
response = requests.get(website,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
})
    
# soup object
soup = BeautifulSoup(response.content, 'html.parser')
    
# results
results = soup.find_all('div',{'class':'product-info'})
    
# loop through results
for result in results:
       
    # building name
    building_name.append(result.find('font').get_text())
      
    # building info
    building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Pingtung

for i in range (1,3):
    
    # website in variable
    website = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e5%b1%8f%e6%9d%b1%e7%b8%a3&a2=&q=' 

    # request to website
    response = requests.get(website,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Taichung

for i in range (1,3):
    
    # website in variable
    website = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e5%8f%b0%e4%b8%ad%e5%b8%82&a2=&q=' 

    # request to website
    response = requests.get(website,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Tainan

for i in range (1,6):
    
    # website in variable
    website = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e5%8f%b0%e5%8d%97%e5%b8%82&a2=&q=' 

    # request to website
    response = requests.get(website,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Taipei

for i in range (1,21):
    
    # website in variable
    website = 'https://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e5%8f%b0%e5%8c%97%e5%b8%82&a2=&q=' 

    # request to website
    response = requests.get(website,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Taitung 

# website in variable
website = 'https://group.lifego.tw/Litem.aspx?t=1041&page=1&a1=%e5%8f%b0%e6%9d%b1%e7%b8%a3&a2='

# request to website
response = requests.get(website,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
})
    
# soup object
soup = BeautifulSoup(response.content, 'html.parser')
    
# results
results = soup.find_all('div',{'class':'product-info'})
    
# loop through results
for result in results:
       
    # building name
    building_name.append(result.find('font').get_text())
      
    # building info
    building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Taoyuan

for i in range (1,21):
    
    # website in variable
    website = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e6%a1%83%e5%9c%92%e7%b8%a3&a2=&q=' 

    # request to website
    response = requests.get(website,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Yilan

for i in range (1,4):
    
    # website in variable
    website = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e5%ae%9c%e8%98%ad%e7%b8%a3&a2=&q=' 

    # request to website
    response = requests.get(website,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)

# Web Scraping BeautifulSoup Building Yunlin

for i in range (1,2):
    
    # website in variable
    website = 'http://group.lifego.tw/Litem.aspx?t=1041&page=' + str(i) + '&a1=%e9%9b%b2%e6%9e%97%e7%b8%a3&a2=&q=' 

    # request to website
    response = requests.get(website,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find_all('div',{'class':'product-info'})
    
    # loop through results
    for result in results:
        
        # building name
        building_name.append(result.find('font').get_text())
        
        # building info
        building_info.append(result.find('span').get_text())

# dictionary
building_detail = pd.DataFrame({'Building_Name': building_name, 'Building_Info': building_info})

# Output in Excel
building_detail.to_excel('OldBuilding.xlsx', index = False, header = False)
# building_detail.to_csv('OldBuilding.csv', index = False, header = False)