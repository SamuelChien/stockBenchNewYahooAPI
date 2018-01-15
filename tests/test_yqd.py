from yahoo_quote_download import yqd
import csv
import urllib2
import operator
import datetime


class StockBench:
    def __init__(self):
        self.nasdaqCompanyList = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"

    def getSymbolList(self):
        response = urllib2.urlopen(self.nasdaqCompanyList)
        cr = csv.reader(response)

        currentDate = datetime.datetime.now()
        earlierDate = currentDate - datetime.timedelta(days=180)
        currentDateStr = currentDate.strftime("%Y%m%d")
        earlierDateStr = earlierDate.strftime("%Y%m%d")

        # SymbolDict = {}
        # for row in cr: 
        #     if row[0] != "Symbol":
        #         print row[0]
                
        #         try:
        #             historicalData = yqd.load_yahoo_quote(row[0], earlierDateStr, currentDateStr)
        #             SymbolDict[row[0]] = float(historicalData[-2].split(",")[1]) * 100 / float(historicalData[1].split(",")[1])
        #         except:
        #             continue

        # sorted_symbol = sorted(SymbolDict.items(), key=operator.itemgetter(1))
        # print sorted_symbol

        with open('csvOutput/eggs.csv', 'wb') as csvfile:
            csvWriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for row in cr: 
                if row[0] != "Symbol":
                    print row[0]
                    try:
                        historicalData = yqd.load_yahoo_quote(row[0], earlierDateStr, currentDateStr)
                        for day in historicalData[1:]:
                            if day == "":
                                continue
                            dayList = day.split(",")
                            result = [row[0], dayList[0], dayList[1]]
                            csvWriter.writerow(result)
                    except:
                        continue


if __name__ == "__main__":
    StockBench().getSymbolList()


