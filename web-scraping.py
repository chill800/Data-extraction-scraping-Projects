from bs4 import BeautifulSoup as b
import requests as r
import pandas as p


myUrl = 'https://www.skysports.com/f1/standings'
# gets the url text
downloadURL = r.get(myUrl, headers={'User-Agent': 'test'})
# use html parser to convert to text
soap = b(downloadURL.text, "html.parser")

fullTable = soap.select('tbody')[0]
driver = fullTable.select('a span')

tableRows = []

for d in driver:
    tableRows.append(str(d).replace(
        '<span class="standing-table__cell--name-text">', '').replace('</span>', '').strip())

df = p.DataFrame(tableRows, columns=['DriversName'])
df.to_excel(r'C:\Users\chene\Documents\Resume and certificates\export_dataframe.xlsx',
            sheet_name='Drivers', header=True)
print(df)
