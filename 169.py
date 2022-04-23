from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkmb
root=Tk()
root.title("create dynamic elements using dropdown")
root.geometry("900x400")

gui_elements=["label","button","dropdown"]

dropdown=ttk.Combobox(root,state="readonly",values=gui_elements)
dropdown.pack()

class createElements:
    def __init__(self):
        print("this class is used to create dynamuc effect")
        
    def createlabel(self):
        label1=Label(root,text="a new label is created using class",fg="red")
        label1.pack()
        
    def createbutton(self):
        btn=Button(root,text="a new button is created using class",command=self.displaymsg)
        btn.pack()
        
    def createdrop(self):
        drop_var=[1,2,3]
        drop=ttk.Combobox(root,state="readonly",values=drop_var)
        drop.pack()
        
    def choose(self):
        global dropdown
        element=dropdown.get()
        if element=="label":
            self.createlabel()
        elif element=="button":
            self.createbutton()
        elif element=="dropdown":
            self.createdrop()
            
    def displaymsg(self):
        tkmb.showinfo("info","you created a buttion using class")
        
        
        
        
obj=createElements()
        

btn=Button(root,text="click",command=obj.choose)
btn.pack(padx=10,pady=10)

root.mainloop()
