# -*- coding: utf-8 -*-

import json
from keyboard_util import *


def select_next_stock():
    click(973, 221, True)
    time.sleep(1)
    click(950, 239, True)
    click(1242, 221, True)
    time.sleep(1)
    click(903, 112, True)


    key_in(VK_F5)
    time.sleep(3)
    key_in(VK_F10)
    time.sleep(3)


def get_stock_sector_information():
    #下一个股 鼠标位置 {'y': 112L, 'x': 903L}
    #下一个股 右键选择 全选位置 {'y': 221L, 'x': 973L}
    #下一个股 右键选择 复制位置 {'y': 239L, 'x': 950L}
    #Assume total 1000 stocks

    #right click
    click(903, 112, False)
    time.sleep(1)

    #select all
    click(973, 221, True)

    time.sleep(1)

    #right click
    click(903, 112, False)
    time.sleep(1)

    #copy
    click(950, 239, True)
    time.sleep(3)

    #get data
    data = get_copied_data()

    return process_data(data)


def process_data(data):
    industry = None
    concepts = None
    stock_id = None
    if data is None:
        return get_stock_sector_information()
    for line in data.split('\r\n'):
        try:
            line = line.decode('gb2312')
        except:
            continue
        if stock_id is None and '60' in line:
            stock_id = int(line)
        if industry is None and u'\u6240\u5c5e\u884c\u4e1a' in line: #所属行业
            industry = line[line.find(u'\u6240\u5c5e\u884c\u4e1a')+5:].lstrip().rstrip()
        if concepts is None and u'\u6d89\u53ca\u6982\u5ff5' in line: #涉及概念
            concepts = line[line.find(u'\u6d89\u53ca\u6982\u5ff5')+5:].lstrip().rstrip().split(' ')
    print stock_id
    print concepts
    print industry

    if stock_id is None or concepts is None or industry is None:
        return get_stock_sector_information()
    return [stock_id, concepts, industry]


def add_into_dict_list_with_key (key, value, current_dict):
    if key in current_dict.keys():
        current_dict[key].append(value)
    else:
        current_dict[key] = [value]
    return current_dict

def main():
    time.sleep(10)
    print query_mouse_position()
    stock_concept = dict()
    stock_industry = dict()
    concept_stock = dict()
    industry_stock = dict()

    try:
        f = open('company_sector_data', 'r')
        data = json.loads(f.read())
        f.close()
        stock_concept = data['stock_concept']
        stock_industry = data['stock_industry']
        concept_stock = data['concept_stock']
        industry_stock = data['industry_stock']
    except:
        pass

    for i in range(1000):
        try:
            [stock_id, concepts, industry] = get_stock_sector_information()
        except:
            pass
        if stock_id not in stock_industry.keys():
            stock_industry[stock_id] = industry
            industry_stock = add_into_dict_list_with_key(industry, stock_id, industry_stock)
            stock_concept[stock_id] = concepts
            for concept in concepts:
                concept_stock = add_into_dict_list_with_key(concept, stock_id, concept_stock)
            save_record(concept_stock,industry_stock, stock_industry, stock_concept)
        clear_copied_data()
        select_next_stock()
        time.sleep(3)
    ctypes.windll.user32.MessageBoxA(0, "Done", "Python task", 1)


def save_record(concept_stock,industry_stock, stock_industry, stock_concept):
    data = dict()
    data['concept_stock'] = concept_stock
    data['industry_stock'] = industry_stock
    data['stock_industry'] = stock_industry
    data['stock_concept'] = stock_concept
    content = json.dumps(data)
    f = open('company_sector_data', 'w')
    f.write(content)
    f.close()



if __name__ == '__main__':
    main()


