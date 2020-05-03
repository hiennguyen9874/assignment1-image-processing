import sys
from scipy import signal

from scipy import linalg
import numpy as np

x = np.array([[1, 2, 3, 4, 5],
                    [10, 9, 8, 7, 6],
                    [11, 12, 13, 14, 15],
                    [21, 22, 23, 24, 25],
                    [16, 17, 18, 19, 20]])
y = np.array([[0, 1, 0],
                    [0, -2, 0],
                    [2, 0, -1]])

# print(signal.convolve2d(x , y , 'full'))

s1 = np.array(x.shape)
s2 = np.array(y.shape)

size = s1 + s2 - 1


fsize = 2 ** np.ceil(np.log2(size)).astype(int)
fslice = tuple([slice(0, int(sz)) for sz in size])


new_x = np.fft.fft2(x , fsize)


new_y = np.fft.fft2(y , fsize)
result = np.fft.ifft2(new_x*new_y)[fslice].copy()

print(np.array(result.real , np.int32))
print(signal.convolve2d(x , y , 'same'))
print(np.array(signal.fftconvolve(x,y, ) , np.int32))