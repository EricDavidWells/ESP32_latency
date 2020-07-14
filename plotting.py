import numpy as np
from matplotlib import pyplot as plt


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


def throughput_plot(filename, maxvalue=None):
    data = np.genfromtxt(filename, delimiter=',')
    data = data[np.logical_not(np.isnan(data))] # remove nan entries

    if maxvalue is None:
        maxvalue = max(data)

    print(maxvalue)

    plt.figure()

    H = plt.hist(data, bins=np.linspace(0, maxvalue, 1000))
    plt.xlabel("Latency (s)")
    plt.ylabel("# of Occurrences")
    plt.title("Throughput of ESP32 Access Point Using One-Directional Communication")
    x = np.max(data)/2
    y = H[0].max()/2
    plt.text(x, y, "Mean Value: " + str(np.mean(data)), horizontalalignment='center', verticalalignment='center')


if __name__ == "__main__":
    maxvalue =  latency_plot("latency_test_16B_100s_1m.txt")
    throughput_plot("throughput_test_16B_100s_1m.txt")
    plt.show()

