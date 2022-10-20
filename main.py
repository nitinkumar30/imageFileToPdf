from assets.functions import *
from assets.variables import *


for i, j, k in zip(imgPath, wordPath, pdfPath):
    text = extractTextFromImg(i)
    appendDataToWord(j, text)
    convertDocxToPdf(j, k)
