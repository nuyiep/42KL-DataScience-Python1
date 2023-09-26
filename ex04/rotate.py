
from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 1. plt.imshow()- expects input data to be 2D array (grayscale image)
#					or 3D array (RGB image) with specific shapes
# 				- for grayscale image: (height, width)
#				- for RGB image: (height, width, 3) 3 represents the color channels (Red, Green, Blue)
#
def ft_rotate(np_zoomed_image_array: np.array):
	'''Reshape'''
	"""Rotate using customized transpose function"""
	rotated_image = np.rot90(np_zoomed_image_array, k = 1)
	plt.imshow(rotated_image)
	plt.title("Transposed Image")
	plt.show()

def ft_zoom(np_image_array: np.array, path: str) -> np.array:
	'''Zoom image using slicing method'''
	np_after_slicing = np_image_array[100:500, 400:800, 0:1] #[y-axis, x-axis]
	print("New shape after slicing:")
	print(np.shape(np_after_slicing))
	print(np_after_slicing)
	# Display the zoomed image 
	# plt.imshow(np_after_slicing)
	# plt.title("Zoomed Image")
	# plt.show()
	return (np_after_slicing)

def main():
	'''Main'''
	path = "animal.jpeg"
	np_image_array = ft_load(path)
	np_zoomed_image_array = ft_zoom(np_image_array, path)
	ft_rotate(np_zoomed_image_array)

if __name__ == "__main__":
	main()
