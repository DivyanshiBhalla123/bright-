from bs4 import BeautifulSoup as bs
import time
import requests
import pandas as pd
import csv
url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(url)
soup=bs(page.text,"html.parser")
star_table=soup.find('table')
temp=[]
table_row=star_table.find_all("tr")
for tr in table_row:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td] 
    temp.append(row)
star_names=[]
star_distance=[]
radius=[]
mass=[]
luminous=[]
for i in range(1,len(temp)):
    star_names.append(temp[i][1])
    star_distance.append(temp[i][3])
    mass.append(temp[i][5])
    radius.append(temp[i][6])
    luminous.append(temp[7])
df2=pd.DataFrame(list(zip(star_names,star_distance,mass,radius,luminous)),columns=['star_name','star_distance','mass','radius','luminous'])    
df2.to_csv('bright_stars.csv')
