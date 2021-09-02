from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from tkinter import filedialog


class LottoFrame(Frame):
    def __init__(self, master, configs, **kw):
        super().__init__(master, **kw)

        master.geometry("500x500")
        self.lotto_frame = ttk.Frame(master)
        self.lotto_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.config_image = PhotoImage(file="configs.gif")
        Button(self.lotto_frame, image=self.config_image,
               command=lambda: self.__to_config(configs)).pack(side=BOTTOM)

    def __to_config(self, configs):
        self.master.geometry("400x700")
        self.lotto_frame.destroy()
        configs.config_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)
        configs.tkraise()
