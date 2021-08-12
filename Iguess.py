from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")

random_number_list = Label(root)
random_number_sorted_list = Label(root)
Ty = Entry(root)
Ty.place(relx=0.5,rely=0.2, anchor=CENTER)
array_3d = ("NKing!")

def randomlist():
    
    randomlist = random.sample(range(5, 25),5)
    random_number_list["text"] = "new password : " + str(array_3d)
    randomlist.sort()
    random_number_sorted_list ["text"] = "Guessed Password: " + str(Ty) 

btn=Button(root,text="generate new password ",command=randomlist)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)


random_number_list.place(relx=0.5,rely=0.5,anchor=CENTER)
random_number_sorted_list.place(relx=0.5,rely=0.3, anchor=CENTER)

root.mainloop()