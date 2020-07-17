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

    plt.figure(1)
    plt.xscale('logit')
    plt.plot(x, y)
    plt.gca().xaxis.set_minor_formatter(NullFormatter())


def throughput_plot(filename, maxvalue=None):
    data = np.genfromtxt(filename, delimiter=',')
    data = data[np.logical_not(np.isnan(data))] # remove nan entries

    if maxvalue is None:
        maxvalue = max(data)

    plt.figure()

    H = plt.hist(data, bins=np.linspace(0, maxvalue, 1000))
    plt.xlabel("Latency (s)")
    plt.ylabel("# of Occurrences")
    plt.title("Throughput of ESP32 Access Point Using One-Directional Communication")
    x = np.max(data)/2
    y = H[0].max()/2
    plt.text(x, y, "Mean Value: " + str(np.mean(data)), horizontalalignment='center', verticalalignment='center')


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

    plt.figure(1)
    plt.xscale('logit')
    plt.plot(x, y)
    plt.gca().xaxis.set_minor_formatter(NullFormatter())


if __name__ == "__main__":
    throughput_plot_log("throughput_test_16B_100s_1m.txt")
    latency_plot_log("latency_test_16B_100s_1m.txt")

    throughput_plot("throughput_test_16B_100s_1m.txt")
    latency_plot("latency_test_16B_100s_1m.txt")
    plt.show()

