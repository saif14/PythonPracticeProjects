from msilib.schema import RadioButton
from tkinter import *

window = Tk()

window.title("My Python GUI")
window.minsize(width=300, height=200)


my_label = Label(text="Lalala Label", font=("Arial", 18, "normal"))
my_label.grid(column=4, row=6)


def button_click():
    my_label["text"] = input_entry.get()


button = Button(text="Click me senpai!", command=button_click)
# button.pack()
button.grid(column=4, row=8)


input_entry = Entry(width=10)
input_entry.insert(END, string="LALALA")
# input_entry.pack()

# text = Text(height=5, width=30)
# text.focus()
# print(text.get("1.0", END))
# text.pack()
#
# def spin_box():
#     print(spinbox.get())
#
#
# spinbox = Spinbox(from_=0, to=10, width=5, command=spin_box)
# spinbox.pack()
#
# def scale_use(value):
#     print(value)
#
#
# scale = Scale(from_=0, to=100, command=scale_use)
# scale.pack()
#
#
# def check_btn_used():
#     print(checked_state.get())
#
#
# checked_state = IntVar()
# check_btn = Checkbutton(text="Is On?", variable= checked_state, command=check_btn_used)
# check_btn.pack()
#
#
# def radio_used():
#     print(radio_state.get())
#
#
# radio_state = IntVar()
# radio_btn1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radio_btn2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radio_btn3 = Radiobutton(text="Option3", value=3, variable=radio_state, command=radio_used)
# radio_btn1.pack()
# radio_btn2.pack()
# radio_btn3.pack()

window.mainloop()
