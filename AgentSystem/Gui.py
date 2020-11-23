from tkinter import *
from time import sleep

class GUI:

    def __init__(self):
        self.__setup_ui()

    def __setup_ui(self):
        self.window = Tk()
        self.window.title('Bank Simulation')
        self.window.geometry('600x400')

        self.atm_queue_label = Label(self.window, text='ATM queue')
        self.atm_queue_label.grid(column=0, row=0, padx=30)
        self.atm_label = Label(self.window, text='ATM usage')
        self.atm_label.grid(column=1, row=0, padx=30)
        self.atm_res_label = Label(self.window, text='ATM result')
        self.atm_res_label.grid(column=2, row=0, padx=30)

        self.atm_queue_list = Listbox(width=30, height=10)
        self.atm_queue_list.grid(column=0, row=1)
        self.atm_list = Listbox(width=30, height=10)
        self.atm_list.grid(column=1, row=1)
        self.atm_res_list = Listbox(width=30, height=10)
        self.atm_res_list.grid(column=2, row=1)

        self.service_queue_label = Label(self.window, text='Service queue')
        self.service_queue_label.grid(column=0, row=2, padx=30)
        self.service_label = Label(self.window, text='Service usage')
        self.service_label.grid(column=1, row=2, padx=30)
        self.service_res_label = Label(self.window, text='Service result')
        self.service_res_label.grid(column=2, row=2, padx=30)
        self.service_queue_list = Listbox(width=30, height=10)
        self.service_queue_list.grid(column=0, row=3)
        self.service_list = Listbox(width=30, height=10)
        self.service_list.grid(column=1, row=3)
        self.service_res_list = Listbox(width=30, height=10)
        self.service_res_list.grid(column=2, row=3)


if __name__ == '__main__':
    gui = GUI()
    for i in ('one', 'one', 'one', 'one', 'one'):
        gui.atm_queue_list.insert(0, i)
    gui.window.mainloop()
