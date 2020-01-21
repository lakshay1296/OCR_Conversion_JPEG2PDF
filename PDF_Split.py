from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_reader = PdfFileReader(open("C:\\Users\lakshay.saini\Documents\TEST\Martin Renteria.pdf", "rb"))
pdf_writer = PdfFileWriter()

a = 99+100+100

# for i in range(a, 290):
for i in range(200,290):

    val = bool(i<=a)

    if val == True:

        pdf_writer.addPage(pdf_reader.getPage(i))
        # output.addPage(pdf)

        with open("C:\\Users\lakshay.saini\Documents\TEST\PDFs\Martin Renteria-page%s.pdf" % a, "wb") as outputStream:
            pdf_writer.write(outputStream)

        print (str(i))


