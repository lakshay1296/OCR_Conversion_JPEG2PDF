"""
    pack manger parameters: -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
    anchor params: n, ne, e, se, s, sw, w, nw, or center
    grid param: -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
"""

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Progressbar
from tkinter import ttk
import time


def functionality():
    pass


def fileopen():
    # withdraws the master window
    # master.withdraw()
    filename = askopenfilename()
    print(filename)


def menu_bar(master):
    menubar = Menu(master)
    master.config(menu=menubar)

    fileMenu = Menu(menubar)
    menubar.add_cascade(label="Menu", menu=fileMenu)
    fileMenu.add_command(label="Exit", command=master.quit)


def check_buttons(check_list):
    for i in check_list:
        print(i.get())


def window(master):
    """ Main Window """

    check_list = []

    menu_bar(master)

    """ Start Frame to hold widgets """

    Label(master, text="Tesseract Powered OCR", bg="white", height=2, width=40) \
        .grid(row=0, sticky=NW, padx=10, pady=5)

    select_pdf = IntVar()
    pdf = Checkbutton(master, text=" PDF", variable=select_pdf) \
        .grid(sticky=NW, padx=15, pady=15, row=1, column=0)

    select_hocr = IntVar()
    hocr = Checkbutton(master, text=" hOCR", variable=select_hocr) \
        .grid(sticky=NW, padx=100, pady=15, row=1)

    check_list.append(select_pdf)
    check_list.append(select_hocr)

    # Button for opening files
    file_open = Button(master, text="Select File Location", command=lambda: fileopen()) \
        .grid(sticky=NW, padx=15, pady=25, row=2)

    # Button for submitting options
    submit = Button(master, text="Submit", command=lambda: check_buttons(check_list)) \
        .grid(sticky=NW, padx=15, pady=10, row=3)


if __name__ == '__main__':
    root_app = Tk()
    root_app.title("Tesseract powered OCR")
    # Set constant app size
    # root_app.geometry("1280x720")
    window(root_app)
    root_app.mainloop()
