import requests
import csv
from bs4 import BeautifulSoup

def getRecords(id):
    resp = requests.get("http://www.cbr.ru/scripts/XML_dynamic.asp",
                    params = {
                        "date_req1":"01/03/2020",
                        "date_req2":"01/07/2020",
                        "VAL_NM_RQ":id})
    soup = BeautifulSoup(resp.content, 'xml')
    return soup.findAll('Record')
    
idUSA = "R01235"
idEuro = "R01239"
idInd = "R01270"
idUkr = "R01720"
recordsUSA = getRecords(idUSA)
recordsEuro = getRecords(idEuro)
recordsInd = getRecords(idInd)
recordsUkr = getRecords(idUkr)

result = [['Дата', 'Доллар США', 'Евро', 'Индийская Рупия', 'Украинская гривна']]
for i in range(len(recordsUSA)):
    result.append([recordsUSA[i]['Date'],recordsUSA[i].Value.text,
                   recordsEuro[i].Value.text,
                   recordsInd[i].Value.text,
                   recordsUkr[i].Value.text])
with open('currency.csv', 'w') as file:
    writer = csv.writer(file)
    for row in result:
        writer.writerow(row)
