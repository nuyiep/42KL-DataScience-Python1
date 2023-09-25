
from PIL import Image
import numpy as np

def ft_load(path: str) -> np.array:
	'''
		Loads an image, prints its format, 
			  and its pixel content in RGB format
		Handles JPG and JPEG format
		Pillow treats JPEG and JPG as equivalent and uses 
		JPEG as the standard format name for JPEG images
	'''
	try:
		image = Image.open(path)
		image.show()
		image_format = image.format
		print("Image Format: ", image_format)
		np_image = np.array(image)
		print("The shape of image is:", np_image.shape)
		return (np_image)
	except Exception as e:
		print(f"{e}")
		return ("Error")
		exit
