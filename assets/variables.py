# Define path to tessaract.exe
tesseractPath = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define path to image
# imgPath = 'jpgFiles/1.PNG'  # Oldest

# imgPath = 'jpgFiles/' + str(i) + '.PNG'
# wordPath = 'wordFiles/' + str(i) + '.docx'
# pdfPath = 'pdfFiles/' + str(i) + '.pdf'

imgPath = []
wordPath = []
pdfPath = []


for i in range(1, 4):
    pattern = str(i)
    imgPath.append('jpgFiles/' + pattern + '.PNG')
    wordPath.append('wordFiles/' + pattern + '.docx')
    pdfPath.append('pdfFiles/' + pattern + '.pdf')
