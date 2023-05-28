import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Ipv4Screen(ttk.Frame):
    def __init__(self, parent, controller, show_ethernet_screen):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)
        self.rowconfigure(4, weight=2)
        
        status_part = Frame(self, bg='black')
        status_part.grid(row=0, column=0, columnspan=2, sticky='NEWS')
        status_part.rowconfigure(0, weight=1)
        status_part.columnconfigure(0, weight=1)
        status_part.columnconfigure(1, weight=10)
        status_part.columnconfigure(2, weight=1)

        back_button_part = tk.Frame(status_part, bg='black')
        back_button_part.grid(row=0, column=0, sticky='NEWS')
        back_button_part.place(relx=0.1, rely=0.5, anchor='c')
        back_button_part.rowconfigure(0, weight=1)
        back_button_part.columnconfigure(0, weight=1)
        back_button_part.columnconfigure(1, weight=1)

        back_button_part.bind("<Button-1>", show_ethernet_screen)
        back_button_part.rowconfigure(0,weight=1)
        back_button_part.columnconfigure(0, weight=1)
        back_button_part.columnconfigure(1, weight=1)
        
        self.get_image(back_button_part, '/home/orangepi/env_sensor/env_py_gui/img/parts/back_button.png', 30, 30,0, 0, 'E', command=show_ethernet_screen)
        back_label = Label(back_button_part, text='BACK', font=('Arial', 30), fg='white', bg='black', pady=3)
        back_label.grid(row=0, column=1, sticky='NW')
        def back_click(event):
            show_ethernet_screen()
        back_label.bind("<Button-1>", back_click)

################################################################################################
        ipv4_frame = Frame(self, bg='red')
        ipv4_frame.grid(row=1, column=0, sticky='NEWS')

        sub_net_frame = Frame(self, bg='blue')
        sub_net_frame.grid(row=2, column=0, sticky='NEWS')

        gateway_frame = Frame(self, bg='yellow')
        gateway_frame.grid(row=3, column=0, sticky='NEWS')
        
        number_pad_frame = Frame(self, bg='green')
        number_pad_frame.grid(row=1, rowspan=3, column=1, sticky='NEWS')
        number_pad_frame.columnconfigure(0, weight=1)
        number_pad_frame.columnconfigure(1, weight=1)
        number_pad_frame.columnconfigure(2, weight=1)
        number_pad_frame.rowconfigure(0, weight=1)
        number_pad_frame.rowconfigure(1, weight=1)
        number_pad_frame.rowconfigure(2, weight=1)
        number_pad_frame.rowconfigure(3, weight=1)
        label_1 = self.number_label(number_pad_frame, '1',0,0)
        label_2 = self.number_label(number_pad_frame, '2',0,1)
        label_3 = self.number_label(number_pad_frame, '3',0,2)
        label_4 = self.number_label(number_pad_frame, '4',1,0)
        label_5 = self.number_label(number_pad_frame, '5',1,1)
        label_6 = self.number_label(number_pad_frame, '6',1,2)
        label_7 = self.number_label(number_pad_frame, '7',2,0)
        label_8 = self.number_label(number_pad_frame, '8',2,1)
        label_9 = self.number_label(number_pad_frame, '9',2,2)
        label_dot = self.number_label(number_pad_frame, '.',3,0)
        label_0 = self.number_label(number_pad_frame, '0',3,1)
        label_delete = self.number_label(number_pad_frame, 'Del',3,2)
        
        
        
        
        
# IPv4 주소
# 서브넷 마스크
# 기본 게이트웨이
    def get_image(self, frame, path, width, height, row, column,sticky, command=None):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)
        def local_click(event):
            command()
        img_label.bind("<Button-1>", local_click)
    
    def number_label(self,frame, text, row, column, fontsize=15):
        label = Label(frame, text=text, font=('Arial bold',fontsize))
        label.grid(row=row, column=column, sticky='NEWS')
        return label