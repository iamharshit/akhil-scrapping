import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.seedrs.com/invest")
soup=BeautifulSoup(r.content,'html.parser')

##############Finding Company Names####################

names_html = soup.find_all("h3", { "class" : "CampaignCard-campaignName" })

names = []
for name in names_html:
	names.append( name.get_text()[1:-2] )

#print names


#################Finding Company Taglines################

taglines_html = soup.find_all("p", { "class" : "CampaignCard-campaignSummary show-for-large-only show-for-medium-only" })

taglines = []
for tagline in taglines_html:
	taglines.append( tagline.get_text()[1:-2] )

#print taglines


#################Finding Numbers(equity+investments+investors)######################

numbers_html = soup.find_all("p", { "class" : "CampaignCard-statValue" })

numbers = []
for number in numbers_html:
	numbers.append( number.get_text() )

equitys = []
investments = []
investors = []

i=0
while i<len(numbers):
	equitys.append(numbers[i])     
	i+=1 
	
	investments.append(numbers[i])
	i+=1
	
	investors.append(numbers[i])
	i+=1

#print equitys
#print investments
#print investors


########################Finding Country#######################

countrys_html = soup.find_all("p", { "class" : "CampaignCard-country" })

countrys = []
for country in countrys_html:
	countrys.append( country.get_text()[2:-1] )

#print countrys


########################Finding ProgressMessage#######################

ProgressMessages_html = soup.find_all("footer", { "class" : "CampaignCard-progressMessage" })

ProgressMessages = []
for ProgressMessage in ProgressMessages_html:
	ProgressMessages.append( ProgressMessage.get_text()[1:-1] )

#print ProgressMessages



#######################Writing into csv file############

import pandas as pd
df = pd.DataFrame(
    {'COMPANY NAMES': names,
     'COMPANY TAGLINES': taglines,
      'COUNTRYS': countrys,
     'EQUITYS': equitys,
	 'INVESTMENTS': investments,
	 'INVESTORS': investors,
	 'PROGRESS MESSAGES': ProgressMessages
    })

df.to_csv('seedrs.csv', sep=',', encoding='utf-8', index = False)





