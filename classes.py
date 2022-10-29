import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract

class Osoznanie():
    def __init__(self, image):
        self.image = cv2.imread(str(image))
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'



    def __str__(self):
        string = pytesseract.image_to_string(self.image, lang= 'rus')
        return string


    def fail_funcs(self, nazvanie):
        string = pytesseract.image_to_string(self.image, lang='rus')
        try:
            with open(str(nazvanie + ".txt"), "w") as file:
                file.write(string)
                return f"файл успешно создан! Имя файла {str(nazvanie)}"
        except:
            return "Неизвестная ошибка"

    def no_fail_funcs(self):
        string = pytesseract.image_to_string(self.image, lang='rus')
        try:
            with open("text.txt", "w") as file:
                file.write(str(string))
                return f"файл успешно создан! Имя файла text"
        except:
            return "Неизвестная ошибка"



    def skolcko_slov(self, text):
        string = pytesseract.image_to_string(self.image, lang='rus')
        a = 0

        for i in str(string):
            if str(i) == str(text):
                a=+1
        if a == 0:
            return "Нет слов"
        else:
            return f"Слово {str(text)} встречается {str(a)}"


    def naidem(self):
        pass






