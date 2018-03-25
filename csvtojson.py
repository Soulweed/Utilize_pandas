import csv
import json


global fileName
global filePath

fileName = 'SolarData.csv'
filePath = '~/PycharmProjects/Solar/'


def extrac2json(data):
    for ind in range(len(data)) :
        datajson = json.dumps(data[ind])
        print(datajson)

def read_csv():
    reader = csv.DictReader(open('./Solar.csv', 'r',encoding='utf-8'))
    data = []
    for row in reader:
        data.append(row)

    return data

def main():
    print('Start Convert CSV to JSON Program')
    data = read_csv()
    extrac2json(data)

if __name__ == '__main__':
    main()