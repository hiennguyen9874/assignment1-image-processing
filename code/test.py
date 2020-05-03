import numpy as np
from numpy import pi, exp, sqrt
from helpers import vis_hybrid_image, load_image, save_image
from scipy.signal import convolve2d, correlate2d, convolve
from student import my_imfilter, my_imfilter_fft


# cutoff_frequency = 7
# s, k = cutoff_frequency, cutoff_frequency*2
# probs = np.asarray([exp(-z*z/(2*s*s))/sqrt(2*pi*s*s)
#                     for z in range(-k, k+1)], dtype=np.float32)
# kernel = np.outer(probs, probs)
# image1 = load_image('../data/01_dog.bmp')

# low_frequencies = my_imfilter(image1, kernel)
# low_frequencies1 = convolve(image1, np.array([kernel, kernel, kernel]), mode = 'same')
# low_frequencies2 = my_imfilter_fft(image1, kernel)
# print(np.subtract(low_frequencies1, low_frequencies2))
# # print(low_frequencies2)

image = np.array([[1, 2, 3, 4, 5],
                    [10, 9, 8, 7, 6],
                    [11, 12, 13, 14, 15],
                    [21, 22, 23, 24, 25],
                    [16, 17, 18, 19, 20]])
kernel = np.array([[0, 1, 0],
                    [0, -2, 0],
                    [2, 0, -1]])
print(my_imfilter(image, kernel))
print(my_imfilter_fft(image, kernel))
print(convolve2d(image, kernel, mode = 'same'))