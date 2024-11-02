from tkinter import *
from PIL import ImageTk, Image



# instance
root = Tk()
root.title("Hello World Ttile")
root.geometry("640x480")
root.iconbitmap("20240914.jpg")

# Add Image
my_image = ImageTk.PhotoImage(Image.open("20240914.jpg"))
image_label= Label(image = my_image)
image_label.grid(row=0, column=0)

my_label = Label(root,text = " 0Hello World",fg="white",bg="black",font=("helvetica",8))
my_label.grid(row=0, column=0)

my_label_2 = Label(root,text = "1 It's Free to use! down50", relief="sunken")
my_label_2.grid(row=1, column=1, sticky=W) 

my_label_3 = Label(root,text = "2 Quick Brown Fox Raide! Row Spanning 2", relief="raised")
my_label_3.grid(row=2, column=2, rowspan=2)


my_label_4 = Label(root,text = "3 Quick Brown Fox Raide!", relief="groove")
my_label_4.grid(row=3, column=3)

my_label_5 = Label(root,text = "4 Quick Brown Fox Raide ROW 3!", relief="ridge", width=12)
my_label_5.grid(row=4, column=1)

my_label_6 = Label(root,text = "5 Quick Brown Fox Disabled", state="disabled", height=10)
my_label_6.grid(row=5, column=2, sticky=S)





# loop
root.mainloop()