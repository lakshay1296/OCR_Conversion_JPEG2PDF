from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import time

def functionality():
    pass

def progress_bar(master, val):

    style = ttk.Style()

    style.theme_use('default')

    style.configure("black.Horizontal.TProgressbar", background='black')

    bar = Progressbar(master, length=200, variable=val, style='black.Horizontal.TProgressbar')

    bar.grid(column=0, row=0)

    bar.pack()


def window(master):
    """ Main Window """
    root_app.title("Tesseract powered OCR")

    """ Start Frame to hold widgets """

    main_frame = Frame(master=master)
    main_frame.grid(row=1, column=0, sticky=S)

    label = Label(main_frame, text="Tesseract Powered OCR", bg="white", height=2, width=100)
    label.pack()

    select_pdf = IntVar()
    Checkbutton(master, text=" PDF", variable=select_pdf, padx=100) \
        # .grid(row=1)

    """ Pack the frame """

    main_frame.config(bd=1, relief=SOLID)
    main_frame.pack()


if __name__ == '__main__':
    root_app = Tk()
    # Set constant app size
    root_app.geometry("1280x720")
    window(root_app)
    root_app.mainloop()

    for i in range(5):

        time.sleep(2.0)
        progress_bar(root_app, i)
        print(i)
