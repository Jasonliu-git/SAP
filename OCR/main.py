import pytesseract
from PIL import Image
# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r' C:\Users\twg01789\AppData\Local\Programs\Tesseract-OCR\tesseract.exe
'  # Update this path based on your installation
# Path to the image file
image_path = 'path_to_your_image.jpg'
# Open the image using Pillow
image = Image.open(image_path)
# Perform OCR using pytesseract
# Specify the language as Chinese Traditional (chi_tra)
text = pytesseract.image_to_string(image, lang='chi_tra')
print(text)
