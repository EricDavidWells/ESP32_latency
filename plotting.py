import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import NullFormatter  # useful for `logit` scale


def latency_plot(filename, maxvalue=None):
    data = np.genfromtxt(filename, delimiter=',')
    data = data[np.logical_not(np.isnan(data))]

    if maxvalue is None:
        maxvalue = max(data)

    plt.figure()
    H = plt.hist(data, bins=np.linspace(0, maxvalue, 1000))
    plt.xlabel("Latency (s)")
    plt.ylabel("# of Occurrences")
    plt.title("Latency of ESP32 Access Point Using Handshake Bi-Directional Communication")
    x = data.max()/2
    y = H[0].max()/2
    plt.text(x, y, "Mean Value: " + str(np.mean(data)), horizontalalignment='center', verticalalignment='center')


def latency_plot_log(filename, maxvalue=None):

    data = np.genfromtxt(filename, delimiter=',')
    data = data[np.logical_not(np.isnan(data))] # remove nan entries
    if maxvalue is None:
        maxvalue = max(data)

    # print(len(data))
    # print(sum(data))
    data_range = (min(data), max(data))

    y = np.linspace(data_range[0], data_range[1], 10000)
    x = np.zeros(y.shape)
    for i, val in enumerate(y):
        x_mask = data <= val
        count = np.sum(x_mask)
        x[i] = count/data.size

    plt.figure()
    plt.title("Latency (ESP32 Handshake)")
    plt.xscale('logit')
    plt.plot(x, y)
    plt.gca().xaxis.set_minor_formatter(NullFormatter())

    plt.xlabel("Percentage of Transfers")
    plt.ylabel("Time (s)")
    # plt.text(x, y, "Mean Value: " + str(np.mean(data)), horizontalalignment='center', verticalalignment='center')


def throughput_plot(filename, maxvalue=None):
    data = np.genfromtxt(filename, delimiter=',')
    data = data[np.logical_not(np.isnan(data))] # remove nan entries

    if maxvalue is None:
        maxvalue = max(data)

    plt.figure()

    H = plt.hist(data, bins=np.linspace(0, maxvalue, 1000))
    plt.xlabel("Latency (s)")
    plt.ylabel("# of Occurrences")
    plt.title("Throughput")
    x = np.max(data)/2
    y = H[0].max()/2

    meanval = np.round(np.mean(data), 5)
    meanfreq = np.round(1/meanval, 5)
    plt.text(x, y, "Mean Value: " + str(meanval) + "\nMean Freq (Hz): " + str(meanfreq), horizontalalignment='center', verticalalignment='center')


def throughput_plot_log(filename, maxvalue=None):

    data = np.genfromtxt(filename, delimiter=',')
    data = data[np.logical_not(np.isnan(data))]  # remove nan entries
    if maxvalue is None:
        maxvalue = max(data)

    # print(len(data))
    # print(sum(data))
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
    plt.plot(x, y)
    plt.gca().xaxis.set_minor_formatter(NullFormatter())
    plt.xlabel("Percentage of Transfers")
    plt.ylabel("Time (s)")


def time_series_plot(filename, maxvalue=None):
    data = np.genfromtxt(filename, delimiter=',')
    data = data[np.logical_not(np.isnan(data))]  # remove nan entries
    if maxvalue is None:
        maxvalue = max(data)

    x = np.cumsum(data)
    plt.figure()
    plt.title("Time Series")
    plt.plot(x, data)
    plt.xlabel("Time (s)")
    plt.ylabel("Latency (s)")


if __name__ == "__main__":

    # filename = r"data\2020-07-26_TCP_throughput_test_100s_5m.txt"
    # filename = r"data\throughput_test_16B_100s_1m.txt"
    filename = r"data\2020-07-27_UDP_throughput_test_100s_16buf_2m.txt"

    throughput_plot(filename)
    throughput_plot_log(filename)
    time_series_plot(filename)
    # latency_plot_log("latency_test_16B_100s_1m.txt")

    # throughput_plot("throughput_test_16B_100s_1m.txt")
    # latency_plot("latency_test_16B_100s_1m.txt")
    plt.show()

