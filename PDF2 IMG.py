'''------------------------------------------------------------------------

    Put "your path\poppler-0.68.0\bin" location to the environment variable

------------------------------------------------------------------------'''

from pdf2image import convert_from_path
import cv2
import os

'''----------------------------------------------------------------
    For converting PDF into JPEG and save them on the local system.
----------------------------------------------------------------'''

def pdf2img():
    count = 1
    # for root, dir, files in os.walk("C:\\Users\lakshay.saini\Documents\TEST\PDFs", topdown=True):
    #     for pdf_file in files:
    #         if "Martin Renteria-page299.pdf" in pdf_file:

                # Putting "\bin" path in poppler_path helps in locating executable file
                # pages = convert_from_path(root + "/" + pdf_file, 300, poppler_path="C:\\Users\lakshay.saini\PycharmProjects\OCR_Conversion_JPEG2PDF\poppler-0.68.0\\bin")
    pages = convert_from_path("D:\Data\\26 feb Med Legal" + "/" + "Alta Los Angeles Hospitals Inc - Medical Records_172570.PDF", 300,
                              poppler_path="C:\\Users\lakshay.saini\PycharmProjects\OCR_Conversion_JPEG2PDF\poppler-0.68.0\\bin")

    for page in pages:

        page.save("D:\Data\\26 feb Med Legal" + "/image/" + "Alta Los Angeles Hospitals Inc - Medical Records_172570.PDF".replace(".PDF", "_" + str(count) + ".jpeg"), "JPEG")
        count = count + 1

        print ("Converted " + str(count) + "Page")

    print ("Alta Los Angeles Hospitals Inc - Medical Records_172570.PDF")

def image_tweak():
    # C:\Users\lakshay.saini\Desktop\Med Legal\PDF\PDF\image
    image = cv2.imread("C:\\Users\lakshay.saini\Desktop\Med Legal\PDF\PDF\image\MW Complete Pain Solutions_1.jpeg", cv2.IMREAD_UNCHANGED)

    ''' Converting to GREYSCALE increases the file size '''
    # img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    y, x, z = image.shape
    new_shape = (int(x/1.5), int(y/1.5))
    resized_img = cv2.resize(image, new_shape)

    print (resized_img.shape)

    cv2.imwrite("C:\\Users\lakshay.saini\Desktop\Med Legal\PDF\PDF\image\MW Complete Pain Solutions_1_RGB.jpeg", resized_img)

if __name__ == '__main__':

    # image_tweak()
    pdf2img()