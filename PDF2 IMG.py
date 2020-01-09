'''------------------------------------------------------------------------

    Put "your path\poppler-0.68.0\bin" location to the environment variable

------------------------------------------------------------------------'''

from pdf2image import convert_from_path
import cv2
import os

'''----------------------------------------------------------------
    For converting PDF into JPEG and save them on the local system.
----------------------------------------------------------------'''

for root, dir, files in os.walk("C:\\Users\lakshay.saini\Desktop\Med Legal\PDF\PDF"):
    for file in files:

        # Putting "\bin" path in poppler_path helps in locating executable file
        pages = convert_from_path(root + "/" + file, 300, poppler_path="C:\\Users\lakshay.saini\PycharmProjects\OCR_Conversion_JPEG2PDF\poppler-0.68.0\\bin")
        count = 1
        for page in pages:

            page.save(root + "/image/" + file.replace(".pdf", "_" + str(count) + ".jpeg"), "JPEG")
            count = count + 1

        print (file)