import tkinter
from tkinter import *
windows = Tk()
windows.title("mile To Kilometer Converter")
windows.minsize(400, 400)
windows.config(padx=100, pady=100)

#input
# Entry
input = Entry(width=10)
# input.grid()
input.grid(column=1,row= 0)
print(input.get())

# Label
my_label = tkinter.Label(text="Miles", font=("Arial", 14))
my_label.grid(column= 2, row= 0)

# Label
my_label1 = tkinter.Label(text="is_equal_to", font=("Arial", 14))
my_label1.grid(column= 0, row= 1)

my_label2 = tkinter.Label(text=f"0", font=("Arial", 14))
my_label2.grid(column=1, row=1)

my_label3 = tkinter.Label(text="KM", font=("Arial", 14))
my_label3.grid(column= 2, row= 1)
# Button
def button_clicked():
    a=input.get()
    my_label2 = tkinter.Label(text=f"{round((int(a)*1.6),2)}", font=("Arial", 14))
    my_label2.grid(column=1, row=1)
    print(int(a)*1.6)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)


windows.mainloop()