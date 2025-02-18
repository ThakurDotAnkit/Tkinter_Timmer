from tkinter import *
import tkinter

windows = Tk()
windows.title("My First GUI Program")
windows.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24))
my_label.grid()

my_label.config(text="New_Text")


# Button
def button_clicked():
    my_label.config(text=input.get())
    print("I Got Clicked")


button = Button(text="Click Me", command=button_clicked)
button.grid(column=2,row=2)


# Button2
button1 = Button(text="Do Not Click Me")
button1.grid(column=3,row=1)




# Entry
input = Entry(width=10)
# input.grid()
input.grid(column=4,row= 3)
print(input.get())


def get_input():
    print(input.get())
    my_label.config(text=input.get())


windows.mainloop()
