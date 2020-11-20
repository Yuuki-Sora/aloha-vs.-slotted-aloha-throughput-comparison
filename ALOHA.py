import numpy as np
import matplotlib.pyplot as plt

X = np.arange(0, 10, 0.01)
ALOHA = X * np.power(np.e, -2 * X)
S_ALOHA = X * np.power(np.e, -X)

plt.title("ALOHA vs. Slotted ALOHA Throughput Graph")
plt.xlabel("G - traffic load")
plt.ylabel("S - throughput")
plt.plot(X, S_ALOHA, label='Slotted ALOHA')
plt.plot(X, ALOHA, label='ALOHA')
plt.legend()
plt.annotate(
    'Upper limit (Slotted ALOHA): 37%', xy=(1.2, 1/np.e), xytext=(2.3, 1/np.e), c='royalblue',
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='royalblue')
)
plt.annotate(
    'Upper limit (ALOHA): 18%', xy=(0.7, 1/(2*np.e)), xytext=(1.8, 1/(2*np.e)), c='chocolate',
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='chocolate')
)
plt.xticks(np.arange(0, 11, 1))
plt.xlim([0, 10])
plt.ylim([0, 0.4])
plt.show()
