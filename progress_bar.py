import tkinter.ttk as ttk
import tkinter as tk
from threading import Thread
import time


class Main(object):

    def __init__(self, master):
        self.master = master

        self.label = tk.Label(self.master, text="Tesseract Powered OCR")
        self.label.pack()

        self.checkbox(self.master)

        self.frame = tk.Frame(self.master, width=400, height=400)
        self.frame.config(bd=1, relief=tk.SOLID)
        self.frame.pack(expand=True)

        self.button = tk.Button(self.frame, text="Add Bar", command=self.start_thread)
        self.button.config(bd=1, relief=tk.SOLID)
        self.button.pack(fill="y")

        # self.button1 = tk.Button(self.frame, text="Show Option", command=self.start_thread1)
        # self.button.config(bd=1, relief=SOLID)
        # self.button.pack(fill="y")

    def checkbox(self, master):
        select_pdf = tk.IntVar()
        check_pdf = tk.Checkbutton(self.master, text="PDF", variable=select_pdf)
        check_pdf.pack()

        # print(check_pdf.tk.getint())

    def start_thread(self):
        self.t = Thread(target=self.add_bar)
        self.t.start()

    # def start_thread1(self):
    #     self.t = Thread(target=self.add_label)
    #     self.t.start()

    def add_bar(self):
        var = tk.IntVar()
        var.set(0)

        progessbar = ttk.Progressbar(self.frame, variable=var, orient=tk.HORIZONTAL, length=200)
        progessbar.pack()

        self.add_values(var)

    # def add_label(self, master):
    #     label = Label(self.master, text="PDF has been selected")

    def add_values(self, var):
        variable = var
        for x in range(10):
            time.sleep(2.0)
            variable.set(x)


if __name__ == '__main__':

    root = tk.Tk()
    app = Main(root)
    root.geometry("1280x720")
    root.mainloop()
