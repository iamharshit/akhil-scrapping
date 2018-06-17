import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
r=requests.get("https://www.fundingcircle.com/us/resources#", headers=headers)
soup=BeautifulSoup(r.content,'html.parser')



##############Finding Category####################
categorys = []

categorys_html = soup.find_all("h6", { "class" : "headline6" })

for category in categorys_html:
	categorys.append(category.get_text() ) 

#print categorys



################## TOPIC ##########################

topics = []

topics_html = soup.find_all("h2", { "class" : "headline5" })
for topic in topics_html:
	topics.append(topic.get_text() ) 

#print topics



################# CONTENT ########################

contents = []

contents_html = soup.find_all("p", { "class" : "body2" })
for content in contents_html:
	contents.append(content.get_text() ) 

#print contents


############## Data Cleaning #################

actual_index = min(len(categorys), len(topics), len(contents))
categorys = categorys[:actual_index]  
topics = topics[:actual_index]
contents = contents[:actual_index]

############### Putting in csv ######################

import pandas as pd
df = pd.DataFrame(
    {'CATEGORY': categorys,
     'TOPIC': topics,
     'CONTENT': contents,
    })

df.to_csv('fundingcircle.csv', sep=',', encoding='utf-8', index = False)


