'''
    inputFile needs to be an image
    inputFile format: PDFname_count

    outputFile needs to be pdf
'''

import os
import re
import csv
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

# f = open("C:\\Users\lakshay.saini\Desktop\Med Legal\PDF\Listing.csv", "w+", newline="")
# w = csv.writer(f, delimiter=",")
# w.writerow(["File Name"])

''' Enter path of folder containing images '''

# C:\\Users\lakshay.saini\Desktop\Med Legal\PDF\Images
path = input("Enter folder path containing images: ")
try:

    os.makedirs(str(path) + "/OCR")

except Exception:
    pass

import pandas as pd
df = pd.read_csv("C:\\Users\lakshay.saini\Desktop\Med Legal\PDF\Listing.csv")

''' OCR Code '''
for root, dir, files in os.walk(path):
    for jpeg in files:
        if jpeg.lower().endswith(".jpeg"):
            inputFile = root + "/" + jpeg
            outputFile = root + "/" + jpeg.replace(".jpeg", "")
            os.system('tesseract --psm 6 "' + inputFile + '" "' + outputFile + '" pdf')

''' PDF creation and merging from images. '''
for i in df.index:
    fileName = df["File Name"][i]
    pdf_writer = PdfFileWriter()

    for root, dir, files in os.walk(path):
        for pdf in files:

            ''' Extracting Parent Name '''
            matchObj = re.match("(.*)_.*.pdf", pdf, re.I | re.M)
            if matchObj:
                file_name = matchObj.group(1)
                print(file_name)
            else:
                file_name = pdf
            '''------------------------'''

            if pdf.lower().endswith(".pdf") and (file_name == fileName):

                ''' Code for merging PDF '''
                pdf_reader = PdfFileReader(root + "/" + pdf)
                for page in range(pdf_reader.getNumPages()):
                    pdf_writer.addPage(pdf_reader.getPage(page))

        with open(path + "\OCR\\" + fileName + ".pdf", 'wb') as fh:
                pdf_writer.write(fh)
        print (fileName + " PDF has been created")


# for root, dir, files in os.walk("C:\\Users\lakshay.saini\Desktop\Med Legal\PDF\Images"):
#     for file in files:
#         if file.lower().endswith(".jpeg"):
#             w.writerow([str(file)])
