import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import NullFormatter

def latency_plot(filename, maxvalue=None):
    data = np.genfromtxt(filename, delimiter='\n')
    data = data[np.logical_not(np.isnan(data))]

    if maxvalue is None:
        maxvalue = max(data)

    plt.figure()
    H = plt.hist(data, bins=np.linspace(0, maxvalue, 250), color='darkslategray')

    plt.xlabel("Latency (ms)")
    plt.ylabel("# of Occurrences")
    plt.title("Latency Histogram")
    x = data.max()/2
    y = H[0].max()/2

    meanval = np.round(np.mean(data), 5)
    meanfreq = np.round(1/meanval, 5)
    # plt.text(x, y, "Mean Value: " + str(meanval) + "\nMean Freq (Hz): " + str(meanfreq), horizontalalignment='center', verticalalignment='center')


def latency_plot_log(filename, maxvalue=None):

    data = np.genfromtxt(filename, delimiter='\n')
    data = data[np.logical_not(np.isnan(data))] # remove nan entries
    if maxvalue is None:
        maxvalue = max(data)

    data_range = (min(data), max(data))

    y = np.linspace(data_range[0], data_range[1], 10000)
    x = np.zeros(y.shape)
    for i, val in enumerate(y):
        x_mask = data <= val
        count = np.sum(x_mask)
        x[i] = count/data.size

    plt.figure()
    plt.title("Logit")
    # plt.ylim([0, 0.01])
    plt.xscale('logit')
    plt.plot(x, y, color='darkslategray')
    plt.gca().xaxis.set_minor_formatter(NullFormatter())

    plt.xlabel("Percentage of Transfers")
    plt.ylabel("Latency (ms)")


def throughput_plot(filename, maxvalue=None):
    data = np.genfromtxt(filename, delimiter='\n')
    data = data[np.logical_not(np.isnan(data))] # remove nan entries

    if maxvalue is None:
        maxvalue = max(data)

    plt.figure()

    H = plt.hist(data, bins=np.linspace(0, maxvalue, 1000), color='darkslategray')
    plt.xlabel("Latency (s)")
    plt.ylabel("# of Occurrences")
    plt.title("Throughput")
    x = np.max(data)/2
    y = H[0].max()/2

    meanval = np.round(np.mean(data), 5)
    meanfreq = np.round(1/meanval, 5)
    plt.text(x, y, "Mean Value: " + str(meanval) + "\nMean Freq (Hz): " + str(meanfreq), horizontalalignment='center', verticalalignment='center')


def throughput_plot_log(filename, maxvalue=None):

    data = np.genfromtxt(filename, delimiter='\n')
    data = data[np.logical_not(np.isnan(data))]  # remove nan entries
    if maxvalue is None:
        maxvalue = max(data)

    data_range = (min(data), max(data))

    y = np.linspace(data_range[0], data_range[1], 10000)
    x = np.zeros(y.shape)
    for i, val in enumerate(y):
        x_mask = data <= val
        count = np.sum(x_mask)
        x[i] = count/data.size

    plt.figure()
    plt.title("Throughput")
    plt.xscale('logit')
    plt.plot(x, y, color='darkslategray')
    plt.gca().xaxis.set_minor_formatter(NullFormatter())
    plt.xlabel("Percentage of Transfers")
    plt.ylabel("Time (s)")


def time_series_plot(filename, maxvalue=None):
    data = np.genfromtxt(filename, delimiter='\n')
    data = data[np.logical_not(np.isnan(data))]  # remove nan entries
    if maxvalue is None:
        maxvalue = max(data)

    x = np.cumsum(data)
    plt.figure()
    plt.title("Time Series")
    plt.plot(x, data, '.', markersize=2, color='darkslategray')
    plt.xlabel("Time (ms)")
    plt.ylabel("Latency (ms)")

    meanval = np.round(np.mean(data), 5)
    print("Average latency: " + str(meanval))


if __name__ == "__main__":

    filename = r"data\TCP_latency_test_60s_1m.txt"
    latency_plot(filename)
    latency_plot_log(filename)
    time_series_plot(filename)

    plt.show()

