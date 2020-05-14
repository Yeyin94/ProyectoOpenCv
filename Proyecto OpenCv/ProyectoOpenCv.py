import cv2
from Gato.ImageStorage import ImageStorage
import re
class Converter:
	
	def img_to_gray_scale(img):
	    """Recibe un objeto imagen y devuleve la imagen en blanco y negro"""
	    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	    return gray_img

	if __name__ == '__main__':
	    img = ImageStorage.read_image("imagenes/GatoColor.jpg")
	    img_gray = img_to_gray_scale(img)
	    ImageStorage.save_img(img=img_gray, name_img="programando_hola_mundo")
	    print("La imagen ha sido convertida a escala de grises")

c = Converter()
