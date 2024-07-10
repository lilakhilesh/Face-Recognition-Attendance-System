from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        

        title_lb1=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1530,height=45)
        
        
        img_top=Image.open(r"img\image8.jpg")
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1530,height=720)

           
        dev_label=Label(f_lb1,text="Email:=akhilesh.bksc22@gmail.com",font=("times new roman",17,"bold"),bg="white")
        dev_label.place(x=500,y=220)   
           
           
           
           


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()