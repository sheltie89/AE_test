import numpy as np 

def psnr(img_1, img_2, data_range=255):
    mse = np.mean((img_1.astype(float) - img_2.astype(float)) ** 2)
    return 10 * np.log10((data_range ** 2) / mse)
