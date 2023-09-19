from pathlib import Path
from skimage import io
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def read_colorimg(imgpath):
    # Read the color image from the path
    color_img = mpimg.imread(imgpath)
    # Convert the color to grayscale using the average method
    gray_img = np.dot(color_img[...,:3], [0.33, 0.33, 0.33])
    # Save the color image as a grayscale image, if you want
    # io.imsave('gray.png', gray_pixels.astype(np.uint8))
    # Pad the image with boundary zeroes
    padded_img = np.pad(gray_img, (1,), 'constant', constant_values=0)
    # Convert the pixel data to a list and return
    return padded_img[:, :].tolist()

def verify_result(pixel_values, new_pixel_values, mask):
    # Create the original image array from the list
    orig_image = np.asarray(pixel_values)[1:-1,1:-1]
    edges_image = np.asarray(new_pixel_values)
    # Find the correct answer using convolve(). Reverse the mask when passing to convolve() 
    correct_edges_image = ndimage.convolve(orig_image, np.array(mask)[::-1, ::-1], mode='constant', cval=0)
    # Compare each updated value against the correct answer 
    comparison = edges_image == correct_edges_image
    print(f"{comparison.all()} result")

def view_images(imgpath, new_pixel_values):
    orig_image = mpimg.imread(imgpath)
    edges_image = np.asarray(new_pixel_values)

    plt.rcParams['font.size'] = 30
    plt.rcParams['axes.titlepad'] = 20 
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    ax = axes.ravel()
    ax[0].imshow(orig_image)
    ax[0].set_title("Input image")
    ax[1].imshow(edges_image, cmap='gray', vmin = 0, vmax = 255)
    ax[1].set_title("Edges of the image")
    plt.show() 