import json
import csv

def getResult():
    with open("C:\\Users\\firda\\Downloads\\sales.json") as file:
        data = json.load(file)
        result = []
        for i in data:
            for country in i['sales_by_country']:
                for year in i['sales_by_country'][country]:
                    result.append([i['item'],
                              country,
                              year,
                              i['sales_by_country'][country][year]])
    return result

def writeResult(result):
    with open('sales.csv', 'w') as file:
        writer = csv.writer(file)
        for row in result:
            writer.writerow(row)
        
result = getResult()
writeResult(result)

