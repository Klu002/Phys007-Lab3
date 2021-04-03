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

def calculate_period(df):
    peak_times = get_peaks(df).Time.values
    periods = []
    for i in range(len(peak_times) - 1):
        periods.append(peak_times[i + 1] - peak_times[i])
    periods = filter(lambda x: x > 0.3, periods)
    periods = list(periods)
    return np.average(periods[2:10]), periods[2:10]

def print_stats(file):
    print("==="+file+"===")
    averages = []
    periods = []
    for i in range(1, 4):
        # Might have to change file path to /Data/
        df = get_accelerometer_info('Phys007-Lab3/Data/' + file + str(i) + '.csv')
        avg, period = calculate_period(df)
        averages.append(avg)
        periods = periods + period

    print(averages)
    print("avg: " + str(np.average(averages)))
    print("stddev: " + str(np.std(periods)))

if __name__ == '__main__':
    print_stats("longheavy")
    print_stats("longlight")
    print_stats("shortheavy")
    print_stats("shortlight")

