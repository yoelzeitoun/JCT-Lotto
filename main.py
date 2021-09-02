from Configs import Configs
from Draw import Draw
from Menu import MenuBar
from tkinter import *


def main():
    root = Tk()
    root.title('JCT Lotto')
    MenuBar(root)
    Configs(root)

    root.mainloop()


if __name__ == "__main__": main()
