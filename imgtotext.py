import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def imgtxt(name):
    img = Image.open(name)
    text = pytesseract.image_to_string(img,lang='rus')
    return text


