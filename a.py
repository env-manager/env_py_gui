from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title('Drop Down Button')

root.geometry("400x400")

# Drop Down Boxes

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
drop.pack()

img = Image.open('/home/orangepi/env_sensor/env_py_gui/img/humidity/humidity0.png')
temp_hum_0_img = img.resize((240, 35), Image.ANTIALIAS)
hum_0_img = ImageTk.PhotoImage(temp_hum_0_img)

img_label = Label(root, image=hum_0_img, bg='black')
img_label.pack()

# def get_image_instance(frame, path, width, height, row, column,sticky, command=None):
#     img = Image.open(path)
#     resized_img = img.resize((width,height), Image.ANTIALIAS)
#     photo_img = ImageTk.PhotoImage(resized_img)
#     img_label = Label(frame, image=photo_img, bg='black')
#     img_label.image = photo_img
#     img_label.grid(row=row, column=column, sticky=sticky)
#     def local_click(event):
#         if command == None:
#             pass
#         else:
#             command()
#     img_label.bind("<Button-1>", local_click)
#     return img_label

# hum_gauge = get_image_instance(root,'/home/orangepi/env_sensor/env_py_gui/img/humidity/humidity5.png', 240, 35, 0, 5, 'NEWS')

root.mainloop()