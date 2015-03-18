__author__ = 'zhanyingbo'

from data_selection import  follow_high

import download
import index_list
from test_buy_date import t20141217, t20141218

from dataScript.algo.macd import *
def main():
    print 'done'
    #download.update()
    # list_of_stocks = index_list.INDEX_LIST.keys()
    # t20141217.test(list_of_stocks)
    # t20141218.test(list_of_stocks)
    #follow_high(list_of_stocks)

#
# def test2():
#     correct_performance = {}
#     correct_number = {}
#     for index in sorted(index_list.INDEX_LIST.keys()):
#         print index + 'done'
#         data = a1.prepare_data(index)
#         if data == None:
#             print index + ' data invalid'
#             continue
#         clf = KNeighborsClassifier(n_neighbors=5, weights='distance')
#         clf.fit(data['learning_sample'], data['learning_target'])
#
#         testing_result = clf.predict(data['testing_sample'])
#         performance = performance_evaluation(testing_result,data['testing_target'])
#         tomorrow_result = clf.predict(a1.generate_next_trading_data(index))[0]
#         if tomorrow_result == 1:
#             correct_performance[index] = performance['buy_correct']
#             correct_number[index] = performance['total_buy']
#
#
#
#
#     print 'correct_performance'
#     print correct_performance
#     sorted_x = sorted(correct_performance.items(), key=operator.itemgetter(1), reverse=True)
#     print sorted_x
#
#
#     print 'correct_number'
#     print correct_number
#     sorted_x = sorted(correct_number.items(), key=operator.itemgetter(1), reverse=True)
#     print sorted_x
#
#
#
# def test():
#     correct_performance = {}
#     final_data = {'learning_sample':[],'learning_target':[],'testing_sample':[]}
#     for index in index_list.INDEX_LIST.keys():
#         data = a1.prepare_data(index)
#         if data == None:
#             print index + ' data invalid'
#             continue
#         final_data['learning_sample'] += data['learning_sample']
#         final_data['learning_target'] += data['learning_target']
#     clf = RandomForestClassifier(n_estimators=10)
#     clf.fit(final_data['learning_sample'], final_data['learning_target'])
#
#     for index in index_list.INDEX_LIST.keys():
#         data = a1.prepare_data(index)
#         if data == None:
#             print index + ' data invalid'
#             continue
#         testing_result = clf.predict(data['testing_sample'])
#         performance = performance_evaluation(testing_result,data['testing_target'])
#
#         tomorrow_result = clf.predict(a1.generate_next_trading_data(index))[0]
#         if tomorrow_result == 1:
#             correct_performance[index] = performance['buy_correct']
#
#
#
#     print 'correct_performance'
#     print correct_performance
#     sorted_x = sorted(correct_performance.items(), key=operator.itemgetter(1), reverse=True)
#     print sorted_x


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
else:
    pass