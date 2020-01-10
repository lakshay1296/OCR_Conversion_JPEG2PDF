'''
    inputFile needs to be an image
    inputFile format: PDFname_count (if you want the naming convention to be different, then change the regex too.)

    outputFile needs to be pdf

    Put "your path\poppler-0.68.0\bin" location to the environment variable

'''

import os
import re
import csv
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import pandas as pd

''' Enter path of folder containing images '''

# C:\\Users\lakshay.saini\Desktop\Med Legal\PDF\Images
path = input("Enter folder path containing images: ")
# try:
#
#     os.makedirs(str(path) + "/OCR")
#
# except Exception:
#     pass

df = pd.read_csv("C:\\Users\lakshay.saini\Desktop\LIVE\image\Listing.csv")
df1 = pd.read_csv("C:\\Users\lakshay.saini\Desktop\LIVE\PDF_Listing.csv")

def extract_list():
    f = open("C:\\Users\lakshay.saini\Desktop\LIVE\Listing.csv", "w+", newline="")
    w = csv.writer(f, delimiter=",")
    w.writerow(["File Name"])

    # Keep the directory files in an alphabetical order
    for root, dir, files in os.walk("C:\\Users\lakshay.saini\Documents\image", topdown=True):
        for file in files:
            if file.lower().endswith(".jpeg"):
                w.writerow([str(file)])


def perform_ocr(oem_mode=None, psm_mode=None):

    ''' OCR Code '''
    for root, dir, files in os.walk(path):
        for jpeg in files:
            if jpeg.lower().endswith(".jpeg"):
                inputFile = root + "/" + jpeg
                outputFile = root + "/" + jpeg.replace(".jpeg", "")
                os.system('tesseract --psm 6 "' + inputFile + '" "' + outputFile + '" pdf')
                # os.system('tesseract "' + inputFile + '" "' + outputFile + '" --oem 1 --psm 6 pdf')

def pdf_merge():

    ''' PDF creation and merging from images. '''
    for i in df.index:
        print(df)
        fileName = df["File Name"][i]
        pdf_writer = PdfFileWriter()

        for j in df1.index:
                pdf = df1["File Name"][j]
                root = df1["Root"][i]

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

