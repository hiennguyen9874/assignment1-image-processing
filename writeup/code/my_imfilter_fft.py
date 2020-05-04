kernel_row, kernel_col = kernel.shape
if (kernel_row % 2 == 0) or (kernel_col % 2 == 0):
    raise Exception('Kernel is not of odd dimensions')

color_channel = []
num_channel = 1
if len(image.shape) == 2:
    # grayscale image
    color_channel.append(image)
elif len(image.shape) == 3:
    # RGB image
    num_channel = image.shape[2]
    for i in range(image.shape[2]):
        color_channel.append(image[:, :, i])
else:
    return

h = kernel_row//2
w = kernel_col//2

for i in range(num_channel):
    channel_size = np.array(color_channel[i].shape)
    kernel_size = np.array(kernel.shape)
    size = channel_size + kernel_size - 1
    fsize = np.array([np.max(size), np.max(size)])

    channel_fft = np.fft.fft2(color_channel[i], fsize)
    kernel_fft = np.fft.fft2(kernel, fsize)
    color_channel[i] = (np.real(np.fft.ifft2(channel_fft*kernel_fft)))[h:channel_size[0] + h, h:channel_size[1] + h]

if num_channel == 1:
    filtered_image = color_channel[0]
else:
    filtered_image = np.stack(color_channel, axis=2)