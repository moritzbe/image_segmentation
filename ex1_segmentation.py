

# This exercise is all about counting stars.
# The goal is to know how many stars are in the image and what sizes they are.
# Problematic is only the moon.


import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

# plt.ion()
# plt.close('all')

# Load the respective image
img = plt.imread('stars.jpg')

# Sum up all color channels to get a grayscale image.
# use numpy function sum and sum along axis 2
# rescale the finale image to [0.0 1.0]

ims = img.sum(-1)
max_value = ims.max()
ims_rescaled = ims/max_value

# Now look at your image using imshow. Use vmin and vmax parameters in imshow 
#  to select an appropriate threshold.
plt.figure()
plt.imshow(ims_rescaled, vmin=0, vmax=1)


# You can set thresholds to cut the background noise
# Once you are sure you have all stars included use a binary threshold.

ims_bin = ims_rescaled
threshold = 0.1
ims_bin[ims_bin > threshold] = 1
ims_bin[ims_bin < threshold] = 0

# # (Tip: a threshold of 0.1 seemed to be good, but pick your own)
# # Now with the binary image use the opning and closing to 
# # bring the star to compacter format. Take care that no star connects to another
s1 = np.array([[1,1,1],[1,1,1],[1,1,1]])
ims2 = ndi.binary_closing(ims_bin, structure=s1)

# # repeat if necessary
# # remove isolated pixels around the moon with closing by a 2 pixel structure
s2 = np.array([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]])
ims3 = ndi.binary_opening(ims2,structure=s2)

# # play with all the morphological options in ndimage package to increase the quality
# # if still needed

# ims? = ndi.binary_??????(?????) # optional
 
# plotting the sum of all your binary images can help identify if you loose stars. 
# in principal every star is present in every binary image, so real stars have always 
# at least one pixel maximum

plt.figure(1)
plt.imshow(ims2 + ims3)

# # Once you're done, label your image with ndi.label.
im_lbld, num_stars = ndi.label(ims3)
plt.figure(2)
plt.imshow(im_lbld)

# # Use ndi.find_objects in the labeled to return a list of slices through the image for each star
slc_lst = ndi.find_objects(im_lbld)

# # you can have a look now at the individual stars. just apply the slice to your labelled array
starnum = 10
plt.figure(3)
plt.imshow(im_lbld[slc_lst[starnum]])

# # REMAINING task. Sum up each individual star to get a list of star brightnesses
# # make a detailed histogram (>100 bins). Take care to exclude the moon! 
# # This can be done by sorting the brightness array and remove the last element.

# # Remember: im_lbld[slc_lst[<number>]] selects one star. Create a list of star images with [0, 1].
# # Afterwards, sum their intensity up, and np.sort the sums.

# ????
# ????
# plt.figure(4)
# plt.hist(???, bins=100)

plt.show()
