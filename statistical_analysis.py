import numpy as np


response_times = np.array([25, 30, 28, 35, 40, 32, 29, 31, 45, 50])


mean = np.mean(response_times)
print("Mean:", mean)


median = np.median(response_times)
print("Median:", median)


std_dev = np.std(response_times)
print("Standard Deviation:", round(std_dev, 2))


if std_dev > 10:
    print("Response times show considerable variation.")
else:
    print("Response times do not show considerable variation.")
