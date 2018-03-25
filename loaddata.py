import pandas as pd
import matplotlib.pyplot as plt



global fileName
global filePath

fileName = 'SolarData.csv'
filePath = '~/PycharmProjects/Solar/'


def plotData(data):
    # plt.plot(data['Radiation'],'r.-')  # 'r' is the color red
    plt.xlabel('Time')
    plt.ylabel('Radiation')
    plt.title('String Title Here')
    # plt.plot_date(data['Time'],data['Radiation'],'r.-')
    plt.plot(data['Radiation'],'r.-')
    plt.gcf().autofmt_xdate()
    plt.show()

def SelOneDay(DateStr, df) :
    daily = df.loc[df['Data'].str.contains(DateStr)]
    return daily

def LoadData():

    df = pd.DataFrame()
    df = pd.read_csv(filePath+fileName)
    df.sort_values(by=['UNIXTime'])
    return df


def main():

    print('Start Load Dataset')
    df = pd.DataFrame()
    df = LoadData()
    oneday = SelOneDay('9/29/2016', df)
    plotData(oneday)


if __name__ == '__main__':
    main()