__author__ = 'yingbozhan'


#all data ranged from smaller date to larger date.
#the larger the date, the closer to today

from constants.constants import CLOSE, HIGH, OPEN, LOW, VOL
def hit_high_value(known_data, future_data):
    next_data = future_data[0]
    prev_data = known_data[-1]
    if next_data[CLOSE]/prev_data[CLOSE] > 1.09:
        return True
    else:
        return False

