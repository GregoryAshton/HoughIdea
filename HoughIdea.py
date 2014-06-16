import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
y = np.array([2,5,7,9,10,13,16,18,21,22,21,20,19,18,17,14,10,9,7,5,7,9,10,12,13,15,16,17,22,27])

def Linear(x, m, c):
    return m*x + c

def GetMaximum(array):
    i, j = np.unravel_index(array.argmax(), array.shape)
    return i, j

nM, nC = 500, 510
m = np.linspace(-2, 4, nM)
c = np.linspace(-35, 15, nC)

M, C = np.meshgrid(m, c)

bins = [] 
threshold = 1.0
for xval, yval in zip(x, y):
    residual = np.abs(yval - (M*xval + C))
    bins.append((residual < threshold).astype(int))

bins = np.array(bins)
bins_count = bins.sum(axis=0)
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8,4))

ax1.plot(x, y)

cplt = ax2.pcolormesh(M, C, bins_count)
ax2.set_xlabel("m")
ax2.set_ylabel("c")
plt.colorbar(cplt)

i, j = GetMaximum(bins_count)
x_fit = x[bins[:, i, j] == 1]
ax1.plot(x_fit, M[i, j]*x_fit + C[i, j])

plt.show()


plt.show()
