"""------------------------------------------------------------------------

    Put "your path\poppler-0.68.0\bin" location to the environment variable

------------------------------------------------------------------------"""

from pdf2image import convert_from_path
import cv2
import os
import re
import csv
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from tkinter import messagebox
import pandas as pd

""" Check if PDF is encrypted or not. """


def check_pdf_encryption(pdf_path):
    pdf_reader = PdfFileReader(open(pdf_path, "rb"))

    if pdf_reader.isEncrypted:
        return True

    else:
        return False


""" Check if PDF's pages are scanned or readable. """


def is_readable(pdf):
    pdf_reader = PdfFileReader(open(pdf, "rb"))
    # pdf_reader.getNumPages()
    for page in range(pdf_reader.getNumPages()):
        page_data = pdf_reader.getPage(page)
        if "/Font" in page_data["/Resources"]:
            print("[Info]: Looks like there is text in the PDF, contains:", page_data['/Resources'].keys())
            print("Page: " + str(page) + " contains text")
            print(page_data.get("/Rotate"))

        else:
            print("Page: " + str(page) + " does not contain text")
            print(page_data.get("/Rotate"))


''' Performing OCR using Tesseract '''


def perform_ocr(path=None, command=None):
    if path.lower().endswith(".jpeg"):
        inputFile = path
        outputFile = path.replace(".jpeg", "")

        os.system('tesseract "' + inputFile + '" "' + outputFile + '"' + " ".join(command))
        print ('This is the command: tesseract "' + inputFile + '" "' + outputFile + '"' + " ".join(command))
        # os.system('tesseract "' + inputFile + '" "' + outputFile + '" --oem 1 --psm 6 pdf')


def pdf2img(pdf_location,
            poppler_path = "C:\\Users\lakshay.saini\PycharmProjects\OCR_Conversion_JPEG2PDF\poppler-0.68.0\\bin",
            command=None):
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

                    perform_ocr(path=jpeg_path, command=command)

                    os.remove(jpeg_path)

                    ''' pdf merge '''

                    pdf_path = jpeg_path.replace(".jpeg", ".pdf")
                    pdf_obj = open(pdf_path, "rb")
                    pdf_reader = PdfFileReader(pdf_obj)

                    for page in range(pdf_reader.getNumPages()):
                        pdf_writer.addPage(pdf_reader.getPage(page))

                    print("Ocr'd " + str(count) + " Page")
                    count = count + 1

                    with open(ocr_path, 'wb') as fh:
                        pdf_writer.write(fh)

                    pdf_obj.close()

                    os.remove(pdf_path)

                print("OCR'd " + pdf_file + " successfully.")
                messagebox.showinfo(title="OCR Complete", message=pdf_file + " has been OCR'd")

def single_file_ocr(pdf_location,
            poppler_path = "C:\\Users\lakshay.saini\PycharmProjects\OCR_Conversion_JPEG2PDF\poppler-0.68.0\\bin",
            command=None):
    # for root, dir, files in os.walk(pdf_location):
    #     for pdf_file in files:
    #         if ".pdf" in pdf_file:

                path = pdf_location

                path_list = path.split("/")
                pdf_file = path_list[len(path_list)-1]

                ocr_path = path.replace(".pdf", "_ocr.pdf")

                pdf_writer = PdfFileWriter()

                # Putting "\bin" path in poppler_path helps in locating executable file
                pages = convert_from_path(path, 300, poppler_path=poppler_path)

                count = 1
                for page in pages:
                    # page.save(root + pdf_file.replace(".pdf", "_" + str(count) + ".jpeg"), "JPEG")

                    jpeg_path = path.replace(".pdf", "_.jpeg")
                    page.save(jpeg_path, "JPEG")

                    perform_ocr(path=jpeg_path, command=command)

                    os.remove(jpeg_path)

                    ''' pdf merge '''

                    pdf_path = jpeg_path.replace(".jpeg", ".pdf")
                    pdf_obj = open(pdf_path, "rb")
                    pdf_reader = PdfFileReader(pdf_obj)

                    for page in range(pdf_reader.getNumPages()):
                        pdf_writer.addPage(pdf_reader.getPage(page))

                    print("Ocr'd " + str(count) + " Page")
                    count = count + 1

                    with open(ocr_path, 'wb') as fh:
                        pdf_writer.write(fh)

                    pdf_obj.close()

                    os.remove(pdf_path)

                print("OCR'd " + pdf_file + " successfully.")
                messagebox.showinfo(title="OCR Complete", message=pdf_file + " has been OCR'd")


if __name__ == '__main__':
    # C:\Users\lakshay.saini\Desktop\OCR Folder
    pdf_loc = input("Enter PDF Location: ")
    # poppler_path = "C:\\Users\lakshay.saini\PycharmProjects\OCR_Conversion_JPEG2PDF\poppler-0.68.0\\bin"
    is_readable(pdf_loc)
    # pdf2img(pdf_loc, poppler_path)
