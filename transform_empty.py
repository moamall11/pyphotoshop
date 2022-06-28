"""
Python Image Manipulation Empty Template by Kylie Ying (modified from MIT 6.865)

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

from image import Image
import numpy as np

def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)

    #get the attributes of the original image.
    x_pixels,y_pixels,channel_num = image.array.shape
    #make a new image with the same attributes as the original.
    new_im = Image(x_pixels,y_pixels,channel_num)
    #let the new image be just like the original image but with increased/decreased brightness.
    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(channel_num):
    #             new_im.array[x,y,c] = image.array[x,y,c] * factor
    new_im.array = image.array * factor
    return new_im


def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    x_pixels,y_pixels,channel_num = image.array.shape
    new_im = Image(x_pixels,y_pixels,channel_num)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(channel_num):
                new_im.array[x,y,c] = (image.array[x,y,c] - mid) * factor + mid
    return new_im

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels,y_pixels,channel_num = image.array.shape
    new_im = Image(x_pixels,y_pixels,channel_num)
    
    blur_range = kernel_size // 2

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(channel_num):
                total = 0
                for x_i in range(max(0,x - blur_range),min(new_im.x_pixels,x + blur_range +1)):
                    for y_i in range(max(0,y - blur_range),min(new_im.y_pixels,y + blur_range +1)):
                        total += image.array[x_i,y_i,c]
                new_im.array[x,y,c] = total / (kernel_size ** 2)
    return new_im


def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    x_pixels,y_pixels,channel_num = image.array.shape
    new_im = Image(x_pixels,y_pixels,channel_num)

    kernel_size = kernel.shape[0]
    blur_range = kernel_size // 2

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(channel_num):
                total = 0
                for x_i in range(max(0,x - blur_range),min(new_im.x_pixels,x + blur_range +1)):
                    for y_i in range(max(0,y - blur_range),min(new_im.y_pixels,y + blur_range +1)):
                        x_k = x_i + blur_range - x
                        y_k = y_i + blur_range - y
                        kernel_val = kernel[x_k,y_k]
                        total += image.array[x_i,y_i,c] * kernel_val
                new_im.array[x,y,c] = total
    return new_im

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    x_pixels,y_pixels,channel_num = image1.array.shape
    new_im = Image(x_pixels,y_pixels,channel_num)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(channel_num):
                new_im.array[x,y,c] = (image1.array[x,y,c] ** 2 + image2.array[x,y,c] ** 2) ** 0.5
    return new_im
    
if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')
    # # brighten the image.
    # brightened_im = brighten(lake,1.7)
    # # write it.
    # brightened_im.write_image('brightened_lake.png')

    # darkened_im = brighten(lake,0.3)
    # darkened_im.write_image('darkened_lake.png')

    # #increase the contrast of the image.
    # incr_contrast = adjust_contrast(lake,1.7,0.5)
    # incr_contrast.write_image('incr_contrast_lake.png')
    # #decrease the contrast of the image.
    # decr_contrast = adjust_contrast(lake,0.3,0.5)
    # decr_contrast.write_image('decr_contrast_lake.png')
    
    # blurred_im = blur(city,3)
    # blurred_im.write_image('blurred_city_3.png')

    # blurred_im = blur(city,15)
    # blurred_im.write_image('blurred_city_15.png')

    # edge_x_im=apply_kernel(city,np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]))
    # edge_x_im.write_image('edge_x.png')
    # edge_y_im=apply_kernel(city,np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]))
    # edge_y_im.write_image('edge_y.png')

    # edge_xy_im = combine_images(edge_x_im,edge_y_im)
    # edge_xy_im.write_image('edge_xy.png')
