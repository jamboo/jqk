__author__ = 'yingbozhan'

from constants.constants import OPEN, HIGH, LOW, CLOSE, VOL
from ml.util import prepare_raw_data
from util.util import iterate_file_names

from constants import CATEGORIZE_SAMPLE_METHOD

def construct_binary_learning_sample(ticker, study_period):
    raw_data = prepare_raw_data(ticker)
    study_samples = []
    empty_sample = [0,0,0,0,0,0,0,0]
    for i in range(len(raw_data)-1):
        if CATEGORIZE_SAMPLE_METHOD(raw_data[0:i], raw_data[i+1:]):
            study_sample = []
            if i < study_period:
                study_sample = raw_data[0:i]
                while len(study_sample) < study_period:
                    study_sample.insert(0,empty_sample)
            else:
                study_sample = raw_data[i-study_period+1:i]
            study_samples.append(study_sample)
    return study_samples


def combine_binary_study_samples(key_ticker, study_period, checking_condition):
    total_study_samples = []
    for ticker in iterate_file_names():
        if checking_condition(key_ticker, ticker):
            total_study_samples += construct_binary_learning_sample(ticker, study_period)
    return total_study_samples

def construct_testing_sample(ticker, study_period):
    raw_data = prepare_raw_data(ticker)
    empty_sample = [0,0,0,0,0,0,0,0]
    if len(raw_data) < study_period:
        test_sample = raw_data
        while len(test_sample) < study_period:
                test_sample.insert(0,empty_sample)
    return test_sample


