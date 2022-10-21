# JPG to PDF converter

> A framework made for converting an image file to PDF file.  
> Usage of just 4 packages of Python.  


# Working

> 1. First, this will search for the text inside the image file(most probably .jpg/.PNG file).  
> 2. Then, it'll fetch the text & store it in a variable.  
> 3. And then, writes it into a docx file(So that if it extracts wrong text, you can manually type the correct text).  
> 4. And finally, convert the word file hence created into a pdf file.  



https://user-images.githubusercontent.com/40369168/197052863-ef98f8ee-fd87-403b-95f0-3c7139971bdb.mp4





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
text = extractTextFromImg(i) # - extract text from image file
appendDataToWord(j, text) # - append data into word file
convertDocxToPdf(j, k) # - convert it into pdf
```

3. You don't need to change anything in this file. The changes which you need to make is in [variables](assets/variables.py) file.  
4. Just change the value of following pattern variable in [variables](assets/variables.py):
   1. ```pattern = str(i)```  
5. Also, you need to put value of total files inside the imgFiles directory in the variable noOfFiles variable.  
   1.   ```noOfFiles = 3  # Put the total no of files present.``` 


# How to change the pattern

1. pattern is nothing but how image files are arranged in the directory
2. Let's say the sequence in which filename is present 
3. For eg:- If the filename is img1.PNG, put ```pattern = 'img' +str(i)+```


# Author


|                                                                                                                                                                                                         <a href="https://nitin-kr.onrender.com/"><img src="https://github.com/nitinkumar30/nitscv/blob/main/image/nitin-1.jpg" width="150px " height="150px" /></a>                                                                                                                                                                                                          |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                                                                                                                                                                                                                                                                 **[Nitin Kumar](https://nitin-kr.onrender.com/)**                                                                                                                                                                                                                                                                  |
| <a href="https://twitter.com/nitinkumar30"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/twitter.png" width="32px" height="32px"></a> <a href="https://www.facebook.com/b1AcK6AG16"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/facebook.png" width="32px" height="32px"></a> <a href="https://www.linkedin.com/in/nitin30kumar/"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/linkedin.png" width="32px" height="32px"></a> |


