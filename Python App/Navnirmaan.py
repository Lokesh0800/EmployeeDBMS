from tkinter import *
from tkinter import ttk
import mysql.connector
import pandas as pd
import time,datetime
import csv
from PIL import Image, ImageTk

class Main(Tk):
    fgg = 'black'
    font_color = "#C34545"
    bg_color = '#b3e0ff'
    frame_bx = '#002e4d'
    msg_color = 'red'
    password = 'lokesh321'
    
    def __init__(self):
        super().__init__()
        screen_wd = self.winfo_screenwidth()
        screen_ht = self.winfo_screenheight()
        self.state('zoomed')
        self.minsize(screen_wd,screen_ht)
        self.title("Navnirmaan Associates")
        self.config(bg='#b3e0ff')
        self.Date = datetime.datetime.now()
        
        self.img = PhotoImage(file='navnirmaan_logo.png')
        self.iconbitmap("logo_icon.ico")
        self.mainmenu()
        
        

    def mainmenu(self):

        for widgets in self.winfo_children():
            widgets.destroy()

        self.image = Label(self,image=self.img, bg=Main.bg_color)
        self.image.place(x=0,y=0)

        self.cont_us = Label(self, text="Contact Us", fg=Main.fgg, bg=Main.bg_color, font='Arial 22 bold')
        self.cont_us.place(x=1300,y=680)

        self.cont1 = Label(self, text="navnirmaan.india62@gmail.com", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont1.place(x=1160,y=720)

        self.cont2 = Label(self, text="+91- 90095 26662", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont2.place(x=1250,y=750)
            
        self.l1 = Label(self, text="WELCOME TO NAVNIRMAAN ASSOCIATES", font='Arial 46 bold',fg=Main.font_color, bg=Main.bg_color)
        self.l1.place(x=200, y=5)
        
        self.f1 = Frame(self, bg=Main.frame_bx, bd=10,relief=SUNKEN, width=800, height=600)
        self.f1.place(x=400, y=120)

        self.l2 = Label(self.f1, text="CLICK BELOW OPTIONS TO PROCEED",font='Arial 28 bold', bg=Main.frame_bx, fg=Main.font_color,)
        self.l2.place(x=50, y=10)
        
        self.material = Button(self.f1, text="MATERIAL", width=15, font='Arial 20 bold', fg=Main.font_color, bg=Main.bg_color, command=self.Material)
        self.material.place(x=100, y=220)

        self.labour = Button(self.f1, text="LABOUR", width=15, fg=Main.font_color, font='Arial 20 bold', bg=Main.bg_color, command=self.Labour)
        self.labour.place(x=440, y=220)

        self.DateTime = Label(self,text=self.Date.strftime("%B %d"),bg=Main.bg_color,fg='black',font='Arial 18 bold')
        self.DateTime.place(x=10,y=750)

    def Material(self):

        for widgets in self.winfo_children():
            widgets.destroy()

        self.image = Label(self,image=self.img, bg=Main.bg_color)
        self.image.place(x=0,y=0)

        self.cont_us = Label(self, text="Contact Us", fg=Main.fgg, bg=Main.bg_color, font='Arial 22 bold')
        self.cont_us.place(x=1300,y=680)

        self.cont1 = Label(self, text="navnirmaan.india62@gmail.com", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont1.place(x=1160,y=720)

        self.cont2 = Label(self, text="+91- 90095 26662", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont2.place(x=1250,y=750)
        
        self.l1 = Label(self, text="NAVNIRMAAN ASSOCIATES", font='Arial 46 bold', fg=Main.font_color, bg=Main.bg_color)
        self.l1.place(x=400, y=5)

        self.f1 = Frame(self,bg=Main.frame_bx, bd=6,relief=GROOVE, width=800, height=600)
        self.f1.place(x=400, y=120)

        self.l2 = Label(self.f1, text="MATERIAL",font='Arial 24 bold', bg=Main.frame_bx, fg=Main.font_color)
        self.l2.place(x=320, y=10)

        self.btn1 = Button(self.f1, text="DATA ENTRY", width=20,font='Arial 16 bold',bg=Main.bg_color, fg=Main.font_color, command=self.Material_Data_Entry_Win)
        self.btn1.place(x=80, y=200)

        self.btn2 = Button(self.f1, text="ACCESS DATA", width=20,font='Arial 16 bold',bg=Main.bg_color, fg=Main.font_color, command=self.Material_Data_Access_Win)
        self.btn2.place(x=420, y=200)

        self.btn3 = Button(self.f1, text="DELETE DATA", width=20,font='Arial 16 bold',bg=Main.bg_color, fg=Main.font_color, command=self.Delete_Material_Win)
        self.btn3.place(x=80, y=300)

        self.btn4 = Button(self.f1, text="CREATE CSV",width=20, font='Arial 16 bold',bg=Main.bg_color, fg=Main.font_color, command=self.Material_CSV)
        self.btn4.place(x=420, y=300)

        self.back = Button(self.f1, text="BACK",width=10, font='Arial 16 bold', fg=Main.font_color,bg=Main.bg_color, command=self.mainmenu)
        self.back.place(y=545)

    def Material_Data_Entry_Win(self):

        for widgets in self.winfo_children():
            widgets.destroy()

        self.image = Label(self,image=self.img, bg=Main.bg_color)
        self.image.place(x=0,y=0)
        
        self.cont_us = Label(self, text="Contact Us", fg=Main.fgg, bg=Main.bg_color, font='Arial 22 bold')
        self.cont_us.place(x=1300,y=680)

        self.cont1 = Label(self, text="navnirmaan.india62@gmail.com", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont1.place(x=1160,y=720)

        self.cont2 = Label(self, text="+91- 90095 26662", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont2.place(x=1250,y=750)
            
        self.l1 = Label(self, text="NAVNIRMAAN ASSOCIATES", font='Arial 46 bold',fg=Main.font_color, bg=Main.bg_color)
        self.l1.place(x=350, y=5)

        self.date = Label(self, text='DATE (YYYY-MM-DD)', pady=20, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.date.place(x=350, y=150)

        self.particular = Label(self, text='PARTICULAR',pady=10, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.particular.place(x=350, y=220)

        self.site = Label(self, text='SITE', pady=10, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.site.place(x=350, y=280)

        self.traders = Label(self, text='TRADERS',pady=10, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.traders.place(x=350, y=340)

        self.quantity = Label(self, text='QUANTITY',pady=10, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.quantity.place(x=350, y=410)

        self.amount = Label(self, text='AMOUNT',pady=10, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.amount.place(x=350, y=480)

        self.date_ent = Entry(self, width=50, font="Arial 16 bold")
        self.date_ent.place(x=650, y=170)

        self.particular_ent = Entry(self, width=50, font="Arial 16 bold")
        self.particular_ent.place(x=650, y=230)

        self.site_ent = Entry(self, width=50, font="Arial 16 bold")
        self.site_ent.place(x=650, y=290)

        self.traders_ent = Entry(self, width=50, font="Arial 16 bold")
        self.traders_ent.place(x=650, y=350)

        self.quantity_ent = Entry(self, width=50, font="Arial 16 bold")
        self.quantity_ent.place(x=650, y=420)

        self.amount_ent = Entry(self, width=50, font="Arial 16 bold")
        self.amount_ent.place(x=650, y=490)
        #self.amount_ent.config(state='disabled')

        self.sub_btn = Button(self, text="ADD",font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color, command=self.Material_Entry)
        self.sub_btn.place(x=650, y=540)

        self.ret_btn = Button(self, text="DASHBOARD",font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color, command=self.Material)
        self.ret_btn.place(x=850, y=540)

        self.frame = Frame(self, bg=Main.frame_bx, bd=6,relief=SUNKEN, width=800, height=200)
        self.frame.place(x=10, y=600)

    def Material_Entry(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

        d0 = self.date_ent.get()
        d1 = self.particular_ent.get()
        d2 = self.site_ent.get()
        d3 = self.traders_ent.get()
        d4 = self.quantity_ent.get()
        d5 = self.amount_ent.get()
        

        if d0 and d1 and d2 and d3 and d4 and d5:

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=Main.password,
                database="NavnirmaanAssociates"
            )
            query = "INSERT INTO material (Date,particular,site,traders,quantity,amount) VALUES (%s,%s,%s,%s,%s,%s)"
            values = (d0, d1, d2, d3, d4, d5)
            try:
                mycursor = mydb.cursor()
                mycursor.execute(query, values)
                mydb.commit()
                mydb.close()
                var = [self.date_ent, self.particular_ent,self.site_ent, self.traders_ent, self.quantity_ent, self.amount_ent]

                for i in var:
                    i.delete(0, 'end')
                    
                l1 = Label(self.frame, text="Data Uploaded Successfully",font='Arial 36 bold', bg=Main.frame_bx, fg='red')
                l1.place(x=100, y=80)
                mydb.close()
            except mysql.connector.IntegrityError as er:
                l1 = Label(self.frame, text="!!!Error,Data Addition Failed",font='Arial 36 bold', bg=Main.frame_bx, fg='red')
                l1.place(x=100, y=80)
                mydb.close()
            except mysql.connector.DatabaseError as er:
                l1 = Label(self.frame, text="!!!Error,Wrong Input",font='Arial 36 bold', bg=Main.frame_bx, fg='red')
                l1.place(x=100, y=80)
                mydb.close()
        else:
            l1 = Label(self.frame, text="!!!Error,Missing Fields",font='Arial 36 bold', bg=Main.frame_bx, fg='red')
            l1.place(x=100, y=80)

    def Material_Data_Access_Win(self):

        for widgets in self.winfo_children():
            widgets.destroy()

        self.image = Label(self,image=self.img, bg=Main.bg_color)
        self.image.place(x=0,y=0)
        
        self.cont_us = Label(self, text="Contact Us", fg=Main.fgg, bg=Main.bg_color, font='Arial 22 bold')
        self.cont_us.place(x=1300,y=680)

        self.cont1 = Label(self, text="navnirmaan.india62@gmail.com", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont1.place(x=1160,y=720)

        self.cont2 = Label(self, text="+91- 90095 26662", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont2.place(x=1250,y=750)
        
        self.name = Label(self, text='NAVNIRMAAN ASSOCIATES', pady=20, font="Arial 46 bold", fg=Main.font_color, bg=Main.bg_color)
        self.name.place(x=350,y=5)
    
        self.site = Label(self, text='SITE', pady=20, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.site.place(x=250, y=150)

        self.Or = Label(self, text='OR', pady=20, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.Or.place(x=450, y=220)

        self.traders = Label(self, text='TRADERS', pady=20, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.traders.place(x=250, y=280)

        self.message = Label(self, text="MESSAGE BOX", pady=20, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.message.place(x=1200, y=90)

        self.site_ent = Entry(self, width=50, font="Arial 16 bold")
        self.site_ent.place(x=450, y=170)

        self.traders_ent = Entry(self, width=50, font="Arial 16 bold")
        self.traders_ent.place(x=450, y=300)

        self.sub_btn = Button(self, text="ACCESS",font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color, command=self.Material_Access)
        self.sub_btn.place(x=350, y=370)

        self.getall = Button(self, text="ACCESS ALL",font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color, command=self.Access_All_Material)
        self.getall.place(x=550, y=370)

        self.ret_btn = Button(self, text="DASHBOARD",font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color, command=self.Material)
        self.ret_btn.place(x=750, y=370)

        self.csv_btn = Button(self, text="CSV",font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color, command=self.Create_Material_CSV)
        self.csv_btn.place(x=950, y=370)
        
        self.frame = Frame(self, bg=Main.frame_bx, bd=6,relief=SUNKEN, width=1200, height=300)
        self.frame.place(x=50, y=440)
        
        self.treev = ttk.Treeview(self.frame)
        self.treev.pack(side="top")
        self.treev["columns"] = ("1", "2", "3","4", "5","6","7")
        self.treev['show'] = 'headings'
        table_headings=["ID","DATE","PARTICULAR","SITE","TRADERS","QUANTITY","AMOUNT"]
        for i in range(len(self.treev["columns"])):
                self.treev.column(self.treev["columns"][i], width = 200, anchor ='c')
                self.treev.heading(self.treev["columns"][i], text =table_headings[i])
            
        self.msgframe = Frame(self, bg=Main.frame_bx, bd=6,relief=SUNKEN, width=400, height=250)
        self.msgframe.place(x=1100, y=150)
            

    def Material_Access(self):

        for widget in self.frame.winfo_children():
            widget.destroy()

        for widget in self.msgframe.winfo_children():
            widget.destroy()
            
        self.treev = ttk.Treeview(self.frame)
        self.treev.pack(side="top")

        self.treev["columns"] = ("1", "2", "3","4", "5","6","7")
        self.treev['show'] = 'headings'
        table_headings=["ID","DATE","PARTICULAR","SITE","TRADERS","QUANTITY","AMOUNT"]
        for i in range(len(self.treev["columns"])):
                self.treev.column(self.treev["columns"][i], width = 200, anchor ='c')
                self.treev.heading(self.treev["columns"][i], text =table_headings[i])
        
        d0 = self.site_ent.get()
        d1 = self.traders_ent.get()

        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=Main.password,
                database="NavnirmaanAssociates"
            )
        
        if d0:
            try:
                self.treev["columns"] = ("1", "2", "3","4", "5","6")
                self.treev['show'] = 'headings'
                table_headings=["ID","DATE","PARTICULAR","TRADERS","QUANTITY","AMOUNT"]
                for i in range(len(self.treev["columns"])):
                    self.treev.column(self.treev["columns"][i], width = 200, anchor ='c')
                    self.treev.heading(self.treev["columns"][i], text =table_headings[i])
                mycursor = mydb.cursor()
                mycursor.execute(f"SELECT Id,DATE_FORMAT(Date,'%d/%c/%Y'),particular,traders,quantity,amount FROM material WHERE site = '{d0}' ORDER BY Date")
                data = mycursor.fetchall()
                if data != []:
                    for k in data:
                        self.treev.insert("", 'end',values =(k[0], k[1], k[2], k[3], k[4], k[5]))
                    l1 = Label(self.msgframe, text="Data Successfully Retrived",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                    l1.place(x=10, y=80)
                    self.traders_ent.delete(0, 'end')
                else:
                    l1 = Label(self.msgframe, text="!!!Error,Site data not found",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                    l1.place(x=10, y=80)
                    self.traders_ent.delete(0, 'end')
            except mysql.connector.errors.ProgrammingError as er:
                l1 = Label(self.msgframe, text="!!!Error,Site name not Exist",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                l1.place(x=10, y=80)
                self.traders_ent.delete(0, 'end')
            mydb.close()
                
        elif d1:
            try:
                self.treev["columns"] = ("1", "2", "3","4", "5","6")
                self.treev['show'] = 'headings'
                table_headings=["ID","DATE","PARTICULAR","SITE","QUANTITY","AMOUNT"]
                for i in range(len(self.treev["columns"])):
                    self.treev.column(self.treev["columns"][i], width = 200, anchor ='c')
                    self.treev.heading(self.treev["columns"][i], text =table_headings[i])
                mycursor = mydb.cursor()
                mycursor.execute(f"SELECT Id,DATE_FORMAT(Date,'%d/%c/%Y'),particular,site,quantity,amount FROM material WHERE traders = '{d1}' ORDER BY Date")
                data = mycursor.fetchall()
                if data != []:
                    for k in data:
                        self.treev.insert("", 'end', text ="L1",values =(k[0], k[1], k[2], k[3], k[4]))
                    l1 = Label(self.msgframe, text="Data Successfully Retrived",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                    l1.place(x=10, y=80)
                    self.site_ent.delete(0, 'end')
                else:
                    l1 = Label(self.msgframe, text="!!!Error,data not found",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                    l1.place(x=10, y=80)
                    self.site_ent.delete(0, 'end')
            except mysql.connector.errors.ProgrammingError as er:
                    l1 = Label(self.msgframe, text="!!!Error,Traders name not Exist",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                    l1.place(x=10, y=80)
                    self.site_ent.delete(0, 'end')
            mydb.close()
        else:
            l1 = Label(self.msgframe, text="!!!Error,Missing Field",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
            l1.place(x=10, y=80)
            self.site_ent.delete(0, 'end')
            self.traders_ent.delete(0, 'end')
            mydb.close()

    def Access_All_Material(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
            
        for widget in self.msgframe.winfo_children():
            widget.destroy()
            
        self.treev = ttk.Treeview(self.frame)
        self.treev.pack(side="top")
        self.treev["columns"] = ("1", "2", "3","4", "5","6","7")
        self.treev['show'] = 'headings'
        self.table_headings=["ID","DATE","PARTICULAR","SITE","TRADERS","QUANTITY","AMOUNT"]
        for i in range(len(self.treev["columns"])):
                self.treev.column(self.treev["columns"][i], width = 200, anchor ='c')
                self.treev.heading(self.treev["columns"][i], text =self.table_headings[i])

        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=Main.password,
                database="NavnirmaanAssociates"
            )
        query = "SELECT Id,DATE_FORMAT(Date,'%d/%c/%Y'),particular,site,traders,quantity,amount FROM material ORDER BY Date"
        mycursor = mydb.cursor()
        mycursor.execute(query)
        data = mycursor.fetchall()  
        for k in data:
                self.treev.insert("", 'end',values =(k[0], k[1], k[2], k[3], k[4], k[5],k[6]))
        l1 = Label(self.msgframe, text="Data Successfully Retrived",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
        l1.place(x=10, y=80)
        self.site_ent.delete(0, 'end')
        self.traders_ent.delete(0, 'end')
        mydb.close()

    def Delete_Material_Win(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.image = Label(self,image=self.img, bg=Main.bg_color)
        self.image.place(x=0,y=0)

        self.cont_us = Label(self, text="Contact Us", fg=Main.fgg, bg=Main.bg_color, font='Arial 22 bold')
        self.cont_us.place(x=1300,y=680)

        self.cont1 = Label(self, text="navnirmaan.india62@gmail.com", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont1.place(x=1160,y=720)

        self.cont2 = Label(self, text="+91- 90095 26662", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont2.place(x=1250,y=750)

        self.name = Label(self, text='NAVNIRMAAN ASSOCIATES', font="Arial 46 bold", fg=Main.font_color, bg=Main.bg_color)
        self.name.place(x=500, y=5)

        self.sitename = Label(self, text='ENTER SITE NAME', pady=20, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.sitename.place(x=250, y=140)
    
        self.sitename_ent = Entry(self, width=50, font="Arial 16 bold")
        self.sitename_ent.place(x=500, y=150)

        self.OR = Label(self, text='OR', pady=20, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.OR.place(x=750, y=190)

        self.data_id = Label(self, text='ENTER ID NUMBER', pady=20, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.data_id.place(x=250, y=260)
    
        self.data_id_ent = Entry(self, width=50, font="Arial 16 bold")
        self.data_id_ent.place(x=500, y=290)

        self.sub_btn = Button(self, text="DELETE",font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color, command=self.Delete_Site)
        self.sub_btn.place(x=500, y=400)

        self.ret_btn = Button(self, text="DASHBOARD",font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color, command=self.Material)
        self.ret_btn.place(x=750, y=400)

        self.msgframe2 = Frame(self,  bd=6,relief=SUNKEN, width=400, height=250, bg=Main.frame_bx)
        self.msgframe2.place(x=1120, y=150)

        self.messagebox2 = Label(self, text='MESSAGE BOX', pady=20, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.messagebox2.place(x=1220, y=80)
      
    def Delete_Site(self):
        d0 = self.sitename_ent.get()
        d1 = self.data_id_ent.get()

        for widget in self.msgframe2.winfo_children():
                widget.destroy()
        if d0:

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=Main.password,
                database="NavnirmaanAssociates"
            )

            try:
                mycursor = mydb.cursor()
                mycursor.execute(f"DELETE FROM material WHERE site = '{d0}'") 
                mydb.commit() 
                l1 = Label(self.msgframe2, text="Successfull,Site Deleted",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                l1.place(x=10, y=90)
                self.sitename_ent.delete(0, 'end')
            except:
                l1 = Label(self.msgframe2, text="!!!Error,Check site name",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                l1.place(x=10, y=90)
            mydb.close()

        elif d1:

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=Main.password,
                database="NavnirmaanAssociates"
            )

            try:
                mycursor = mydb.cursor()
                mycursor.execute(f"DELETE FROM material WHERE Id = {d1}") 
                mydb.commit() 
                l1 = Label(self.msgframe2, text="Successfull,ID Deleted",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                l1.place(x=10, y=90)
                self.data_id_ent.delete(0, 'end')
            except:
                l1 = Label(self.msgframe2, text="!!!Error,Check ID number",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                l1.place(x=10, y=90)
            mydb.close()
            
        else:
            
            l1 = Label(self.msgframe2, text="!!!Error,Missing Field",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
            l1.place(x=10, y=90)
            
        
    def Create_Material_CSV(self):
        d0 = self.site_ent.get()
        d1 = self.traders_ent.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=Main.password,
            database="NavnirmaanAssociates"
        )
        
        if d0:
            try:           
                mycursor = mydb.cursor()
                mycursor.execute(f"SELECT DATE_FORMAT(Date,'%d/%c/%Y'),particular,site,traders,quantity,amount FROM material WHERE site = '{d0}' ORDER BY Date")
                result=mycursor.fetchall()
                c_list = [column[0] for column in mycursor.description]
                try:
                    with open(f'{d0} Site.csv', 'w+', newline='') as csvfile:
                        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csvwriter.writerow(c_list)
                        for row in result:
                            csvwriter.writerow(row)
                except:
                    l1 = Label(self.msgframe, text="  !!!Error,File is already open   ",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                    l1.place(x=10, y=80)
            except:
                l1 = Label(self.msgframe, text="  !!!Error,Site Does Not Exist   ",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                l1.place(x=10, y=80)
            
        elif d1:
            try:
                mycursor = mydb.cursor()
                mycursor.execute(f"SELECT DATE_FORMAT(Date,'%d/%c/%Y'),particular,site,traders,quantity,amount FROM material WHERE traders = '{d1}' ORDER BY Date")
                result=mycursor.fetchall()
                c_list = [column[0] for column in mycursor.description]
                try:
                    with open(f'{d1} Traders.csv', 'w+', newline='') as csvfile:
                        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csvwriter.writerow(c_list)
                        for row in result:
                            csvwriter.writerow(row)
                except:
                    l1 = Label(self.msgframe, text="   Error,File is already open   ",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                    l1.place(x=10, y=80)
            except:
                l1 = Label(self.msgframe, text="   Error,Traders Name Not Exist   ",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                l1.place(x=10, y=80)
        mydb.close()

    def Material_CSV(self):
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=Main.password,
            database="NavnirmaanAssociates"
        )

        query = "SELECT DATE_FORMAT(Date,'%d/%c/%Y'),particular,site,traders,quantity,amount FROM material ORDER BY Date"  
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result=mycursor.fetchall()
        c_list = [column[0] for column in mycursor.description]
        try:
            with open('Materials.csv', 'w+', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csvwriter.writerow(c_list)
                for row in result:
                    csvwriter.writerow(row)
        except:
            pass
        mydb.close()
       
    def Labour(self):
        for widgets in self.winfo_children():
            widgets.destroy()

        self.image = Label(self,image=self.img, bg=Main.bg_color)
        self.image.place(x=0,y=0)

        self.cont_us = Label(self, text="Contact Us", fg=Main.fgg, bg=Main.bg_color, font='Arial 22 bold')
        self.cont_us.place(x=1300,y=680)

        self.cont1 = Label(self, text="navnirmaan.india62@gmail.com", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont1.place(x=1160,y=720)

        self.cont2 = Label(self, text="+91- 90095 26662", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont2.place(x=1250,y=750)
        
        self.l1 = Label(self, text="NAVNIRMAAN ASSOCIATES", font='Arial 46 bold', fg=Main.font_color, bg=Main.bg_color)
        self.l1.place(x=400, y=5)

        self.f1 = Frame(self, bd=6,relief=GROOVE, width=800, height=600, bg=Main.frame_bx)
        self.f1.place(x=400, y=120)

        self.l2 = Label(self.f1, text="LABOUR",font='Arial 24 bold', fg=Main.font_color, bg=Main.frame_bx)
        self.l2.place(x=320, y=10)

        self.btn1 = Button(self.f1, text="DATA ENTRY", width=20,font='Arial 16 bold', fg=Main.font_color, bg=Main.bg_color, command=self.Labour_Data_Entry_Win)
        self.btn1.place(x=80, y=200)

        self.btn2 = Button(self.f1, text="ACCESS DATA", width=20,font='Arial 16 bold', fg=Main.font_color, bg=Main.bg_color, command=self.Labour_Data_Access_Win)
        self.btn2.place(x=420, y=200)

        self.btn3 = Button(self.f1, text="DELETE", width=20,font='Arial 16 bold',fg=Main.font_color, bg=Main.bg_color, command=self.Delete_Labour_Win)
        self.btn3.place(x=80, y=300)

        self.btn4 = Button(self.f1, text="CREATE CSV",width=20, font='Arial 16 bold',fg=Main.font_color, bg=Main.bg_color, command=self.Labour_CSV)
        self.btn4.place(x=420, y=300)

        self.back = Button(self.f1, text="BACK",width=10, font='Arial 16 bold',fg=Main.font_color, bg=Main.bg_color, command=self.mainmenu)
        self.back.place(y=545)

    def Labour_Data_Entry_Win(self):
        
        for widgets in self.winfo_children():
            widgets.destroy()

        self.image = Label(self,image=self.img, bg=Main.bg_color)
        self.image.place(x=0,y=0)

        self.cont_us = Label(self, text="Contact Us", fg=Main.fgg, bg=Main.bg_color, font='Arial 22 bold')
        self.cont_us.place(x=1300,y=680)

        self.cont1 = Label(self, text="navnirmaan.india62@gmail.com", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont1.place(x=1160,y=720)

        self.cont2 = Label(self, text="+91- 90095 26662", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont2.place(x=1250,y=750)
            
        self.name = Label(self, text='NAVNIRMAAN ASSOCIATES', font="Arial 46 bold", fg=Main.font_color, bg=Main.bg_color)
        self.name.place(x=380, y=10)

        self.date = Label(self, text='DATE (YYYY-MM-DD)', pady=20, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.date.place(x=350,y=150)

        self.particular = Label(self, text='PARTICULAR',pady=10, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.particular.place(x=350, y=220)

        self.site = Label(self, text='SITE', pady=10, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.site.place(x=350, y=280)

        self.amount = Label(self, text='AMOUNT',pady=10, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.amount.place(x=350, y=340)

        self.labour_date_ent = Entry(self, width=50, font="Arial 16 bold")
        self.labour_date_ent.place(x=650, y=170)

        self.labour_particular_ent = Entry(self, width=50, font="Arial 16 bold")
        self.labour_particular_ent.place(x=650, y=230)

        self.labour_site_ent = Entry(self, width=50, font="Arial 16 bold")
        self.labour_site_ent.place(x=650, y=290)

        self.labour_amount_ent = Entry(self, width=50, font="Arial 16 bold")
        self.labour_amount_ent.place(x=650, y=350)
        #self.amount_ent.config(state='disabled')

        self.sub_btn = Button(self, text="ADD",font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color, command=self.Labour_Entry)
        self.sub_btn.place(x=650, y=450)

        self.ret_btn = Button(self, text="DASHBOARD",font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color, command=self.Labour)
        self.ret_btn.place(x=850, y=450)

        self.frame = Frame(self, bg=Main.frame_bx, bd=6,relief=SUNKEN, width=800, height=200)
        self.frame.place(x=350, y=550)

    def Labour_Entry(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

        d0 = self.labour_date_ent.get()
        d1 = self.labour_particular_ent.get()
        d2 = self.labour_site_ent.get()
        d3 = self.labour_amount_ent.get()
        

        if d0 and d1 and d2 and d3:

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=Main.password,
                database="navnirmaanassociates"
            )
            query = "INSERT INTO labour (Date,particular,site,amount) VALUES (%s,%s,%s,%s)"
            values = (d0, d1, d2, d3)
            try:
                mycursor = mydb.cursor()
                mycursor.execute(query, values)
                mydb.commit()
                var = [self.labour_date_ent, self.labour_particular_ent,self.labour_site_ent,self.labour_amount_ent]
                for i in var:
                    i.delete(0, 'end')
                l1 = Label(self.frame, text="Data Uploaded Successfully",font='Arial 36 bold', bg=Main.frame_bx, fg=Main.msg_color)
                l1.place(x=30, y=60)
            except mysql.connector.IntegrityError as er:
                l1 = Label(self.frame, text="!!!Error,Data Addition Failed",font='Arial 36 bold', bg=Main.frame_bx, fg=Main.msg_color)
                l1.place(x=30, y=60)
            except mysql.connector.DatabaseError as er:
                l1 = Label(self.frame, text="!!!Error,Wrong Input",font='Arial 36 bold', bg=Main.frame_bx, fg=Main.msg_color)
                l1.place(x=30, y=60)
            mydb.close()
        else:
            l1 = Label(self.frame, text="!!!Error,Missing Fields",font='Arial 36 bold', bg=Main.frame_bx, fg=Main.msg_color)
            l1.place(x=30, y=60)

    def Labour_Data_Access_Win(self):

        for widgets in self.winfo_children():
            widgets.destroy()

        self.image = Label(self,image=self.img, bg=Main.bg_color)
        self.image.place(x=0,y=0)

        self.cont_us = Label(self, text="Contact Us", fg=Main.fgg, bg=Main.bg_color, font='Arial 22 bold')
        self.cont_us.place(x=1300,y=680)

        self.cont1 = Label(self, text="navnirmaan.india62@gmail.com", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont1.place(x=1160,y=720)

        self.cont2 = Label(self, text="+91- 90095 26662", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont2.place(x=1250,y=750)

        self.name = Label(self, text='NAVNIRMAAN ASSOCIATES', pady=20, font="Arial 46 bold", fg=Main.font_color, bg=Main.bg_color)
        self.name.place(x=400)
        
        self.laboursite = Label(self, text='SITE', pady=20, font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color)
        self.laboursite.place(x=250, y=150)

        self.labourparticular = Label(self, text='PARTICULAR', pady=20, font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color)
        self.labourparticular.place(x=250, y=280)

        self.message = Label(self, text='MESSAGE BOX', pady=20, font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color)
        self.message.place(x=1200, y=90)

        self.laboursite_ent = Entry(self, width=50, font="Arial 16 bold")
        self.laboursite_ent.place(x=450, y=170)

        self.labourparticular_ent = Entry(self, width=50, font="Arial 16 bold")
        self.labourparticular_ent.place(x=450, y=300)

        self.sub_btn = Button(self, text="ACCESS",font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color, command=self.Labour_Access)
        self.sub_btn.place(x=350, y=400)

        self.getall = Button(self, text="ACCESS ALL",font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color, command=self.Access_All_Labour)
        self.getall.place(x=550, y=400)

        self.ret_btn = Button(self, text="DASHBOARD",font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color, command=self.Labour)
        self.ret_btn.place(x=750, y=400)

        self.csv_btn = Button(self, text="CSV",font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color, command=self.Create_Labour_CSV)
        self.csv_btn.place(x=950, y=400)

        self.frame = Frame(self, bg=Main.frame_bx, bd=6,relief=SUNKEN, width=1200, height=300)
        self.frame.place(x=50, y=500)

        self.treev = ttk.Treeview(self.frame)
        self.treev.pack(side="top")
        self.treev["columns"] = ("1", "2", "3","4","5")
        self.treev['show'] = 'headings'
        table_headings=["ID","DATE","PARTICULAR","SITE","AMOUNT"]
        for i in range(len(self.treev["columns"])):
                self.treev.column(self.treev["columns"][i], width = 200, anchor ='c')
                self.treev.heading(self.treev["columns"][i], text =table_headings[i])
        
        self.msgframe = Frame(self, bg=Main.frame_bx, bd=6,relief=SUNKEN, width=400, height=250)
        self.msgframe.place(x=1100, y=150)
        
    def Labour_Access(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        for widget in self.msgframe.winfo_children():
            widget.destroy()
        self.treev = ttk.Treeview(self.frame)
        self.treev.pack(side="top")
        self.treev["columns"] = ("1", "2", "3","4")
        self.treev['show'] = 'headings'
        table_headings=["ID","DATE","PARTICULAR","AMOUNT"]
        for i in range(len(self.treev["columns"])):
                self.treev.column(self.treev["columns"][i], width = 200, anchor ='c')
                self.treev.heading(self.treev["columns"][i], text =table_headings[i])

        d0 = self.laboursite_ent.get()
        d1 = self.labourparticular_ent.get()

        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=Main.password,
                database="navnirmaanassociates"
            )

        if d0 and d1:
            self.treev["columns"] = ("1", "2","3")
            self.treev['show'] = 'headings'
            table_headings=["ID","DATE","AMOUNT"]
            for i in range(len(self.treev["columns"])):
                self.treev.column(self.treev["columns"][i], width = 200, anchor ='c')
                self.treev.heading(self.treev["columns"][i], text =table_headings[i])
            try:
                query = f"SELECT Id,DATE_FORMAT(Date,'%d/%c/%Y'),amount FROM labour WHERE site = '{d0}' AND particular = '{d1}' ORDER BY Date"
                mycursor = mydb.cursor()
                mycursor.execute(query)
                data = mycursor.fetchall()
                if data != []:
                    for k in data:
                        self.treev.insert("", 'end', text ="L1",values =(k[0], k[1],k[2]))
                    l1 = Label(self.msgframe, text="Data Successfully Retrived",font='Arial 18 bold', bg=Main.frame_bx, fg=Main.msg_color)
                    l1.place(x=10, y=80)
                    self.laboursite_ent.delete(0, 'end')
                    self.labourparticular_ent.delete(0, 'end')
                else:
                    l1 = Label(self.msgframe, text="!!!Error,data not found",font='Arial 18 bold',bg=Main.frame_bx, fg=Main.msg_color)
                    l1.place(x=10, y=80)
                    self.laboursite_ent.delete(0, 'end')
                    self.labourpartucular_ent.delete(0, 'end')
            except:
                l1 = Label(self.msgframe, text="!!!Error,Data does not Exist",font='Arial 18 bold',bg=Main.frame_bx, fg=Main.msg_color)
                l1.place(x=10, y=80)
                self.laboursite_ent.delete(0, 'end')
                self.labourparticular_ent.delete(0, 'end')
        
        elif d0:
            
            self.treev["columns"] = ("1", "2", "3","4")
            self.treev['show'] = 'headings'
            table_headings=["ID","DATE","PARTICULAR","AMOUNT"]
            for i in range(len(self.treev["columns"])):
                self.treev.column(self.treev["columns"][i], width = 200, anchor ='c')
                self.treev.heading(self.treev["columns"][i], text =table_headings[i])
            try:

                mycursor = mydb.cursor()
                mycursor.execute(f"SELECT Id,DATE_FORMAT(Date,'%d/%c/%Y'),particular,amount FROM labour Where site = '{d0}' ORDER BY Date")
                data = mycursor.fetchall()
                if data != []:
                    for k in data:
                        self.treev.insert("", 'end',values =(k[0], k[1], k[2],k[3]))
                    l1 = Label(self.msgframe, text="Data Successfully Retrived",font='Arial 18 bold',bg=Main.frame_bx, fg=Main.msg_color)
                    l1.place(x=10, y=80)
                    self.laboursite_ent.delete(0, 'end')
                    self.labourparticular_ent.delete(0, 'end')
                else:
                    l1 = Label(self.msgframe, text="!!!Error,Site data not found",font='Arial 18 bold',bg=Main.frame_bx, fg=Main.msg_color)
                    l1.place(x=10, y=80)
                    self.laboursite_ent.delete(0, 'end')
                    self.labourparticular_ent.delete(0, 'end')

            except mysql.connector.errors.ProgrammingError as er:
                l1 = Label(self.msgframe, text="!!!Error,Site not Exist",font='Arial 18 bold',bg=Main.frame_bx, fg=Main.msg_color)
                l1.place(x=10, y=80)
                self.laboursite_ent.delete(0, 'end')
                self.labourparticular_ent.delete(0, 'end')
                

        else:
            l1 = Label(self.msgframe, text="!!!Error,Missing Field",font='Arial 18 bold', bg=Main.frame_bx, fg=Main.msg_color)
            l1.place(x=10, y=80)
            self.laboursite_ent.delete(0, 'end')
            self.labourparticular_ent.delete(0, 'end')

    def Access_All_Labour(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
            
        for widget in self.msgframe.winfo_children():
            widget.destroy()
            
        self.treev = ttk.Treeview(self.frame)
        self.treev.pack(side="top")
        self.treev["columns"] = ("1", "2", "3","4","5")
        self.treev['show'] = 'headings'
        table_headings=["ID","DATE","PARTICULAR","SITE","AMOUNT"]
        for i in range(len(self.treev["columns"])):
                self.treev.column(self.treev["columns"][i], width = 200, anchor ='c')
                self.treev.heading(self.treev["columns"][i], text =table_headings[i])

        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=Main.password,
                database="navnirmaanassociates"
            )
        
        query = "SELECT Id,DATE_FORMAT(Date,'%d/%c/%Y'),particular,site,amount FROM labour ORDER BY Date"
        mycursor = mydb.cursor()
        mycursor.execute(query)
        data = mycursor.fetchall()  
        for k in data:
                self.treev.insert("", 'end',values =(k[0], k[1], k[2], k[3],k[4]))
        l1 = Label(self.msgframe, text="Data Successfully Retrived",font='Arial 18 bold', bg=Main.frame_bx, fg=Main.msg_color)
        l1.place(x=10, y=80)
        mydb.close()
        
    def Create_Labour_CSV(self):
        d0 = self.laboursite_ent.get()
        d1 = self.labourparticular_ent.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=Main.password,
            database="navnirmaanassociates"
        )
        
        if d0 and d1:
            try:
                query = f"SELECT DATE_FORMAT(Date,'%d/%c/%Y'),particular,site,amount FROM labour WHERE site = '{d0}' AND particular = '{d1}' ORDER BY Date"  
                mycursor = mydb.cursor()
                mycursor.execute(query)
                result=mycursor.fetchall()
                c_list = [column[0] for column in mycursor.description]
                try:
                    with open(f'{d0} {d1} Site.csv', 'w+', newline='') as csvfile:
                        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csvwriter.writerow(c_list)
                        for row in result:
                            csvwriter.writerow(row)
                except:
                    l1 = Label(self.msgframe, text="   !!!Error,File is already open    ",font='Arial 18 bold',bg=Main.frame_bx, fg=Main.msg_color)
                    l1.place(x=10, y=80)
                
            except:
                l1 = Label(self.msgframe, text="     !!!Error,Data Not Found    ",font='Arial 18 bold',bg=Main.frame_bx, fg=Main.msg_color)
                l1.place(x=10, y=80)             
            
        elif d0:
            try:
                query = f"SELECT DATE_FORMAT(Date,'%d/%c/%Y'),particular,site,amount FROM labour WHERE site = '{d0}' ORDER BY Date"
                mycursor = mydb.cursor()
                mycursor.execute(query)
                result=mycursor.fetchall()
                c_list = [column[0] for column in mycursor.description]
                try:
                    with open(f'{d0} Site.csv', 'w+', newline='') as csvfile:
                        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csvwriter.writerow(c_list)
                        for row in result:
                            csvwriter.writerow(row)
                    l1 = Label(self.msgframe, text="  Data Successfully Retrived ",font='Arial 18 bold',bg=Main.frame_bx, fg=Main.msg_color)
                    l1.place(x=50, y=80)
                except:
                    l1 = Label(self.msgframe, text="Error,File is already open",font='Arial 18 bold',bg=Main.frame_bx, fg=Main.msg_color)
                    l1.place(x=50, y=80)
            except:
                l1 = Label(self.msgframe, text="    !!!Error,Site Not Exist    ",font='Arial 18 bold',bg=Main.frame_bx, fg=Main.msg_color)
                l1.place(x=10, y=80)
        mydb.close()
    
    def Delete_Labour_Win(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.image = Label(self,image=self.img, bg=Main.bg_color)
        self.image.place(x=0,y=0)

        self.cont_us = Label(self, text="Contact Us", fg=Main.fgg, bg=Main.bg_color, font='Arial 22 bold')
        self.cont_us.place(x=1300,y=680)

        self.cont1 = Label(self, text="navnirmaan.india62@gmail.com", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont1.place(x=1160,y=720)

        self.cont2 = Label(self, text="+91- 90095 26662", fg=Main.fgg, bg=Main.bg_color, font='Arial 18 bold')
        self.cont2.place(x=1250,y=750)

        self.name = Label(self, text='NAVNIRMAAN ASSOCIATES', font="Arial 46 bold",fg=Main.font_color, bg=Main.bg_color)
        self.name.place(x=350, y=10)

        self.sitename = Label(self, text='ENTER SITE NAME', pady=20, font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color)
        self.sitename.place(x=250, y=150)
    
        self.labour_sitename_ent = Entry(self, width=50, font="Arial 16 bold")
        self.labour_sitename_ent.place(x=500, y=170)

        self.OR = Label(self, text='OR', pady=20, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.OR.place(x=500, y=220)

        self.labour_data_id = Label(self, text='ENTER ID NUMBER', pady=20, font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color)
        self.labour_data_id.place(x=250, y=300)
    
        self.labour_data_id_ent = Entry(self, width=50, font="Arial 16 bold")
        self.labour_data_id_ent.place(x=500, y=330)

        self.sub_btn = Button(self, text="DELETE",font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color, command=self.Delete_Labour_Site)
        self.sub_btn.place(x=500, y=420)

        self.ret_btn = Button(self, text="DASHBOARD",font="Arial 16 bold", fg=Main.font_color, bg=Main.bg_color, command=self.Labour)
        self.ret_btn.place(x=700, y=420)

        self.msgframe2 = Frame(self, bg=Main.frame_bx, bd=6,relief=SUNKEN, width=400, height=250)
        self.msgframe2.place(x=1130, y=170)

        self.messagebox2 = Label(self, text='MESSAGE BOX', pady=20, font="Arial 16 bold",fg=Main.font_color, bg=Main.bg_color)
        self.messagebox2.place(x=1250, y=80)
        
    def Delete_Labour_Site(self):
        
        for widget in self.msgframe2.winfo_children():
                widget.destroy()
                
        d0 = self.labour_sitename_ent.get()
        d1 = self.labour_data_id_ent.get()
        if d0:

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=Main.password,
                database="navnirmaanassociates"
            )

            try:
                mycursor = mydb.cursor()
                mycursor.execute(f"DELETE FROM labour WHERE site ='{d0}'")
                mydb.commit() 
                l1 = Label(self.msgframe2, text="Successfull,Site Deleted",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                l1.place(x=15, y=90)
                self.labour_sitename_ent.delete(0, 'end')
            except:
                l1 = Label(self.msgframe2, text="!!!Error,Check Site Name",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                l1.place(x=15, y=90)
                self.labour_sitename_ent.delete(0, 'end')
            mydb.close()

        elif d1:

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=Main.password,
                database="navnirmaanassociates"
            )

            try:
                mycursor = mydb.cursor()
                mycursor.execute(f"DELETE FROM labour WHERE Id = {d1}")
                mydb.commit()  
                l1 = Label(self.msgframe2, text="Successfull,ID Deleted",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                l1.place(x=15, y=90)
                self.labour_data_id_ent.delete(0, 'end')
            except:
                l1 = Label(self.msgframe2, text="!!!Error,Check ID Number",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
                l1.place(x=15, y=90)
                self.labour_data_id_ent.delete(0, 'end')
            mydb.close()
                
        else:
            l1 = Label(self.msgframe2, text="!!!Error,Missing Field",font='Arial 18 bold', fg=Main.msg_color, bg=Main.frame_bx)
            l1.place(x=15, y=90)
            

    def Labour_CSV(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=Main.password,
            database="navnirmaanassociates"
        )

        query = "SELECT DATE_FORMAT(Date,'%d/%c/%Y'),particular,site,amount FROM labour ORDER BY Date"
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result=mycursor.fetchall()
        c_list = [column[0] for column in mycursor.description]
        try:
            with open('Labour.csv', 'w+', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csvwriter.writerow(c_list)
                for row in result:
                    csvwriter.writerow(row)
        except:
            pass
        mydb.close()

if __name__ == "__main__":
    data = Main()
    data.mainloop()
