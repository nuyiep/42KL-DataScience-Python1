
from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def ft_zoom(np_image_array: np.array, image: str):
	'''Zoom image using slicing method'''
	np_after_slicing = np_image_array[400:, 400:, 1]
	print("New shape after slicing:")
	print(np.shape(np_after_slicing))
	print(np_after_slicing)
	# Display the zoomed image 
	plt.imshow(np_after_slicing)
	plt.title("Zoomed Image")
	plt.show()
	

def main():
	'''Main'''
	image = "animal.jpeg"
	np_image_array = ft_load(image)
	ft_zoom(np_image_array, image)
	
if __name__ == "__main__":
	main()
