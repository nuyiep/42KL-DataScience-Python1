
from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 1. plt.imshow()- expects input data to be 2D array (grayscale image)
#					or 3D array (RGB image) with specific shapes
# 				- for grayscale image: (height, width)- 1 channel
#				- for RGB image: (height, width, 3) 3 represents the color channels (Red, Green, Blue)
#
def ft_rotate(np_zoomed_image_array: np.array):
	'''Transpose the image'''
	height, width, channels = np_zoomed_image_array.shape
	rotated_data = np.zeros((width, height, channels), dtype=np.uint8) 
	#data type uint8- typically used for image data
	for x in range(width):
		for y in range(height):
			rotated_data[x, y, :] = np_zoomed_image_array[y, x, :] 
			#swap x and y coordinates= transpose
	print("New shape after Transpose:", end='')
	print(np.shape(rotated_data))
	print(rotated_data)
	plt.imshow(rotated_data)
	plt.title("Transposed Image")
	plt.show()

def ft_zoom(np_image_array: np.array, path: str) -> np.array:
	'''Zoom image using slicing method'''
	np_after_slicing = np_image_array[100:500, 400:800, 0:1] #[y-axis, x-axis]
	print("The shape of image is: ", end='')
	print(np.shape(np_after_slicing))
	print(np_after_slicing)
	return (np_after_slicing)

def main():
	'''Main'''
	path = "../animal.jpeg"
	np_image_array = ft_load(path)
	np_zoomed_image_array = ft_zoom(np_image_array, path)
	ft_rotate(np_zoomed_image_array)

if __name__ == "__main__":
	main()
