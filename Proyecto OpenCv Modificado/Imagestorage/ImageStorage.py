import cv2
import re

class ImageStorage:

    @staticmethod
    def read_image(path_img):
        """Leer una imagen desde el disco y devolver in objeto imagen"""
        if isinstance(path_img, str):
            try:
                img = cv2.imread(path_img)
                return img
            except:
                print("formato no valido")
            

    @staticmethod
    def save_img(img, name_img):
        # write image on disk
        # escribir validador de string, regex, validar que un string termine en jpg
        name_img = name_img + ".jpg"
        if re.search('jpg$',name_img):
            print("El archivo es de formato jpg")
        else:
            print("El archivo no tiene extension jpg")        
        cv2.imwrite(name_img, img)


