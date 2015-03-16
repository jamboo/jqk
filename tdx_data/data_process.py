__author__ = 'Winface'

import run_config


def prepare_daily_raw_data(filename):
    file_handle = open(filename, 'r')
    lines = file_handle.readlines()
    result = []

    for line in lines:
        parts = line.split(',')
        date = int(parts[0])
        result.append([date, float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]), float(parts[6])])

    if run_config.backdate is not None and run_config.backdate <= len(result):
        return result[len(result)-run_config.backdate:]
    # smaller time comes first
    return result

