from tkinter import *
import Backend
import time
import csv

def removewhitespace(delimit,infn):
    csvfile= open(infn,'r')
    csvfile1= open('Out'+infn+time.strftime("%d%m%Y%H%M%S"),'w') 
    stripped = (row.strip() for row in csvfile)
    reader = csv.reader(stripped,delimiter=',')
    writer= csv.writer(csvfile1)
    for row in reader:
       writer.writerow([e.strip() for e in row])
		print('hello'+' '+delimit+' '+infn+time.strftime("%d%m%Y")+time.strftime("%H%M%S"))
    
removewhitespace(';','C:\D_Drive\Value_Sets_new.csv')

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 23:01:19 2018

@author: Rahul.Mishra1
"""

from tkinter import *
import Backend


def view_command():
    lstbx.delete(0,END)
    for row in Backend.view():
        lstbx.insert(END,row)

def search_command():
    lstbx.delete(0,END)
    for row in Backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        lstbx.insert(END,row)

def add_command():
    Backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    lstbx.delete(0,END)
    lstbx.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def update_command():
    Backend.update(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())


def delete_command():


def close_command():


window=Tk()

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

lstbx=Listbox(window,height=6,width=35)
lstbx.grid(row=2,column=0,rowspan=8,columnspan=2)

scrbr=Scrollbar(window)
scrbr.grid(row=2,column=2,rowspan=8)

lstbx.configure(yscrollcommand=scrbr.set)
scrbr.configure(command=lstbx.yview)

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=3,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=6,column=3)

b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=7,column=3)

b6=Button(window,text="Close",width=12,command=close_command)
b6.grid(row=8,column=3)

window.mainloop()