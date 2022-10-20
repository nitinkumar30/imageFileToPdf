from PIL import Image
from pytesseract import pytesseract
import docx
from docx2pdf import convert

# Define path to tessaract.exe
tesseractPath = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define path to image
# i = 0
# imgPath = 'jpgFiles/1.PNG'
# imgPath = 'jpgFiles/' + str(i) + '.PNG'
# wordPath = 'wordFiles/' + str(i) + '.docx'
# pdfPath = 'pdfFiles/' + str(i) + '.pdf'

from assets.variables import *

# Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = tesseractPath

for i, j, k in zip(imgPath, wordPath, pdfPath):
    # Open image with PIL
    print('\n\n', i, j, k)
    img = Image.open(i)

    # Extract text from image
    text = pytesseract.image_to_string(img)

    # open docx file
    my_doc = docx.Document()
    # write the above 'text' variable in the word file
    my_doc.add_paragraph(text)
    # save the docx file
    my_doc.save(j)
    print(j)

    convert(j, k)
