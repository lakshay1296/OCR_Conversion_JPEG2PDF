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

    for root, dir, files in os.walk("C:\\Users\lakshay.saini\Desktop\Med Legal\PDF\PDF"):
        for file in files:

            # Putting "\bin" path in poppler_path helps in locating executable file
            pages = convert_from_path(root + "/" + file, 300, poppler_path="C:\\Users\lakshay.saini\PycharmProjects\OCR_Conversion_JPEG2PDF\poppler-0.68.0\\bin")
            count = 1
            for page in pages:

                page.save(root + "/image/" + file.replace(".pdf", "_" + str(count) + ".jpeg"), "JPEG")
                count = count + 1

            print (file)

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

    image_tweak()