import json
import csv

def getResult():
    with open("C:\\Users\\firda\\Downloads\\sales.json") as file:
        data = json.load(file)
        result = []
        for current_item in data:
            for country in current_item['sales_by_country']:
                for year in current_item['sales_by_country'][country]:
                    result.append([current_item['item'],
                              country,
                              year,
                              current_item['sales_by_country'][country][year]])
    return result

def writeResult(result):
    with open('sales.csv', 'w') as file:
        writer = csv.writer(file)
        for row in result:
            writer.writerow(row)
        
result = getResult()
writeResult(result)

