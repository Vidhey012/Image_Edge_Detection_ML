from helper_functions import *

#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "./images/"
imgpath = datafolder + "1.jpg" 
#----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
#----------------------------------------WRITE YOUR CODE HERE----------------------------------------
# Create a data structure to store updated pixel information

new_pixel_values =[[0]*numb_colns for _ in range(numb_rows)]

# Define the 3 x 3 mask as a tuple of tuples
mask = [[-1,-1,-1], [-1,8,-1], [-1,-1,-1]]

# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(pixel_values,i,j):
    rw_start=i
    rw_end=i+2
    cl_start=j
    cl_end=j+2
    return [[pixel_values[i][j] for j in range(cl_start,cl_end+1)] for i in range(rw_start,rw_end+1)]

# Implement a function to flatten a 2D list or a 2D tuple
def flatten(pixel_values):
    return [pixel_values[i][j] for i in range(len(pixel_values)) for j in range(len(pixel_values[i]))]

# For each of the pixel values, excluding the boundary values
for i in range(numb_rows):
    for j in range(numb_colns):        
        # Create little local 3x3 box using list slicing
        neighbour_pixels = flatten(get_slice_2d_list(pixel_values,i,j))
        mask_new=flatten(mask)
        # Apply the mask
        mult_result = map(lambda p,q:p*q, neighbour_pixels, mask_new)        
    # Sum all the multiplied values and set the new pixel value
        sum=0
        for x in mult_result:
            sum+=x
        new_pixel_values[i][j]=sum
        
        
        
#        
#----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)