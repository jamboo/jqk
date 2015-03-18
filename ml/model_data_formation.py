__author__ = 'yingbozhan'


def next_prev_ratio(data):
    sample = [[1,1,1,1,1,1,1,1]]
    prev = data[0]
    for i in range(1, len(data)):
        ratio = []
        next = data[i]
        for i in len(next):
            ratio.append(next[i]/prev[i])
        sample.append(ratio)
    return sample

