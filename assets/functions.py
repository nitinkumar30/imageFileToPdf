from PIL import Image
from pytesseract import pytesseract
import docx
from docx2pdf import convert

from variables import *


# functions
# - extract text from image file
# - append data into word file
# - convert it into pdf

text = ''


def extractTextFromImg(imgPath):
    # Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = tesseractPath

    # Open image with PIL
    img = Image.open(imgPath)

    # Extract text from image
    text = pytesseract.image_to_string(img)

    return text
    # print(text)  # printing text extracted from image file


def appendDataToWord(wordPath, text):
    # open docx file
    my_doc = docx.Document()
    # write the above 'text' variable in the word file
    my_doc.add_paragraph(text)
    # save the docx file
    my_doc.save(wordPath)
    print(wordPath)


def convertDocxToPdf(wordPath, pdfPath):
    # convert the word into pdf file
    # input = 'wordFiles/1.docx'
    # output = 'pdfFiles/1_.pdf'
    convert(wordPath, pdfPath)
