"""
    pack manger parameters: -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
    anchor params: n, ne, e, se, s, sw, w, nw, or center
    grid param: -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
"""

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from threading import Thread
from Combined import perform_ocr
import time


def fileopen(master):
    # withdraws the master window
    # master.withdraw()
    filename = askopenfilename()
    print(filename)
    # Entry(master, text="Test").grid(padx=0, pady=55, row=2)


def menu_bar(master):
    menubar = Menu(master)
    master.config(menu=menubar)

    fileMenu = Menu(menubar)
    menubar.add_cascade(label="Menu", menu=fileMenu)
    fileMenu.add_command(label="Exit", command=master.quit)


def submit(var_list):
    # list is [pdf, ocr, psm mode]
    # for i in check_list:
    #     print(i.get())
    print("Submit waala: ", filename)

    psm_mode = "--psm " + str(var_list[2])

    # PDF Conversion
    if var_list[0] is True:
        pass

    # HOCR Conversion
    if var_list[1] is True:
        pass


def add_bar(master):
    var = IntVar()
    var.set(0)

    progessbar = ttk.Progressbar(master, variable=var, orient=HORIZONTAL, length=200).grid()

    for x in range(10):
        time.sleep(2.0)
        var.set(x)


def start_thread(master):
    t = Thread(target=lambda: add_bar(master))
    t.start()


def window(master):
    """ Main Window """

    var_list = []

    menu_bar(master)

    Label(master, text="Tesseract Powered OCR", bg="white", height=2, width=40) \
        .grid(row=0, sticky=NW, padx=10, pady=5)

    select_pdf = BooleanVar()
    pdf = Checkbutton(master, text=" PDF", variable=select_pdf) \
        .grid(sticky=NW, padx=15)

    select_hocr = BooleanVar()
    hocr = Checkbutton(master, text=" hOCR", variable=select_hocr) \
        .grid(sticky=NE, padx=15, row=1)

    var_list.append(select_pdf)
    var_list.append(select_hocr)

    combo = ttk.Combobox(master)
    combo["values"] = ("Select PSM mode", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    combo.current(0)
    combo.grid(sticky=NW, padx=15, pady=5)
    var_list.append(combo)

    # Button for opening files
    file_open = Button(master, text="Select File Location", command=lambda: fileopen(master)) \
        .grid(sticky=NW, padx=15, pady=5)

    # Button for submitting options
    submit_button = Button(master, text="Submit", command=lambda: submit(var_list)) \
        .grid(sticky=NW, padx=15, pady=5)

    # Button which activates the progress bar
    add_bar = Button(master, text="Add Bar", command=lambda: start_thread(master), bd=1, relief=SOLID) \
        .grid()


if __name__ == '__main__':
    filename = ""
    root_app = Tk()
    root_app.title("Tesseract powered OCR")
    # Set constant app size
    # root_app.geometry("1280x720")
    window(root_app)
    root_app.mainloop()
