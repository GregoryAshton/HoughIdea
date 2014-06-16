import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
y = np.array([2,5,7,9,10,13,16,18,21,22,21,20,19,18,17,14,10,9,7,5,7,9,10,12,13,15,16,17,22,27])

def Linear(x, m, c):
    return m*x + c

def GetMaximum(array):
    i, j = np.unravel_index(array.argmax(), array.shape)
    return i, j

def GetMCArray(x, y, m, c, threshold=2):
    """ Returns the Hough transformed array of x, y data

    Parameters
    ----------
    x : array_like 
        The x data of length *n*
    y : array_like
        The y data of length *n*
    m : array_like
        1Dcarray of gradient values 
    c : array_like
        1D array of c values

    Returns
    -------
    bins : array, shape(n, len(m), len(c))

    """

    M, C = np.meshgrid(m, c, indexing="ij")
    bins = [] 
    for xval, yval in zip(x, y):
        residual = np.abs(yval - (M*xval + C))
        bins.append((residual < threshold).astype(int))

    bins = np.array(bins)
    return M, C, bins

def GetMCMaximums(bins, size):
    """ Return the indexes of the maximum values

    Parameters
    ----------
    bins : array, 

    size : int


    Returns
    -------
    i_idxs : array
        Indexes of the peaks in m
    j_idxs : array
        Indexes of the peaks in c
    """
    maxima = (bins_count == ndimage.maximum_filter(bins_count, 150))
    i_idxs, j_idxs = np.nonzero(maxima)

    return i_idxs, j_idxs

if __name__ == "__main__":

    nM, nC = 200, 201
    size = 10
    threshold = 1.0

    m = np.linspace(-5, 5, nM)
    c = np.linspace(-200, 100, nC)
    M, C, bins = GetMCArray(x, y, m, c, threshold=threshold)
    bins_count = bins.sum(axis=0)



    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8,4))

    ax1.plot(x, y)

    cplt = ax2.pcolormesh(M, C, bins_count)
    ax2.set_xlabel("m")
    ax2.set_ylabel("c")
    plt.colorbar(cplt)

    i_idxs, j_idxs = GetMCMaximums(bins, size=size)

    #if len(i_idxs) > 100:
    #    raise RuntimeError(" I don't want to plot {} fits".format(len(i_idxs)))

    for i, j in zip(i_idxs, j_idxs):
        x_fit = x[bins[:, i, j] == 1]
        ax1.plot(x_fit, m[i]*x_fit + c[j], alpha=0.8, color="r")

    plt.show()





