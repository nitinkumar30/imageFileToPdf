from assets.functions import *
from assets.variables import *

text = extractTextFromImg(imgPath)
appendDataToWord(wordPath, text)
convertDocxToPdf(wordPath, pdfPath)
