from tkinter import*
from tkinter import ttk
import datetime
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
from tkcalendar import DateEntry
import mysql.connector
import random,os
import time

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Project")
        self.root.geometry("1440x815+0+10")
        
       
        self.Name=StringVar()
        self.ID=StringVar()
        self.GN=StringVar()
        self.Age=StringVar()
        self.SX=StringVar()
        self.M_Name=StringVar()
        self.M_Price=StringVar()
        self.DOP=StringVar()
        self.MFG=StringVar()
        self.EXP=StringVar()
        self.Ref=StringVar()
        self.Dose=StringVar()
        self.Searchby=StringVar()
        self.Searchtxt=StringVar()
        
       
        lbltitle=Label(self.root,bd=10,relief=RIDGE,text="----------------------------MEDI_GUIDE SYSTEM++++++++++++++++",fg="black",bg="white",font=("times new roman",50,"bold"))
        lbltitle.place(x=0,y=0,width=1440,height=100)
        
        lblbase=Label(self.root,relief=RIDGE,text="Made by Pratik Airy",fg="black",bg="white",font=("times new roman",5,"bold"))
        lblbase.place(x=0,y=200,width=1440,height=300)


        img_snake = Image.open('images/snake.jpg')
        img_snake = img_snake.resize((77, 75), Image.ANTIALIAS)
        self.photosnake = ImageTk.PhotoImage(img_snake)
        b1 = Button(self.root, image=self.photosnake, borderwidth=0)
        b1.place(x=370, y=10)

        img_plus1 = Image.open('images/plus1.png')
        img_plus1= img_plus1.resize((77, 75), Image.ANTIALIAS)
        self.photoplus1 = ImageTk.PhotoImage(img_plus1)
        b2 = Button(self.root, image=self.photoplus1, borderwidth=0)
        b2.place(x=999, y=10)
       

       
        #==============================Dataframe============================
        Dataframe=Frame(self.root,bd=10,relief=RIDGE,bg="gray")
        Dataframe.place(x=0,y=100,width=1440,height=400)

        Dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,bg="yellow")
                                               
        Dataframeleft.place(x=0,y=4,width=472,height=370)                            

        Dataframeright=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,bg="green")
                                                 
        Dataframeright.place(x=949,y=6,width=472,height=370)   

        #==============================Buttonsframe========================

        Buttonframe=Frame(self.root,bd=10,relief=RIDGE,bg="black")  
        Buttonframe.place(x=0,y=500,width=1440,height=60)

         #==============================Detailsframe========================

        Detailsframe=Frame(self.root,bd=10,relief=RIDGE,bg="blue")  
        Detailsframe.place(x=0,y=560,width=1440,height=190)

        #=============================== Dataframeleft=======================

        lblName=Label(Dataframeleft,text="Name",font=("times new roman",15,"bold"),bg="yellow",padx=2,pady=5)
        lblName.grid(row=0,column=0,sticky=W)

        comName=ttk.Combobox(Dataframeleft,textvariable=self.Name,font=("times new roman",15,"bold"),
                                                                              width=23)

        comName["values"]=("Imaginary")
        comName.grid(row=0,column=1)
        comName.place(x=110,y=7)

        lblID=Label(Dataframeleft,font=("times new roman",15,"bold"),text="ID",bg="yellow",padx=2,pady=9)
        lblID.grid(row=1,column=0,sticky=W)
        txtID=Entry(Dataframeleft,font=("times new roman",15,"bold"),textvariable=self.ID,width=25)
        txtID.grid(row=1,column=1)
        txtID.place(x=110,y=35)
       
       
        lblGN=Label(Dataframeleft,text="GN",font=("times new roman",15,"bold"),bg="yellow",padx=2,pady=1)
        lblGN.grid(row=2,column=0,sticky=W)

        comGN=ttk.Combobox(Dataframeleft,textvariable=self.GN,font=("times new roman",15,"bold"),
                                                                              width=23)

        comGN["values"]=("Male","Female")
        comGN.grid(row=2,column=1)
        comGN.place(x=112,y=65)

        lblAge=Label(Dataframeleft,font=("times new roman",15,"bold"),text="Age",bg="yellow",padx=2,pady=2)
        lblAge.grid(row=3,column=0,sticky=W)
        txtAge=Entry(Dataframeleft,font=("times new roman",15,"bold"),textvariable=self.Age,width=25)
        txtAge.grid(row=3,column=1)
        txtAge.place(x=110,y=90)

        lblSX=Label(Dataframeleft,font=("times new roman",15,"bold"),text="SX",bg="yellow",padx=2,pady=5)
        lblSX.grid(row=4,column=0,sticky=W)
        txtSX=Entry(Dataframeleft,font=("times new roman",15,"bold"),textvariable=self.SX,width=25)
        txtSX.grid(row=4,column=1)
        txtSX.place(x=110,y=120)

        lblM_Name=Label(Dataframeleft,font=("times new roman",15,"bold"),text="M_Name",bg="yellow",padx=2,pady=5)
        lblM_Name.grid(row=5,column=0,sticky=W)
        txtM_Name=Entry(Dataframeleft,font=("times new roman",15,"bold"),textvariable=self.M_Name,width=25)
        txtM_Name.grid(row=5,column=1)
        txtM_Name.place(x=110,y=150)

        lblM_Price=Label(Dataframeleft,font=("times new roman",15,"bold"),text="M_Price",bg="yellow",padx=2,pady=5)
        lblM_Price.grid(row=6,column=0,sticky=W)
        txtM_Price=Entry(Dataframeleft,font=("times new roman",15,"bold"),textvariable=self.M_Price,width=25)
        txtM_Price.grid(row=6,column=1)
        txtM_Price.place(x=110,y=179)

        lblDOP=Label(Dataframeleft,font=("times new roman",15,"bold"),text="DOP",bg="yellow",padx=2,pady=5)
        lblDOP.grid(row=7,column=0,sticky=W)
        DOP=DateEntry(Dataframeleft,selectmode='day',date_pattern='yyyy-MM-dd',textvariable=self.DOP,width=21)
        DOP.grid(row=7,column=1)
        DOP.place(x=110,y=210)

        lblMFG=Label(Dataframeleft,font=("times new roman",15,"bold"),text="MFG",bg="yellow",padx=2,pady=2)
        lblMFG.grid(row=8,column=0,sticky=W)
        txtMFG=DateEntry(Dataframeleft,selectmode='day',date_pattern='yyyy-MM-dd',textvariable=self.MFG,width=21)
        txtMFG.grid(row=8,column=1)
        txtMFG.place(x=110,y=235)

        lblEXP=Label(Dataframeleft,font=("times new roman",15,"bold"),text="EXP",bg="yellow",padx=2,pady=3)
        lblEXP.grid(row=9,column=0,sticky=W)
        txtEXP=DateEntry(Dataframeleft,selectmode='day',date_pattern='yyyy-MM-dd',textvariable=self.EXP,width=21)
        txtEXP.grid(row=9,column=1)
        txtEXP.place(x=110,y=260)

        lblRef=Label(Dataframeleft,font=("times new roman",15,"bold"),text="Ref",bg="yellow",padx=2,pady=4)
        lblRef.grid(row=10,column=0,sticky=W)
        txtRef=Entry(Dataframeleft,font=("times new roman",15,"bold"),textvariable=self.Ref,width=25)
        txtRef.grid(row=10,column=1)
        txtRef.place(x=110,y=285)

        lblDose=Label(Dataframeleft,font=("times new roman",15,"bold"),text="Dose",bg="yellow",padx=2,pady=4)
        lblDose.grid(row=11,column=0,sticky=W)
        txtDose=Entry(Dataframeleft,font=("times new roman",15,"bold"),textvariable=self.Dose,width=25)
        txtDose.grid(row=11,column=1)
        txtDose.place(x=110,y=315)

        btnData=Button(Dataframeleft,text="Data",bg="yellow",fg="red",font=("times new roman",15,"bold"),width=10,height=2,padx=0,pady=0,command=self.iData)
        btnData.grid(row=0,column=0)
        btnData.place(x=329,y=309)

       
        #=================================Dataframemiddle=============================
        Dataframemiddle=Frame(self.root,bd=10,relief=RIDGE,bg="red")
        Dataframemiddle.place(x=482,y=115,width=476,height=369)

        #=================================Image========================================
        img_stethoscope = Image.open('images/stethoscope.jpg')
        img_stethoscope = img_stethoscope.resize((215, 147), Image.ANTIALIAS)
        self.photostethoscope = ImageTk.PhotoImage(img_stethoscope)
        b3 = Button(self.root, image=self.photostethoscope, borderwidth=0)
        b3.place(x=492, y=125)

        img_tonic = Image.open('images/tonic.jpeg')
        img_tonic = img_tonic.resize((215, 147), Image.ANTIALIAS)
        self.phototonic = ImageTk.PhotoImage(img_tonic)
        b4 = Button(self.root, image=self.phototonic, borderwidth=0)
        b4.place(x=729, y=125)

        img_tablet1 = Image.open('images/tablet1.jpg')
        img_tablet1= img_tablet1.resize((215, 147), Image.ANTIALIAS)
        self.phototablet1= ImageTk.PhotoImage(img_tablet1)
        b5 = Button(self.root, image=self.phototablet1, borderwidth=0)
        b5.place(x=492, y=295)

        img_injection1 = Image.open('images/injection1.png.jpeg')
        img_injection1= img_injection1.resize((215, 147), Image.ANTIALIAS)
        self.photoinjection1= ImageTk.PhotoImage(img_injection1)
        b6 = Button(self.root, image=self.photoinjection1, borderwidth=0)
        b6.place(x=729, y=295)

        img_heart1 = Image.open('images/heart1.png')
        img_heart1= img_heart1.resize((100, 80), Image.ANTIALIAS)
        self.photoheart1= ImageTk.PhotoImage(img_heart1)
        b7 = Button(self.root, image=self.photoheart1, borderwidth=0)
        b7.place(x=666, y=255)

     #================================Search=========================================
        lblSearch=Label(Dataframemiddle,font=("times new roman",15,"bold"),text="Searchby",bg="red")
        lblSearch.grid(row=0,column=0,sticky=W)
        lblSearch.place(x=3,y=325)

        
        
        comSearch=ttk.Combobox(Dataframemiddle,textvariable=self.Searchby,font=("times new roman",15,"bold"),
                                                                              width=10,state="readonly")

        comSearch["values"]=("Name","ID")
        comSearch.grid(row=0,column=0)
        comSearch.place(x=80,y=325)
        
       
        txtSearch=Entry(Dataframemiddle,textvariable=self.Searchtxt,bd=1,width=10,font=("times new roman",15,"bold"))
        txtSearch.grid(row=0,column=0)
        txtSearch.place(x=190,y=325)

        btnSearch= Button(Dataframemiddle, text = 'Search',bg="green",fg="red",font=("times new roman",15,"bold"),width=5,height=1,padx=1,pady=0,command=self.Search_data)
        btnSearch.place(x=285,y=325)

        btnall= Button(Dataframemiddle, text = 'all detail',bg="green",fg="red",font=("times new roman",15,"bold"),width=5,height=1,padx=2,pady=0,command=self.fetch_data)
        btnall.place(x=370,y=325)


        #================================DataframeRight=================================
        
        self.text=Text(Dataframeright,bg="white")
        self.text.place(x=0,y=0,width=430,height=299)
       
        btnsave= Button(Dataframeright, text = 'Save',bg="green",fg="red",font=("times new roman",15,"bold"),width=10,height=2,padx=0,pady=0,command=self.savefile)
        btnsave.place(x=315,y=310)
    
        btnShow_data= Button(Dataframeright,text = 'Display',bg="white",fg="red",font=("times new roman",15,"bold"),width=10,height=2,padx=0,pady=0,command=self.Show_data)
        btnShow_data.place(x=0,y=310)

       
        #================================Buttons=======================================
        
        btnUpdate=Button(Buttonframe,text="Update",bg="white",fg="red",font=("times new roman",15,"bold"),width=18,height=2,padx=1,pady=0,command=self.Update)
        btnUpdate.grid(row=0,column=1)
        btnUpdate.place(x=0,y=0)

        btnDelete=Button(Buttonframe,text="Delete",bg="gray",fg="red",font=("times new roman",15,"bold"),width=18,height=2,padx=1,pady=0, command=self.iDelete)
        btnDelete.grid(row=0,column=2)
        btnDelete.place(x=375,y=0)

        btnReset=Button(Buttonframe,text="Reset",bg="blue",fg="red",font=("times new roman",15,"bold"),width=18,height=2,padx=1,pady=0,command=self.Reset)
        btnReset.grid(row=0,column=3)
        btnReset.place(x=850,y=0)

        btnExit=Button(Buttonframe,text="Exit",background="black",fg="red",font=("times new roman",15,"bold"),width=18,height=2,padx=1,pady=0,command=self.iExit)
        btnExit.grid(row=0,column=4)
        btnExit.place(x=1240,y=0)

       

        btnSave_data= Button(Buttonframe,text = 'Print',bg="white",fg="red",font=("times new roman",15,"bold"),width=5,height=1,padx=1,pady=0)
        btnSave_data.place(x=670,y=0)



        
        #===================================DetailsTable======================================
        #===================================Scrollbar==================================
        Scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("Name","ID","GN","Age","SX","M_Name","M_Price","DOP","MFG",
                                                               "EXP","Ref","Dose"),xscrollcommand=Scroll_x.set,yscrollcommand= Scroll_y.set)


        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)


        Scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        Scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Name",text="Name")
        self.hospital_table.heading("ID",text="ID")
        self.hospital_table.heading("GN",text="GN")
        self.hospital_table.heading("Age",text="Age")
        self.hospital_table.heading("SX",text="SX")
        self.hospital_table.heading("M_Name",text="M_Name")
        self.hospital_table.heading("M_Price",text="M_Price")
        self.hospital_table.heading("DOP",text="DOP")
        self.hospital_table.heading("MFG",text="MFG")
        self.hospital_table.heading("EXP",text="EXP")
        self.hospital_table.heading("Ref",text="Ref")
        self.hospital_table.heading("Dose",text="Dose")
     
        

        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("Name",width=10)
        self.hospital_table.column("ID",width=10)
        self.hospital_table.column("GN",width=10)
        self.hospital_table.column("Age",width=10)
        self.hospital_table.column("SX",width=10)
        self.hospital_table.column("M_Name",width=10)
        self.hospital_table.column("M_Price",width=10)
        self.hospital_table.column("DOP",width=10)
        self.hospital_table.column("MFG",width=10)
        self.hospital_table.column("EXP",width=10)
        self.hospital_table.column("Ref",width=10)
        self.hospital_table.column("Dose",width=10)
      
        

        self.hospital_table.pack(fill=BOTH,expand=1)

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

        #============================connection==================================
        #============================Functionalitydeclration=====================

    def Show_data(self):
        self.text.insert(END,"Name:\t"+self.Name.get()+"\n")
        self.text.insert(END,"ID:\t"+self.ID.get()+"\n")
        self.text.insert(END,"GN:\t"+self.GN.get()+"\n")
        self.text.insert(END,"Age:\t"+self.Age.get()+"\n")
        self.text.insert(END,"SX:\t"+self.SX.get()+"\n")
        self.text.insert(END,"M_Name:\t"+self.M_Name.get()+"\n")
        self.text.insert(END,"M_Price:\t"+self.M_Price.get()+"\n")

        self.text.insert(END,"DOP:\t"+self.DOP.get()+"\n")
        self.text.insert(END,"MFG:\t"+self.MFG.get()+"\n")
        self.text.insert(END,"EXP:\t"+self.EXP.get()+"\n")
        self.text.insert(END,"Ref:\t"+self.Ref.get()+"\n")
        self.text.insert(END,"Dose:\t"+self.Dose.get()+"\n")
    

  

    def Search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Mother9302",database="project", auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()

        my_cursor.execute("select * from hospital where "+str(self.Searchby.get())+" LIKE'%"+str(self.Searchtxt.get())+"%'")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,value=i)
                conn.commit()
                conn.close()


    def savefile(self):
        myFile = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if myFile is None:
         return
        data = self.text.get(1.0,'end')
        myFile.write(data)
        myFile.close()

    def iData(self):
        
        conn=mysql.connector.connect(host="localhost",user="root",password="Mother9302",database="project", auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("insert into  hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                        self.Name.get(),
                                                                                        self.ID.get(),
                                                                                        self.GN.get(),
                                                                                        self.Age.get(),
                                                                                        self.SX.get(),
                                                                                        self.M_Name.get(),
                                                                                        self.M_Price.get(),
                                                                                        self.DOP.get(),
                                                                                        self.MFG.get(),
                                                                                        self.EXP.get(),
                                                                                        self.Ref.get(),
                                                                                        self.Dose.get()
                                                                                        
                                                                                        
                                                                                                    
                                                                                        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("success","record insereted")



    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Mother9302",database="project", auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                 self.hospital_table.insert("",END,values=i)
        conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row) 
        row=content["values"] 
        self.Name.set(row[0])
        self.ID.set(row[1]),
        self.GN.set(row[2])
        self.Age.set(row[3]) 
        self.SX.set(row[4]),
        self.M_Name.set(row[5]),
        self.M_Price.set(row[6]),
        self.DOP.set(row[7]),
        self.MFG.set(row[8]),
        self.EXP.set(row[9]),
        self.Ref.set(row[10]),
        self.Dose.set(row[11])
        


    def Update(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Mother9302",database="project", auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("Update hospital set  Name=%s , GN=%s, Age=%s, SX=%s, M_Name=%s, M_Price=%s, DOP=%s, MFG=%s, EXP=%s, Ref=%s, Dose=%s  where ID=%s ",(

                                                                                        self.Name.get(),
                                                                                        self.GN.get(),
                                                                                        self.Age.get(),
                                                                                        self.SX.get(),
                                                                                        self.M_Name.get(),
                                                                                        self.M_Price.get(),
                                                                                        self.DOP.get(),
                                                                                        self.MFG.get(),
                                                                                        self.EXP.get(),
                                                                                        self.Ref.get(),
                                                                                        self.Dose.get(),
                                                                                        self.ID.get()
                                                                                        
                                                                                                       
                                                                                        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("success","record updated succesfully")                                                                                

    def iDelete(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Mother9302",database="project", auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        query="Delete from hospital where  ID=%s"
        value=(self.ID.get(),)
        my_cursor.execute(query,value)
        
        conn.commit()
        self.fetch_data()
        conn.close()
        self.Reset()
        messagebox.showinfo("Delete","Patient record has been deleted successfully")

    def Reset(self):
        self.Name.set(""),
        self.ID.set("")
        self.GN.set(""),
        self.Age.set(""),
        self.SX.set(""),
        self.M_Name.set(""),
        self.M_Price.set(""),
        self.DOP.set(""),
        self.MFG.set(""),
        self.EXP.set(""),
        self.Ref.set(""),
        self.Dose.set("")
       
       
             

    def iExit(self):
        iExit=messagebox.askyesno("Medi_Guide System")
        if iExit>0:
            root.destroy()
            return


if __name__ == "__main__":
    root=Tk()
    ob=Hospital(root)
    root.mainloop()



        