import numpy as np

def calc_integral_image(img):
    cumulative_sum = np.zeros(img.shape)
    
    for row in range(len(img)):
        for col in range(len(img[row])):
            if row == 0 and col == 0:
                cumulative_sum[row][col] = img[row][col]
            elif row == 0:
                cumulative_sum[row][col] = cumulative_sum[row][col-1] + img[row][col]
            elif col == 0:
                cumulative_sum[row][col] = cumulative_sum[row-1][col] + img[row][col]
            else:
                cumulative_sum[row][col] = (cumulative_sum[row-1][col] + cumulative_sum[row][col-1] - cumulative_sum[row-1][col-1]) + img[row][col]

    return cumulative_sum


