# OCR_Conversion_JPEG2PDF - Windows
### This is a very rough code.

JPEG to OCR'd PDF conversion using tesseract v4 through cmd. Includes OCR'ing the JPEG's and combining multi-page PDF to one.

It is just a simple implementation of using tesseract with **python** (uses os.system for making it work through command line). It works well on windows, however, I couldn't find a way for PDF to PDF conversion using command line as we need to read PDF using command line. 
On the other hand, reading a **JPEG** is still possible with **libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 1.5.3) : libpng 1.6.34 : libtiff 4.0.9 : zlib 1.2.11 : libwebp 0.6.1 : libopenjp2 2.2.0** libraries present in windows.

I'm currently trying to make ***ocrmypdf*** on windows as it shows error in **leptonica.py** about the dll. It's not impossible to do, if anyone finds a way, you can make changes in the repository in a new branch.

##Requirements
Make sure to install libraries in the same manner

-libjpeg : libpng : libtiff : zlib : libwebp : libopenjp2
-leptonica (v1.78) (you can use any version but you would need to change the location of liblept.so location in the code)
-Tesseract (any version)
-Tesseract Language Data (big tessdata)
-ocrmypdf library

## Workflow
- You need to provide the converted JPEG's of PDF's to the code
- Naming convention for JPEG: ***PDFname_count*** (if you want to change, make changes in the ReGex too)
- All the JPEG's must be present in single folder
- OCR folder will be created in root folder
- PDF's will be created page-wise
- Page-wise PDF's will be merged into one parent PDF automatically
- Parent PDF's will be placed in OCR folder.

## Licensing
You can use this repository in anyway you need. Kindly make any changes in a different branch.
