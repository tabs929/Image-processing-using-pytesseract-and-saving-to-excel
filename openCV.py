# Import libraries
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
  
# Path of the pdf
PDF_file = "C:/Users/DELL/opencvIntern/soups.pdf"
  
'''
Part #1 : Converting PDF to images
'''
  
# Store all the pages of the PDF in a variable
pages = convert_from_path(PDF_file, poppler_path = r"C:\Users\DELL\OneDrive\Desktop\poppler\poppler-0.68.0\bin")
  
# Counter to store images of each page of PDF to image
image_counter = 1
  
# Iterate through all the pages stored above
for page in pages:
  
    filename = "page_"+str(image_counter)+".jpg"
      
    # Save the image of the page in system
    page.save(filename, 'JPEG')
  
    # Increment the counter to update filename
    image_counter = image_counter + 1
  
'''
Part #2 - Recognizing text from the images using OCR
'''
# Variable to get count of total number of pages
filelimit = image_counter-1
  
# Creating a text file to write the output
outfile = "out_text.txt"
  
# Open the file in append mode so that 
# All contents of all images are added to the same file
f = open(outfile, "a")
  
# Iterate from 1 to total number of pages
for i in range(1, filelimit + 1):
  
    # Set filename to recognize text from
    filename = "page_"+str(i)+".jpg"
          
    # Recognize the text as string in image using pytesserct
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
  
    text = text.replace('-\n', '')    
  
    # Finally, write the processed text to the file.
    f.write(text)
  
# Close the file after writing all the text.
f.close()