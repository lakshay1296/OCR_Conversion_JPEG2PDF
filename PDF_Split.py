from PyPDF2 import PdfFileWriter, PdfFileReader
import os


def split(pdf, page_num):

    pdf_lis = pdf.split("/")
    pdf_lis1 = pdf.split("/")
    pdf_lis.remove(pdf_lis[-1])
    print(pdf_lis)
    new_path = "/".join(pdf_lis) + "/split/"
    filename = pdf_lis1[-1]
    print (filename)

    try:
        os.mkdir(new_path)

    except Exception:
        pass

    pdf_reader = PdfFileReader(open(pdf, "rb"))

    mid = round(page_num/3)

    pdf_writer = PdfFileWriter()
    for i in range(0,mid):

        pdf_writer.addPage(pdf_reader.getPage(i))
        # output.addPage(pdf)

        with open(new_path + str(filename).lower().replace(".pdf", "_1.pdf"), "wb") as outputStream:
            pdf_writer.write(outputStream)

        outputStream.close()

    pdf_writer = PdfFileWriter()
    for i in range(mid, mid+mid):
        pdf_writer.addPage(pdf_reader.getPage(i))
        # output.addPage(pdf)

        with open(new_path + str(filename).lower().replace(".pdf", "_2.pdf"), "wb") as outputStream1:
            pdf_writer.write(outputStream1)

        outputStream1.close()

    pdf_writer = PdfFileWriter()
    for i in range(mid+mid, page_num):
        pdf_writer.addPage(pdf_reader.getPage(i))
        # output.addPage(pdf)

        with open(new_path + str(filename).lower().replace(".pdf", "_3.pdf"), "wb") as outputStream1:
            pdf_writer.write(outputStream1)

        outputStream1.close()


def merge(pdf): pass

