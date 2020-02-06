"""
    pack manger parameters: -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
    anchor params: n, ne, e, se, s, sw, w, nw, or center
    grid param: -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from threading import Thread
from Combined import perform_ocr
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2image import convert_from_path
import time
import os


class window(object):

    def __init__(self, master):
        """ Main Window """

        var_list = []
        self.master = master

        self.menu_bar(self.master)

        Label(self.master, text="Tesseract Powered OCR", bg="white", height=2, width=55) \
            .grid(row=0, sticky=NW, padx=10, pady=5)

        select_pdf = BooleanVar()
        pdf_c = Checkbutton(self.master, text=" PDF", variable=select_pdf) \
            .grid(sticky=NW, padx=15, row=1, column=0)

        select_hocr = BooleanVar()
        hocr = Checkbutton(self.master, text=" hOCR", variable=select_hocr) \
            .grid(sticky=NE, padx=15, row=1, column=0)

        var_list.append(select_pdf)
        var_list.append(select_hocr)

        combo = ttk.Combobox(self.master)
        combo["values"] = ("Select PSM mode", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
        combo.current(0)
        combo.grid(sticky=NW, padx=15, pady=5, row=2)
        var_list.append(combo)

        # Button for opening folder location
        folder_open = Button(self.master, text="Select Folder Location", command=lambda: self.folderopen()) \
            .grid(sticky=NW, padx=15, pady=5, row=3)

        # Button for opening files
        file_open = Button(self.master, text="Select PDF Location", command=lambda: self.fileopen()) \
            .grid(sticky=NW, padx=15, pady=5, row=4)

        # Button for submitting options
        # submit_button = Button(self.master, text="Submit", command=lambda: self.submit(var_list)) \
        #     .grid(sticky=NW, padx=15, pady=5)

        # Button which activates the progress bar
        add_bar = Button(self.master, text="Real Submit", command=lambda: self.start_thread(var_list), bd=1, relief=SOLID) \
            .grid(sticky=NW, padx=15, pady=5, row=5)

    def submit(self, var_list):
        # list is [pdf, ocr, psm mode]
        # for i in check_list:
        #     print(i.get())
        self.commands = []

        psm_mode = " --psm " + str(var_list[2].get())
        self.commands.append(psm_mode)

        # PDF Conversion
        # if var_list[0].get() is True:
        #     print ("PDF has been selected.")
        #     self.commands.append(" pdf")
        #
        # # HOCR Conversion
        # if var_list[1].get() is True:
        #     print ("HOCR has been selected.")
        #     self.commands.append(" hocr")
        #
        # if self.function == "Initiated fileopen":
        #     # single_file_ocr(pdf_location=self.filename, command=self.commands)
        #     self.ocr_code_singleFile(pdf_location=self.filename, command=self.commands)
        #
        # elif self.function == "Initiated folderopen":
        #     pdf2img(pdf_location=self.filename, command=self.commands)
        #
        # else:
        #     print ("pass")
        pass

    def fileopen(self):
        # withdraws the master window
        # master.withdraw()

        self.function = "Initiated fileopen"
        self.filename = filedialog.askopenfilename()
        pdf_name = self.filename.split("/")
        pdf = pdf_name[len(pdf_name) - 1]
        Label(self.master, text=pdf, font="Helvetica 9 bold").grid(sticky=E, padx=15, pady=5, row=4)

    def folderopen(self):
        # withdraws the master window
        # master.withdraw()

        self.function = "Initiated folderopen"
        self.filename = filedialog.askdirectory()
        pdf_name = self.filename.split("/")
        pdf = pdf_name[len(pdf_name) - 1]
        Label(self.master, text=pdf, font="Helvetica 9 bold").grid(sticky=E, padx=15, pady=5, row=3)

    def menu_bar(self, master):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        helpMenu = Menu(menubar)
        menubar.add_cascade(label="Menu", menu=fileMenu)
        fileMenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="About", menu=helpMenu)
        helpMenu.add_command(label="Help")

    def add_bar(self):
        var = IntVar()
        var.set(0)

        # print (self.commands)

        progessbar = ttk.Progressbar(self.master, variable=var, orient=HORIZONTAL, length=200).grid()

        for x in range(10):
            time.sleep(1.0)
            var.set(x)

        messagebox.showinfo(title="OCR Completed", message="The file has been OCR'd successfully")

    def start_thread(self, var_list):
        # t = Thread(target=lambda: self.add_bar())
        self.commands = []

        psm_mode = " --psm " + str(var_list[2].get())
        self.commands.append(psm_mode)

        # PDF Conversion
        if var_list[0].get() is True:
            print("PDF has been selected.")
            self.commands.append(" pdf")

        # HOCR Conversion
        if var_list[1].get() is True:
            print("HOCR has been selected.")
            self.commands.append(" hocr")

        if self.function == "Initiated fileopen":
            t = Thread(target=lambda: self.ocr_code_singleFile(pdf_location=self.filename, var_list=var_list, command=self.commands))
            t.start()

        elif self.function == "Initiated folderopen":
            t = Thread(target=lambda: self.ocr_code_multiFile(pdf_location=self.filename, var_list=var_list,
                                                               command=self.commands))
            t.start()
        else:
            print("pass")

    def ocr_code_singleFile(self, pdf_location,
            poppler_path = "C:\\Users\lakshay.saini\PycharmProjects\OCR_Conversion_JPEG2PDF\poppler-0.68.0\\bin",
            command=None, var_list=None):

        var = IntVar()
        var.set(0)

        Label(self.master, text="OCR Progess: ", font="Helvetica 9 bold").grid(sticky=NW, padx=15, pady=5, row=6)
        progessbar = ttk.Progressbar(self.master, variable=var, orient=HORIZONTAL, length=200).grid(sticky=NW, padx=15, pady=5, row=7)

        path = pdf_location

        pdf = PdfFileReader(open(pdf_location, 'rb'))
        page_count = pdf.getNumPages()

        print("Pages count is: ", page_count)

        path_list = path.split("/")
        pdf_file = path_list[len(path_list) - 1]

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

            with open(ocr_path, 'wb') as fh:
                pdf_writer.write(fh)

            pdf_obj.close()

            os.remove(pdf_path)

            # For calculating the OCR Progress
            x = (count / page_count) * 100
            percentage = round(x)
            var.set(percentage)
            time.sleep(5.0)
            count = count + 1

        print("OCR'd " + pdf_file + " successfully.")
        messagebox.showinfo(title="OCR Complete", message=pdf_file + " has been OCR'd")


    def ocr_code_multiFile(self, pdf_location,
            poppler_path = "C:\\Users\lakshay.saini\PycharmProjects\OCR_Conversion_JPEG2PDF\poppler-0.68.0\\bin",
            command=None, var_list=None):

        var = IntVar()

        var1 = IntVar()
        var1.set(0)

        labelVar = StringVar()
        labelVar.set("Files Progress: ")

        Label(self.master, text="OCR Progess: ", font="Helvetica 9 bold").grid(sticky=NW, padx=15, pady=5, row=6)
        progessbar = ttk.Progressbar(self.master, variable=var, orient=HORIZONTAL, length=200).grid(sticky=NW, padx=15, pady=5, row=7)
        label1 = Label(self.master, text=labelVar.get(), font="Helvetica 9 bold")\
            # .grid(sticky=NW, padx=15, pady=5)
        progessbar = ttk.Progressbar(self.master, variable=var1, orient=HORIZONTAL, length=200).grid(sticky=NW, padx=15, pady=5, row=9)
        print (label1["text"])

        file_count_list = []

        for root, dir, files in os.walk(pdf_location):
            for pdf_file in files:
                if ".pdf" in pdf_file:
                    file_count_list.append(pdf_file)
        file_count = len(file_count_list)

        file_process = 1
        for root, dir, files in os.walk(pdf_location):
            for pdf_file in files:
                if ".pdf" in pdf_file:

                    # labelVar.set("Files Progress: "+pdf_file+ " Completed.")
                    label1["text"] = "File Name: " + pdf_file
                    label1.grid(sticky=NW, padx=15, pady=5, row=8)
                    print(label1["text"])

                    path = root + "\\" + pdf_file

                    pdf = PdfFileReader(open(path, 'rb'))
                    page_count = pdf.getNumPages()

                    print("Pages count is: ", page_count)

                    path_list = path.split("/")
                    pdf_file = path_list[len(path_list) - 1]

                    ocr_path = path.replace(".pdf", "_ocr.pdf")

                    pdf_writer = PdfFileWriter()

                    # Putting "\bin" path in poppler_path helps in locating executable file
                    pages = convert_from_path(path, 300, poppler_path=poppler_path)

                    var.set(0)
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

                        with open(ocr_path, 'wb') as fh:
                            pdf_writer.write(fh)

                        pdf_obj.close()

                        os.remove(pdf_path)

                        # For calculating the OCR Progress
                        x = (count / page_count) * 100
                        percentage = round(x)
                        var.set(percentage)
                        time.sleep(5.0)
                        count = count + 1

                    print("OCR'd " + pdf_file + " successfully.")

                    # For file processing progress bar
                    y = (file_process / file_count) * 100
                    percentage = round(y)
                    var1.set(percentage)
                    file_process = file_process + 1

        messagebox.showinfo(title="OCR Complete", message="All the files has been OCR'd")


if __name__ == '__main__':
    root_app = Tk()
    root_app.title("Tesseract powered OCR")
    # Set constant app size
    # root_app.geometry("1280x720")
    app = window(root_app)
    root_app.mainloop()
