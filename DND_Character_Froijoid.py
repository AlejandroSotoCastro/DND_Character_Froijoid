import math;
import tkinter as tk
from tkinter import *
#tutorialspoint

lvl=6

STR=19
DEX=13
CON=20
INT=12
WIS=14
CHA=7

BAB=[6,1]
willeza=2
fortaleza=5
reflejos=2

def mod(x):
	return  int((((x - (x % 2)) - 10) / 2))	
root = Tk()

root.geometry("500x500")
root.resizable(0,0)


furichek= IntVar() 
fatichek= IntVar()
var = IntVar()
var2 = IntVar()
var3 = IntVar()

def check():

	global lvl

	global STR
	global DEX
	global CON
	global INT
	global WIS
	global CHA

	global BAB
	global willeza
	global fortaleza
	global reflejos
	DAMAGE=0
	MELE=0
	names=["STR","DEX","CON","INT","WIS","CHA"]
	values=[STR,DEX,CON,INT,INT,INT]
	combat=[MELE,DAMAGE,BAB]
	comnames=["MELE","DAMAGE","BAB"]
	for i in range(5):
		lab=Label(root, text=names[i]+"   "+str(values[i])+"   "+str(mod(values[i])))
		lab.place(x=20, y=30+30*i , width=120, height=25)

	if furichek.get()==1:
		values=[STR+4,DEX,CON+6,INT,WIS,CHA]

		lab=Label(text="RONDAS  "+str(lvl+4+mod(CON)+lvl*2-2))
		lab.place(x=114,y=100,width=150,height=25)
		lab=Label(text="VIDA 	"+str((mod(values[2])-mod(CON))*lvl))
		lab.place(x=125,y=120,width=120, height=25)
		lab=Label(text="FORT 	"+str((mod(values[2])+fortaleza)))
		lab.place(x=250,y=100,width=120, height=25)
		lab=Label(text="WILL 	"+str((mod(values[4])+willeza+2+4)))
		lab.place(x=250,y=120,width=120, height=25)


	if fatichek.get()==1:	
		values[0]-=2 
		values[1]-=2
		
	if var.get()==1:
		combat=[MELE+mod(values[0])+BAB[0]+2,DAMAGE+1.5*mod(values[0])+2]
	
		if furichek.get()==1:
			combat[0]+=2
			combat[1]+=2
	elif var.get()==2:
		combat=[MELE+mod(values[0])+BAB[0]+1,DAMAGE+1.5*mod(values[0])+1]
	elif var.get()==3:
		combat=[MELE+mod(values[0])+BAB[0],DAMAGE+mod(values[0])]
	elif var.get()==4:
		combat=[MELE+mod(values[0])+BAB[0]+1,DAMAGE+1.5*mod(values[0])]


	for i in range(5):
		lab=Label(root, text=names[i]+"   "+str(values[i])+"   "+str(mod(values[i])))
		lab.place(x = 20, y = 30+30*i , width=120, height=25)
	for i in range(2):
		lab=Label(root, text=comnames[i]+"   "+str(int(combat[i])))
		lab.place(x=220+80*i, y=150 , width=80, height=25)
	#####################################################################
	if var2.get()==1:
		combat=[MELE+mod(values[0])+BAB[1]+2,DAMAGE+1.5*mod(values[0])+2]
		if furichek.get()==1:
			combat[0]+=2
			combat[1]+=2
	elif var2.get()==2:
		combat=[MELE+mod(values[0])+BAB[1]+1,DAMAGE+1.5*mod(values[0])+1]
	elif var2.get()==3:
		combat=[MELE+mod(values[0])+BAB[1],DAMAGE+0.5*mod(values[0])]
	elif var2.get()==4:
		combat=[MELE+mod(values[0])+BAB[1]+1,DAMAGE+1.5*mod(values[0])]
	for i in range(2):
		lab=Label(root, text=comnames[i]+"   "+str(int(combat[i])))
		lab.place(x=220+80*i, y=175 , width=80, height=25)
	#####################################################################
	if var3.get()==3:
		combat=[MELE+mod(values[0])+BAB[1],DAMAGE+0.5*mod(values[0])]
	for i in range(2):
		lab=Label(root, text=comnames[i]+"   "+str(int(combat[i])))
		lab.place(x=220+80*i, y=201 , width=80, height=25)
check()


furia= Checkbutton (root, text = "Furia",variable=furichek,command=check)

furia.pack()
furia.place(x=150,y=30)

fatigado= Checkbutton (root, text = "Fatigado",variable=fatichek,command=check)
fatigado.pack()
fatigado.place(x=150,y=50)

mb=  Menubutton ( root, text="Ataque 1", relief=RAISED)
mb.pack()
mb.place(x=150,y=150)
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu
mb2=  Menubutton ( root, text="Ataque 2", relief=RAISED)
mb2.place(x=150,y=175)
mb2.menu =  Menu ( mb2, tearoff = 0 )
mb2["menu"] =  mb2.menu
mb3=  Menubutton ( root, text="Ataque 3", relief=RAISED)
mb3.place(x=150,y=200)
mb3.menu =  Menu ( mb3, tearoff = 0 )
mb3["menu"] =  mb3.menu

mb.menu.add_radiobutton(label="Hacha",value=1, variable=var,command=check) 
mb.menu.add_radiobutton(label="Martillo",value=2,variable=var,command=check)
mb.menu.add_radiobutton(label="Cuernos",value=3, variable=var,command=check)
mb.menu.add_radiobutton(label="Pico",value=4, variable=var,command=check)

mb2.menu.add_radiobutton(label="Hacha",value=1, variable=var2,command=check) 
mb2.menu.add_radiobutton(label="Martillo",value=2,variable=var2,command=check)
mb2.menu.add_radiobutton(label="Cuernos",value=3, variable=var2,command=check)
mb2.menu.add_radiobutton(label="Pico",value=4, variable=var2,command=check)

mb3.menu.add_radiobutton(label="Cuernos",value=3, variable=var3,command=check)

root.mainloop()



