import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.crowdcube.com/investments")
soup=BeautifulSoup(r.content,'html.parser')

##############Finding Company Names+taglines####################

company_html = soup.find_all("div", { "class" : "cc-card__body" })

names = []
taglines = []
for company in company_html:
	company_data = company.get_text()[1:-2].split('\n')
	names.append(company_data[0])
	taglines.append(company_data[1])

#print names
#print taglines


#################Finding Company Numbers################

numbers = []
numbers_html = soup.find_all("dd", { "class" : "cc-inlineStats__value" })

for number in numbers_html:
	numbers.append(number.get_text() ) 

raised = []
equitys = []
investors = []

i=0
while i<len(numbers):
	raised.append(numbers[i])     
	i+=1 
	
	equitys.append(numbers[i])
	i+=1
	
	investors.append(numbers[i])
	i+=1

#print raised
#print equitys
#print investors



############################Days Left########################


DaysLefts = []
DaysLefts_html = soup.find_all("div", { "class" : "cc-card__daysLeft" })

for DaysLeft in DaysLefts_html:
	DaysLefts.append( DaysLeft.get_text() )

#print DaysLefts



############################Target########################


targets = []
targets_html = soup.find_all("div", { "class" : "cc-card__raisedTotal" })

for target in targets_html:
	targets.append( target.get_text().split(' ')[0] )

#print targets



############################Putting all in CSV##############

import pandas as pd
df = pd.DataFrame(
    {'COMPANY NAME': names,
     'COMPANY TAGLINE': taglines,
      'TARGET': targets,
     'RAISED': raised,
	 'EQUITY': equitys,
	 'INVESTOR': investors,
	 'Days Left': DaysLefts
    })

df.to_csv('crowdcube.csv', sep=',', encoding='utf-8', index = False)

