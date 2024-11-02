from tkinter import *

# instance
root = Tk()
root.title("Hello World Ttile")
root.geometry("640x480")

my_label = Label(root,text = "Hello World",fg="white",bg="black",font=("helvetica",32))
my_label.pack()

my_label_2 = Label(root,text = " It's Free to use! down50", relief="sunken")
my_label_2.pack(pady=30) # Move down

my_label_3 = Label(root,text = " Quick Brown Fox Raide!", relief="raised")
my_label_3.pack()


my_label_4 = Label(root,text = " Quick Brown Fox Raide!", relief="groove")
my_label_4.pack()

my_label_5 = Label(root,text = " Quick Brown Fox Raide!", relief="ridge", width=50)
my_label_5.pack()

my_label_6 = Label(root,text = " Quick Brown Fox Disabled", state="disabled", height=50)
my_label_6.pack()





# loop
root.mainloop()