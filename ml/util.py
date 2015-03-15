__author__ = 'zhanyingbo'

from datetime import datetime
import os




DATA_DIRECTORY = "/Users/zhanyingbo/Desktop/Python/stock/data/"

def prepare_raw_data(filename,sample=None):
    file_handle = open(filename, 'r')
    lines = file_handle.readlines()
    result = []

    for line in lines:
        parts = line.split(',')
        date = int(parts[0])
        result.append([date, float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]), float(parts[6])])

    if sample is not None and sample <= len(result):
        return result[len(result)-sample:]
    # smaller time comes first
    return result

        






