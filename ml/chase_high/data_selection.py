__author__ = 'zhanyingbo'


from util import *
import numpy
import index_list
threhold = 1.96
# select last two days increase only
def follow_high(list_of_stocks):
    for ticker in list_of_stocks:
        if '601808' in ticker:
            print 'getit'
        data = prepare_raw_data(ticker, 10)
        if data is None: continue
        per_day_ratio = []
        win_ratio = []
        for each_day_data in data:
            per_day_ratio.append(each_day_data[HIGH]/each_day_data[LOW])
            win_ratio.append(each_day_data[CLOSE]/each_day_data[OPEN])
        stdev = numpy.std(numpy.array(per_day_ratio))
        mean = sum(per_day_ratio)/len(per_day_ratio)
        meet = True
        for i in range(5,10):
            if i < 8:
                if (per_day_ratio[i] - mean)/stdev > threhold and win_ratio[i] > 1:
                    meet = False
            else:
                if (per_day_ratio[i] - mean)/stdev < 1 or win_ratio[i]<1:
                    meet = False

        if meet:
            print ticker
            print index_list.INDEX_LIST[ticker]


