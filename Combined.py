'''------------------------------------------------------------------------

    Put "your path\poppler-0.68.0\bin" location to the environment variable

------------------------------------------------------------------------'''

from pdf2image import convert_from_path
import cv2
import os
import re
import csv
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import pandas as pd

def perform_ocr(path=None, oem_mode=None, psm_mode=None):
    # for root, dir, files in os.walk(path, topdown=True):
    #     for jpeg in files:
    if path.lower().endswith(".jpeg"):
        inputFile = path
        outputFile = path.replace(".jpeg", "")
        os.system('tesseract --psm 6 "' + inputFile + '" "' + outputFile + '" pdf')
        # os.system('tesseract "' + inputFile + '" "' + outputFile + '" --oem 1 --psm 6 pdf')


def pdf2img(pdf_location, poppler_path):

    for root, dir, files in os.walk(pdf_location):
        for pdf_file in files:
            if ".pdf" in pdf_file:

                path = root + "\\" + pdf_file

                ocr_path = path.replace(".pdf", "_ocr.pdf")

                pdf_writer = PdfFileWriter()

                # Putting "\bin" path in poppler_path helps in locating executable file
                pages = convert_from_path(path, 300, poppler_path=poppler_path)

                count = 1
                for page in pages:
                    # page.save(root + pdf_file.replace(".pdf", "_" + str(count) + ".jpeg"), "JPEG")

                    jpeg_path = path.replace(".pdf", "_.jpeg")
                    page.save(jpeg_path, "JPEG")

                    perform_ocr(path=jpeg_path)

                    os.remove(jpeg_path)

                    ''' pdf merge '''

                    pdf_path = jpeg_path.replace(".jpeg", ".pdf")
                    pdf_obj = open(pdf_path, "rb")
                    pdf_reader = PdfFileReader(pdf_obj)

                    for page in range(pdf_reader.getNumPages()):
                        pdf_writer.addPage(pdf_reader.getPage(page))

                    print ("Ocr'd " + str(count) + " Page")
                    count = count + 1

                    with open(ocr_path, 'wb') as fh:
                        pdf_writer.write(fh)

                    pdf_obj.close()

                    os.remove(pdf_path)

                print("OCR'd " + pdf_file + " successfully.")


if __name__ == '__main__':
    pdf_loc = input("Enter PDF Location: ")
    poppler_path = "C:\\Users\lakshay.saini\PycharmProjects\OCR_Conversion_JPEG2PDF\poppler-0.68.0\\bin"
    pdf2img(pdf_loc, poppler_path)
