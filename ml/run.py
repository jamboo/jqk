__author__ = 'yingbozhan'

import constants
import categorize_sample_methods
import construct_model
import model_data_formation
from pre_model_data_process import combine_binary_study_samples, construct_testing_sample


constants.CATEGORIZE_SAMPLE_METHOD = categorize_sample_methods.hit_high_value
constants.MODEL_METHOD = construct_model.m_nearest_centroid
constants.DATA_MODEL_FORMATION_METHOD = model_data_formation.next_prev_ratio
ticker = None

def f():return True

study_samples = combine_binary_study_samples(ticker,30, f)
test_sample = construct_testing_sample(ticker, 30)
data = constants.DATA_MODEL_FORMATION_METHOD(study_samples)
test_data = constants.DATA_MODEL_FORMATION_METHOD(test_sample)
constants.MODEL_METHOD(data,[1 for i in range(len(data))], test_data)


