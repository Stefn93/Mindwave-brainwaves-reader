import numpy as np

from keras.layers import LSTM


dataset=np.genfromtxt('ioio.csv',delimiter=',',dtype=np.int32)


dataset = np.genfromtxt('ioio.csv',delimiter=',',dtype=np.int32)


def calculate_max_sequence_length(dataset):
    max_seq_length = 0
    cur_seq_length = 0
    current_output = dataset[0][-4:]
    seqs = 1
    for row in dataset:
        o=row[-4:]
        if not np.array_equal(o, current_output):
            seqs += 1
            if cur_seq_length > max_seq_length:

                max_seq_length = cur_seq_length
            current_output = o
            cur_seq_length = 1
        else:
            cur_seq_length += 1
    return max_seq_length, seqs


def create_array_task(dataset):
    current_output = dataset[0][-4:]
    array_task = []
    line = 0
    i = 0
    for row in dataset:
        o = row[-4:]
        line += 1
        if not np.array_equal(o, current_output):
            array_task[i] = line
            i += 1
    return array_task

print(calculate_max_sequence_length(dataset))

"""
It builds the network, defining its structure
"""
print(create_array_task(dataset))
