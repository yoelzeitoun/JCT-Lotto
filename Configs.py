from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import ImageTk, Image
from LottoFrame import LottoFrame


class Configs(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.is_show_timer_to_user = False
        self.is_time_limit = False
        self.is_show_during_form = False
        self.is_add_image = False
        self.photo_path = ""
        self.num_of_rows = 0
        self.num_of_columns = 0
        self.time_allocation = 0
        self.ImageCheckButtonVar = IntVar()
        self.radioButtonVar = IntVar()
        self.timeCheckButtonVar = IntVar()
        self.showTimerCheckButtonVar = IntVar()

        master.geometry("400x700")
        self.config_frame = Frame(master)

        self.config_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

        ############################# FORM CONFIGURATIONS #############################
        Label(self.config_frame, text="Number of rows").pack()
        self.row_entry = Entry(self.config_frame, justify=CENTER)
        self.row_entry.insert(0, "4")
        self.row_entry.pack()
        Label(self.config_frame, text="Number of columns").pack()
        self.column_entry = Entry(self.config_frame, justify=CENTER)
        self.column_entry.insert(0, "10")
        self.column_entry.pack()
        sep1 = ttk.Separator(self.config_frame, orient=HORIZONTAL)
        sep1.pack(fill=X, pady=10)
        ############################# TIME CONFIGURATIONS #############################
        self.time_frame = Frame(self.config_frame)
        self.time_frame.pack(fill=X, padx=5, pady=5)
        Checkbutton(self.time_frame, text="Time Limit?",
                    command=self.__time_check_button_logic, variable=self.timeCheckButtonVar).pack()

        self.into_time_frame = Frame(self.time_frame)

        Checkbutton(self.into_time_frame, text="Show Timer to user?", variable=self.showTimerCheckButtonVar).pack()
        Label(self.into_time_frame, text="time allocation (in seconds)").pack()
        self.time_entry = Entry(self.into_time_frame, justify=CENTER)
        self.time_entry.insert(0, "60")
        self.time_entry.pack()
        sep2 = ttk.Separator(self.config_frame, orient=HORIZONTAL)
        sep2.pack(fill=X, pady=10)
        ############################# IMAGE CONFIGURATIONS #############################
        image_frame = Frame(self.config_frame)
        image_frame.pack(fill=X, padx=5, pady=5)
        ###### Check-Button ######
        Checkbutton(image_frame, text="Add image?",
                    command=self.__image_check_button_logic, variable=self.ImageCheckButtonVar).pack()

        self.into_image_frame = Frame(image_frame)
        ###### Button ######
        logo = PhotoImage(file="upload.gif")
        button_upload = Button(self.into_image_frame, image=logo, command=self.__upload_image)
        button_upload.image = logo
        button_upload.pack()

        ###### Radio-Button ######
        radio_button1 = Radiobutton(self.into_image_frame, text="Show only before viewing the form",
                                    variable=self.radioButtonVar,
                                    value=0)
        radio_button1.pack()
        radio_button2 = Radiobutton(self.into_image_frame, text="Show before and during viewing the form",
                                    variable=self.radioButtonVar, value=1)
        radio_button2.pack()
        radio_button1.invoke()

        ############################# Button Validation #############################

        validation_frame = Frame(self.config_frame)
        validation_frame.pack()
        validation_button = Button(validation_frame, text="Start", command=lambda: self.__end_config(master),
                                   height=2, width=20)
        validation_button.pack()

    def __end_config(self, master):
        if self.__configure_all():
            self.config_frame.forget()
            LottoFrame(master, self).tkraise()

    def __configure_all(self):
        self.num_of_rows = self.row_entry.get()
        if not self.__check_entry(self.num_of_rows):
            return False

        self.num_of_columns = self.column_entry.get()
        if not self.__check_entry(self.num_of_columns):
            return False

        self.time_allocation = self.time_entry.get()
        if not self.__check_entry(self.time_allocation):
            return False

        self.is_time_limit = True if self.timeCheckButtonVar.get() == 1 else False

        self.is_show_timer_to_user = True if self.showTimerCheckButtonVar.get() == 1 else False

        self.is_add_image = True if self.ImageCheckButtonVar.get() == 1 else False

        self.is_show_during_form = True if self.radioButtonVar.get() == 1 else False

        if self.is_add_image and len(self.photo_path) == 0:
            messagebox.showerror("ERROR", "Please select a picture!")
            return False

        return True

    def __check_entry(self, num):
        try:
            int(num)
        except ValueError:
            messagebox.showerror("ERROR", "Please enter a valid number!")
            return False
        return True

    def __image_check_button_logic(self):
        if self.ImageCheckButtonVar.get() == 0:
            self.into_image_frame.pack_forget()
        else:
            self.into_image_frame.pack(fill=X, padx=5, pady=5)

    def __time_check_button_logic(self):
        if self.timeCheckButtonVar.get() == 0:
            self.into_time_frame.pack_forget()
        else:
            self.into_time_frame.pack(fill=X, padx=5, pady=5)

    def __upload_image(self):
        # global photo_path
        self.photo_path = filedialog.askopenfilename(initialdir="/Downloads", title="Select A File",
                                                     filetype=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        global path_label
        try:
            path_label.destroy()  # when the user wants to change the image he uploaded
        except NameError:
            pass
        path_label = Label(self.into_image_frame, text=self.photo_path)
        path_label.pack()

        img = Image.open(self.photo_path).resize((300, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)

        global photo_label
        try:
            photo_label.destroy()
        except NameError:
            pass
        photo_label = Label(self.into_image_frame, image=photo)
        photo_label.image = photo
        photo_label.pack()
