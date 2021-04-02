import csv
import pandas as pd
from IPython.display import display
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt
import math

def get_accelerometer_info(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = []
        next(csv_reader)
        for row in csv_reader:
            data_row = {'Gyroscopey': float(row[2]), 'Time': float(row[0])}
            data.append(data_row)
        df = pd.DataFrame(data)
    return df


def get_peaks(df):
    peaks, _ = find_peaks(df.Gyroscopey, height=0)
    return df.iloc[peaks]

def calculate_first_period(df):
    peak_times = get_peaks(df).Time.values
    periods = []
    for i in range(len(peak_times) - 1):
        periods.append(peak_times[i + 1] - peak_times[i])
    periods = filter(lambda x: x > 0.3, periods)
    periods = list(periods)
    return periods[2]

def print_stats(file):
    print("==="+file+"===")
    long_heavy = []
    for i in range(1, 4):
        df = get_accelerometer_info('Data/' + file + str(i) + '.csv')
        long_heavy.append(calculate_first_period(df))
    print(long_heavy)
    print("avg: " + str(np.average(long_heavy)))
    print("stddev: " + str(np.std(long_heavy)))

if __name__ == '__main__':
    print_stats("longheavy")
    print_stats("longlight")
    print_stats("shortheavy")
    print_stats("shortlight")

