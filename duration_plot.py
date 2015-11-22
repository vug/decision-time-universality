import matplotlib.pyplot as plt
import numpy as np

fp = open("sample/durations.txt", "rt")
lines = fp.readlines()
fp.close()

durations = [float(line.split(' ')[0]) for line in lines]
durations = np.asarray(durations)


normalized = (durations-np.mean(durations))/np.std(durations)

bins = np.arange(np.min(normalized), np.max(normalized), 0.36)
c, b = np.histogram(normalized, bins, density=True)
plt.step(b[:-1], c, where='mid', lw=2)
plt.xlabel('normalized duration')
plt.ylabel('frequency')
plt.title('distribution of normalized search durations')
#plt.savefig('distribution2.png')
plt.show()