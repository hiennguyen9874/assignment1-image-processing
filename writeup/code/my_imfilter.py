rotate_kernel = np.flip(kernel)

kernel_row, kernel_col = rotate_kernel.shape

if (kernel_row % 2 == 0) or (kernel_col % 2 == 0):
    raise Exception('Kernel is not of odd dimensions')

color_channel = []
num_channel = 1
if len(image.shape) == 2:
    
    color_channel.append(image)
elif len(image.shape) == 3:
    
    num_channel = image.shape[2]
    for i in range(image.shape[2]):
        color_channel.append(image[:, :, i])
else:
    return

padding_row = kernel_row//2
padding_col = kernel_col//2

for i in range(num_channel):
    channel = color_channel[i]
    result = np.zeros(channel.shape, dtype=np.float32)
    
    channel_padded = np.pad(
        channel, [(padding_row, padding_row), (padding_col, padding_col)], mode='constant')
    for col in range(channel.shape[1]):
        for row in range(channel.shape[0]):
            
            result[row, col] = (
                rotate_kernel * channel_padded[row: row + kernel_row, col: col + kernel_col]).sum()
    color_channel[i] = result


if num_channel == 1:
    filtered_image = color_channel[0]
else:
    filtered_image = np.stack(color_channel, axis=2)