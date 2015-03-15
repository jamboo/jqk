__author__ = 'Winface'


import os
from constants.constants import *
#return file names only
def iterate_file_names():
    list_files = []
    markets_folder = [sz_data_directory, sh_data_directory]
    for market_folder in markets_folder:
        for file in os.listdir(market_folder):
            if file.endswith(".day"):
                list_files.append(file)
    return list_files
