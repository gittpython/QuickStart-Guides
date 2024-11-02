from tkinter import *
from PIL import ImageTk, Image
# instance
root = Tk()
root.title("Hello World Tile")
root.geometry("640x480")

#Create clicked function
def clicked():
    global my_label2
    input = e.get()
    my_label2=Label(root, text= "You clicked the shit! " + input)
    my_label2.pack()
	#my_label2.grid(row=7, column=1)

# hide function
def hise():
	my_label2.pack_forget()
	# my_label2.destroy()

# show vunction
def show():
    my_label2.pack()

#my_label = Label(root,text = " 0Hello World",fg="white",bg="black",font=("helvetica",8))
#my_label.pack()

# Create Buttoons
my_button = Button(root, text="Click Shit",command=clicked)
my_button.pack()

hide_button = Button(root, text="Hide",command=hide)
hide_button.pack()

show_button = Button(root, text="Show",command=show)
show_button.pack()

e = Entry(root, font=("Helvetica", 18))
e.pack(pady=20)

# loop
root.mainloop()