# JPG to PDF converter

> A framework made for converting an image file to PDF file.  
> Usage of just 4 packages of Python.  


# Working

> 1. First, this will seacrh for the text inside the image file(most probably .jpg/.PNG file).  
> 2. Then, it'll fetch the text & store it in a variable.  
> 3. And then, writes it into a docx file(So that if it extracts wrong text, you can manually type the correct text).  
> 4. And finally, convert the word file hence created into a pdf file.  


# Requirements

1. You need to download [tesseract](https://github.com/UB-Mannheim/tesseract/wiki).  
2. You need following packages of python:
   1. PIL
   2. pytesseract
   3. docx
   4. docx2pdf
3. IDLE (PyCharm Community Edition preferrable)  


# How to run

1. Go to [main](main.py) file.  
2. Just check the following lines in the code:

```commandline
text = extractTextFromImg(imgPath) # - extract text from image file
appendDataToWord(wordPath, text) # - append data into word file
convertDocxToPdf(wordPath, pdfPath) # - convert it into pdf
```

3. You don't need to change anything in this file. The changes which you need to make is in [variables](assets/variables.py) file.  
4. Just change the value of following 4 variables:
   1. ```tesseractPath # the tesseract path you just downloaded. The one written in the file is default path```  
   2. ```wordPath # the word file path. Put the word file path under wordFiles directory for better readability```  
   3. ```pdfPath # the pdf file path. Put the pdf file path under pdfFiles directory for better readability```  


# Author


|                                                                                                                                                                                                         <a href="https://nitin-kr.onrender.com/"><img src="https://github.com/nitinkumar30/nitscv/blob/main/image/nitin-1.jpg" width="150px " height="150px" /></a>                                                                                                                                                                                                          |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                                                                                                                                                                                                                                                                 **[Nitin Kumar](https://nitin-kr.onrender.com/)**                                                                                                                                                                                                                                                                  |
| <a href="https://twitter.com/nitinkumar30"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/twitter.png" width="32px" height="32px"></a> <a href="https://www.facebook.com/b1AcK6AG16"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/facebook.png" width="32px" height="32px"></a> <a href="https://www.linkedin.com/in/nitin30kumar/"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/linkedin.png" width="32px" height="32px"></a> |


