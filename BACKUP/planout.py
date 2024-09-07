#!/usr/bin/env python3
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from shapely.geometry import Point, Polygon
from shapely.geometry.polygon import LinearRing, Polygon
from shapely.geometry  import MultiPoint
import tkinter as tk
from tkinter import*
import tkinter.filedialog
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
import os
from sys import exit
import xlwt
from PIL import Image
import datetime

from poly import Poly
from source import Source
from grid import Grid
from polyarea import Polyarea
from polyexp import Polyexp
from diagram import diagram
from tkinter import messagebox 
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo


fp = open("polipar1", 'r')
par1,par2=[],[]
reader = csv.reader(fp, delimiter=' ')
for row in reader:
    par1.append(row[0])
    par2.append(row[1])
fp.close()


# Error  Flags
flaggridnode = 0 
flagpolinode = 0
flagpolishot = 0


root = Tk()
root.title('OBN SURVEY DESIGN')

def OpenFile():
   filename = askopenfilename()

def About():
    print ("Version 1.50 = Marcos Guimaraes")

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File",font=("Sans Bold", 10), menu=filemenu)
filemenu.add_command(label="Spreadsheet file", command=OpenFile)
filemenu.add_command(label="Node polygon file", command=OpenFile)
filemenu.add_command(label="Survey Parameters", command=OpenFile)
filemenu.add_command(label="EXIT", command=exit)
helpmenu = Menu(menu)
menu.add_cascade(label="Help",font=("Sans Bold", 8), menu=helpmenu)
helpmenu.add_command(label="About", command=About)

photo = PhotoImage(file='geomagg3.png')
photo = photo.subsample(2)
photo_label = Label(root, image=photo)
photo_label.image = photo 
photo_label.grid()

Label(root, text='Design 1.51  ',font=("Sans Bold", 8)).grid(row=0,column=5,sticky=NE)
Frame(root, bg="black",width=400, height=400)


#------------ BLOCO  1 ------------------------------------------------------------------------
#######
Label(root, text="_______________________").grid(row=1, column=2, sticky=W)
Label(root, text="Nodes Parameters   ",font=("Sans Bold", 11)).grid(row=2, column=2, sticky=W)
#######
Label(root, text="Nodes space X (m):",font=("Sans Bold", 8)).grid(row=3, column=2,sticky='w')
nodex = DoubleVar()
Entry(root, width=10, textvariable=nodex,font=("Sans Bold", 8)).grid(row=3, column=3,sticky='w')
nodex.set(par1[0])

Label(root, text="       Nodes space Y (m):",font=("Sans Bold", 8)).grid(row=3, column=4,sticky='w')
nodey = DoubleVar()  
Entry(root, width=10, textvariable=nodey,font=("Sans Bold", 8)).grid(row=3, column=5,sticky='w')
nodey.set(par2[0])
#######
Label(root, text="Node grid origx",font=("Sans Bold", 8)).grid(row=4, column=2,sticky='w')
origx = DoubleVar()
Entry(root, width=10, textvariable=origx,font=("Sans Bold", 8)).grid(row=4, column=3,sticky='w')
origx.set(par1[1])
Label(root, text="      Node grid origy: ",font=("Sans Bold", 8)).grid(row=4, column=4,sticky='w')
origy = DoubleVar()
Entry(root, width=10, textvariable=origy,font=("Sans Bold", 8)).grid(row=4, column=5,sticky='w')
origy.set(par2[1])
##########
Label(root, text="Range X (m): ",font=("Sans Bold", 8)).grid(row=5, column=2,sticky='w')
rngy = DoubleVar()
Entry(root, width=10, textvariable=rngy,font=("Sans Bold", 8)).grid(row=5, column=3 ,sticky='w')
rngy.set(par2[3])
Label(root, text="       Range Y (m): ",font=("Sans Bold", 8)).grid(row=5, column=4, sticky='w')
rngx = DoubleVar()
Entry(root, width=10, textvariable=rngx,font=("Sans Bold", 8)).grid(row=5, column=5,sticky='w')
rngx.set(par1[3])
############
Label(root, text="Node Line dir (Deg): ",font=("Sans Bold", 8)).grid(row=6, column=2,sticky='w')
anglex = DoubleVar()
Entry(root, width=10, textvariable=anglex,font=("Sans Bold", 8)).grid(row=6, column=3,sticky='w')
anglex.set(par1[2])
###########
#---------------------------------------------------------------
########
v = IntVar()
v.set(par2[11])
languages = [("Hexagonal"),("Alternate"),("Rectangular"),]
def ShowChoice():
    print(v.get())
for val, language in enumerate(languages):
       Radiobutton(root,text=language,padx = 2,variable=v,command=ShowChoice,
       value=val,font=("Sans Bold", 7),fg ='blue').grid(row =7+val, column=2,sticky=W)
########
#--------------------------------------------------------------
########
ort = IntVar()
ort.set(0)  
languages = [("Parallel"),("Orthogonal"),]
def ShowChoice():
    print(ort.get())
for val, language in enumerate(languages):
    Radiobutton(root, 
     text=language, padx = 2, variable=ort, command=ShowChoice,
     value=val,font=("Sans Bold", 8),fg = 'blue').grid(row =7+val, column=4,sticky=W)
##########

# BLOCO 2 ---------------------------------------------------------------------------
Label(root, text="_______________________").grid(row=10, column=2, sticky=W)
Label(root, text="Shots Parameters   ",font=("Sans Bold", 11)).grid(row=11, column=2, sticky=W)
#########
Label(root, text="Pop space (m):      ",font=("Sans Bold", 8)).grid(row=12, column=2,sticky='w')
shotx = DoubleVar()
Entry(root, width=8, textvariable=shotx,font=("Sans Bold", 8)).grid(row=12, column=3,sticky='w')
shotx.set(par1[4])
Label(root, text="  Array separation Y(m): ",font=("Sans Bold", 8)).grid(row=12, column=4,sticky='w')
shoty = DoubleVar()
Entry(root, width=8, textvariable=shoty,font=("Sans Bold", 8)).grid(row=12, column=5,sticky='w')
shoty.set(par2[4])
########
Label(root, text="Grid orig x: ",font=("Sans Bold", 8)).grid(row=13, column=2,sticky='w')
origxa = DoubleVar()
Entry(root, width=8, textvariable=origxa,font=("Sans Bold", 8)).grid(row=13, column=3,sticky='w')
origxa.set(par1[5])
Label(root, text="  Grid orig y: ",font=("Sans Bold", 8)).grid(row=13, column=4,sticky='w')
origya = DoubleVar()
Entry(root, width=8, textvariable=origya,font=("Sans Bold", 8)).grid(row=13, column=5,sticky='w')
origya.set(par2[5])
########
Label(root, text="Shot Line dir (Deg): ",font=("Sans Bold", 8)).grid(row=14, column=2,sticky='w')
anglexa = DoubleVar()
Entry(root, width=8, textvariable=anglexa,font=("Sans Bold", 8)).grid(row=14, column=3,sticky='w')
anglexa.set(par1[6])
Label(root, text="  Halo (m): ",font=("Sans Bold", 8)).grid(row=14, column=4,sticky='w')
halo = DoubleVar()
Entry(root, width=8, textvariable=halo,font=("Sans Bold", 8)).grid(row=14, column=5,sticky='w')
halo.set(par2[6])
########
Label(root, text="Range x (m): ",font=("Sans Bold", 8)).grid(row=15, column=2,sticky='w')
rngxa = DoubleVar()
Entry(root, width=8, textvariable=rngxa,font=("Sans Bold", 8)).grid(row=15, column=3,sticky='w')
rngxa.set(par1[7])
Label(root, text="  Range  y (m): ",font=("Sans Bold", 8)).grid(row=15, column=4,sticky='w')
rngya = DoubleVar()
Entry(root, width=8, textvariable=rngya,font=("Sans Bold", 8)).grid(row=15, column=5,sticky='w')
rngya.set(par2[7])
#######
#-----------------------------------------------------------------------------
#######
nfontes = IntVar()
option = int(par1[11])
nfontes.set(option)
lname = [("Single Source"), ("Dual Source"), ("Triple Source"),]
def ShowChoice():
    print(nfontes.get())
for val, lname in enumerate(lname):
  Radiobutton(root,text=lname, variable=nfontes,
      command=ShowChoice,value=val+1,font=("Sans Bold", 7),fg = 'blue').grid(row =17+val, 
      column=2, sticky=W)
#########
#------------------------------------------------------------------
#########
ort1 = IntVar()
ort1.set(0)  
languages = [("Parallel"),("Orthogonal"),]

def ShowChoice():
    print(ort1.get())
for val, language in enumerate(languages):
    Radiobutton(root,text=language,padx=2,variable=ort1, command=ShowChoice,
    value=val,font=("Sans Bold", 8),fg = 'blue').grid(row =18+val, column=4,sticky=W)
#########

###_-------------------------------------------------------------------------------
#########
root1 = Frame(root)
tkvar = StringVar(root1)
choices = { 'ProvidedPolygon','CaioExpansion'}
tkvar.set('ProvidedPolygon') # set the default option 
popupMenu = OptionMenu(root, tkvar, *choices)
popupMenu.config(font=('Impact',7))
menu = popupMenu.nametowidget(popupMenu.menuname)
menu.configure(font=('Impact', 7))
popupMenu.grid(row = 15, column=0, sticky=W)
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
# link function to change dropdown
tkvar.trace('w', change_dropdown)
#############

# BLOCO 3 ---------------------------------------------------------------------------
Label(root, text="_______________________").grid(row=20, column=2, sticky=W)
Label(root, text="Survey Parameters  ",font=("Sans Bold", 11)).grid(row=21, column=2, sticky=W)
#########
Label(root, text="Source speed (kts): ",font=("Sans Bold", 8)).grid(row=22, column=2,sticky='w')
velshot = DoubleVar()
Entry(root, width=8, textvariable=velshot,font=("Sans Bold", 8)).grid(row=22, column=3,sticky='w')
velshot.set(par1[12])
Label(root, text="   ROV speed (kts): ",font=("Sans Bold", 8)).grid(row=22, column=4,sticky='w')
velnode = DoubleVar()
Entry(root, width=8, textvariable=velnode,font=("Sans Bold", 8)).grid(row=22, column=5,sticky='w')
velnode.set("1.")
#########
Label(root, text="Line chg (Hours) : ",font=("Sans Bold", 8)).grid(row=23, column=2,sticky='w')
chglinetime = DoubleVar()
Entry(root, width=8, textvariable=chglinetime,font=("Sans Bold", 8)).grid(row=23, column=3,sticky='w')
chglinetime.set(par2[12])
Label(root, text="   Maxoffset (m): ",font=("Sans Bold", 8)).grid(row=23, column=4,sticky='w')
MaxOff = DoubleVar()
Entry(root, width=8, textvariable=MaxOff,font=("Sans Bold", 8)).grid(row=23, column=5,sticky='w')
MaxOff.set(par2[6])
########
Label(root, text="Lines before shot: ",font=("Sans Bold", 8)).grid(row=24, column=2,sticky='w')
PreNodeLines = DoubleVar()
Entry(root, width=8, textvariable=PreNodeLines,font=("Sans Bold", 8)).grid(row=24, column=3,sticky='w')
PreNodeLines.set("3")
Label(root, text="   ESPG : ",font=("Sans Bold", 8)).grid(row=24, column=4,sticky='w')
espg = StringVar()
Entry(root, width=10, textvariable=espg,font=("Sans Bold", 8)).grid(row=24, column=5,sticky='w')
espg.set(par2[9])
#########
Label(root, text="Project :     ",font=("Sans Bold", 8)).grid(row=25, column=2,sticky=W)
ProjName = StringVar()
Entry(root, width=10, textvariable=ProjName,font=("Sans Bold", 8)).grid(row=25, column=3,sticky='w')
ProjName.set(par1[8])
Label(root, text="   Client :     ",font=("Sans Bold", 8)).grid(row=25, column=4,sticky=W)
Co = StringVar()
Entry(root, width=10, textvariable=Co,font=("Sans Bold", 8)).grid(row=25, column=5,sticky='w')
Co.set(par2[8])
#########
Label(root, text="Option : ",font=("Sans Bold", 8)).grid(row=26, column=2,sticky=W)
Option = StringVar()
Entry(root, width=10, textvariable=Option,font=("Sans Bold", 8)).grid(row=26, column=3,sticky='w')
Option.set(par1[9])
########
Label(root, text="Vers: ",font=("Sans Bold", 8)).grid(row=27, column=2,sticky=W)
Version = StringVar()
Entry(root, width=10, textvariable=Version,font=("Sans Bold", 8)).grid(row=27, column=3,sticky='w')
Version.set(par1[10])
########
#FOCA!!!!
########
Label(root, text="  Record length (s)",font=("Sans Bold", 8)).grid(row=26, column=4,sticky=W)
rl = StringVar()
Entry(root, width=10, textvariable=rl,font=("Sans Bold", 8)).grid(row=26, column=5,sticky='w')
rl.set(par1[14])
########
Label(root, text="  Water depth (m) ",font=("Sans Bold", 8)).grid(row=27, column=4,sticky=W)
wd = StringVar()
Entry(root, width=10, textvariable=wd,font=("Sans Bold", 8)).grid(row=27, column=5,sticky='w')
wd.set(par2[14])
########

#---------------------------------------------NODES PLOT SELECT--------------------------------------------------------
########
var1a = IntVar()
Checkbutton(root, text=' Plot node polygon  ',font=("Sans Bold", 9), variable=var1a ).grid(row =3, column=0, sticky=W)
var1a.set("1")
var1b = IntVar()
Checkbutton(root, text=' Plot nodes  ',font=("Sans Bold", 9), variable=var1b ).grid(row =4, column=0, sticky=W)
var1b.set("1")
var1c = IntVar()
Checkbutton(root, text=' Plot node grid origin  ',font=("Sans Bold", 9), variable=var1c ).grid(row =5, column=0, sticky=W)
var1c.set("1")
##########
#---------------------------------------------GRID PLOT SELECT -------------------------------------------------------------
########
var2a = IntVar()
Checkbutton(root, text=' Plot shot polygon ',font=("Sans Bold", 9), variable=var2a ).grid(row =6, column=0,sticky=W)
var2a.set=("0")
var2b = IntVar()
Checkbutton(root, text=' Plot grid points  ',font=("Sans Bold", 9), variable=var2b ).grid(row =7, column=0, sticky=W)
var2b.set("0")
var2c = IntVar()
Checkbutton(root, text=' Plot grid origin  ',font=("Sans Bold", 9), variable=var2c ).grid(row =8, column=0, sticky=W)
var2c.set("0")
#########
#------------------Reading  Node polygon--------------
def rnodes():
 global xp,yp
 X=[]
 xp,yp=[],[]

 with open('pol2.txt','r') as f1:
     reader = csv.reader(f1, delimiter=' ')
     next(reader)
     for row in reader:
      xp.append(float(row[0]))
      yp.append(float(row[1]))

 for k in range(0,len(xp)):
      X.append([float(xp[k]),float(yp[k])])
 poly=Polygon(X)
 PO=Polyarea(xp,yp)
 ring = LinearRing(X)
 s=Polygon(ring)
 global NodeArea, flagpolinode

 NodeArea=PO.getarea()
 flagpolinode = 1
 print ('     ')
 print ('Node Poligons -------------------------------')
 print ('Node polygon - Polyarea (SQ Km)', PO.getarea())
# print ('Node polygon order clockwise?' , PO.getorder())
 print ('Node polygon (SQ Km)', s.area/1000000)
 print ('     ')
 
#------------------Node Grid Generation -----------------------------
 global x0,y0
 global XX,YY
 global NumberofNodes
 global NumberofNodeLines
 global LineNumber, NodeNumber , FNL , LNL, flaggridnode

 XX,YY=[],[]
 rangex=rngx.get()
 rangey=rngy.get()
 x0=origx.get()
 y0=origy.get()
 dx=nodex.get()
 dy=nodey.get()
 nx=int(rangex/dx) #+2
 ny=int(rangey/dy) #+2
 angle = anglex.get()
 angle1=angle
 if v.get() ==0:
   angle1+=30.
 stagger=0
 if v.get() == 1:
  stagger=1
 f = open('nodes.txt', 'w') 

 XX,YY=[],[]

 o1=ort.get()

 CQ=Grid(x0,y0,dx,dy,nx,ny,angle,angle1,stagger,o1)

 x= CQ.getarrx()
 y= CQ.getarry()
 nnx= CQ.getnnx() 
 nny= CQ.getnny()  

 f.write("%s\n" % 'x y s l')

 NumberofNodes=0
 NumberofNodeLines=0
 ntotal=len(x)

###
 a=PB(400,20)
 a.settitle("Nodes Computation")
 a.open()
 upt=0
 progress=1./ntotal
###

 LineNumber=[]
 ###NodeNumber=[]
 FNL=[]
 LNL=[]
 savenode =0
 for k in range(0,nny):
###
   a.update(upt)
###

   flagline = 0
   flagnode = 0

   for l in range(0,nnx):
     aa= poly.contains(Point([float(x[k][l]),float(y[k][l])])) ####2
     bb= ring.contains(Point([float(x[k][l]),float(y[k][l])]))  ### Inclui os nodes on the polygon boundary
     if aa or bb:
      NumberofNodes+=1     # count all nodes in and on the node polygon
      XX.append(float(x[k][l]))
      YY.append(float(y[k][l]))

      aax=x[k][l]
      aay=y[k][l]
      if flagnode==0:
         LineNumber.append(k)
         FNL.append(l)
      if flagline==0:
        if flagnode==0:    #skiping the 1st node - no last node saved yet
          if  savenode!=0:
             LNL.append(savenode)
      f.write("%7.2f %7.2f %i %i\n" % (aax,aay,k,l))
      flagnode = 1   # Stops in the 1st node of the line
      savenode = l   #  Saving the last node  
   flagline = 1      # Stops  in the end node  of each line
   upt=upt+progress
 flaggridnode=1
 LNL.append(savenode)
 f1.close()
 f.close()

###
 a.close()
###

#------------------Shot Grid Generation -------------------------------------------
#
def rshots():

 X3=[]

 global x0a,y0a,x0b,y0b
 global XXgrid,YYgrid
 global xp3,yp3
 global NumberofSailPoints
 global NumberofSailLines 
 global ShotArea
 global nsources,nfontes,dxa,dya
 global NumberofShotPoints,NumberofShotLines,AvSailKm_1,AvShotKm_1,TotalShootTimeHours,TotalShootTimeDays
 global ShotsPerKm2,LinearSailKm,LinearShotKm
 global flagpolishot

 xp3,yp3=[],[]

# Check which source polygon to be used

 if tkvar.get()== 'ProvidedPolygon' :
  e=open('polshot.txt','w')
  with open('pol3.txt','r') as f2:
     reader = csv.reader(f2, delimiter=' ')
     next(reader)
     for row in reader:
      xp3.append(float(row[0]))  
      yp3.append(float(row[1]))
  e.write("%s %s\n" % ("x","y"))
  for i in range (0,len(xp3)):
   e.write("%7.2f %7.2f\n" % (float(xp3[i]),float(yp3[i])))

 if tkvar.get()== 'CaioExpansion':
  e=open('polshot.txt','w')
  C=Poly(xp,yp,halo.get())
  xp3=C.getpxe()
  yp3=C.getpye()
  e.write("%s %s\n" % ("x","y"))
  for i in range (0,len(xp3)):
   e.write("%7.2f %7.2f\n" % (float(xp3[i]),float(yp3[i])))

# if tkvar.get()=='CaioExpRounded':  
#    e=open('polshot.txt','w')
#    C=Poly(xp,yp,halo.get())
#    xp3=C.getpxe()
#    yp3=C.getpye()
#    C1=Polyexp(xp3,yp3,halo.get())
#    xp3=C1.getpex()
#    yp3=C1.getpey()
#    e.write("%s %s\n" % ("x","y"))
#    for i in range (0,len(xp3)):
#      e.write("%7.2f %7.2f\n" % (float(xp3[i]),float(yp3[i])))

 for k in range(0,len(xp3)):
      X3.append([float(xp3[k]),float(yp3[k])])
 polyshot = Polygon(X3)
 ring = LinearRing(X3)
 s = Polygon(ring)
 ShotArea = s.area/1000000
 print ('     ')
 print ('Shot poligons -------------------------------')
 print ('Shot polygon (SQ Km)', s.area/1000000)
 flagpolishot=1

#------------------Sail(Shot) Line Grid ------------------
#  Grid is based on shot arrays  configuration 
#
 LLgrid,PPgrid=[],[]
 XXgrid,YYgrid=[],[]
 LINgrid,PTNgrid=[],[]

 rangexa=rngxa.get()
 rangeya=rngya.get()
 x0a=origxa.get()
 y0a=origya.get()
 dxa=shotx.get()
 dya=shoty.get()
 nsources = nfontes.get()        #Nsources.get()
 anglea = anglexa.get()
 angleb=anglea  
 o1=ort1.get()
 ang = anglea*np.pi/180.
 stagger = 0
 nxa=int(rangexa/dxa)
 nya=int(rangeya/dya)

 if nsources==1:
    dxb =dxa
    dyb=dya
 if nsources==2:
    dxb=dxa/2
    dyb=dya/2
 if nsources==3:             # TRIPLE SOURCE 
    dxb=dxa/2
    dyb=dya
    dxb=dxb*nsources
 nxb=int(rangexa/dxb)
 nyb=int(rangeya/dyb)

 CQgrid=Grid(x0a,y0a,dxb,dyb,nxb,nyb,anglea,angleb,stagger,o1)

 nnx=    CQgrid.getnnx()
 nny=    CQgrid.getnny()
 xgrid=  CQgrid.getarrx()
 ygrid=  CQgrid.getarry()

 grid = open('grid.txt', 'w')
 sht =   open('shots.txt', 'w')
 sail =  open('sail.txt', 'w')
 grid.write("%s\n" % 'x y l s')
 sht.write("%s\n" % 'x y l s')
 sail.write("%s\n" % 'x y l s')

 ntotal=len(xgrid)
 a=PB(400,20)
 a.settitle("Grid lines Computation")
 a.open()
 upt=0
 progress=1./ntotal

 SailLineInterval = dya    # Adjascent arrays separation. 
 SailPointInterval = dyb   # pop interval
 FirstSailLine = 1
 FirstSailLineNumber = 1000
 SailLineIntervalIdx = 1 #int(dya/dyb)
 SailPointIntervalIdx = 1

 for GridLine in range(0,nny):
    a.update(upt)
    for GridPoint in range(0,nnx):
          XXgrid.append(float(xgrid[GridLine][GridPoint]))
          YYgrid.append(float(ygrid[GridLine][GridPoint]))
          LLgrid.append([GridLine,GridPoint])
          LINgrid.append([GridLine])
          PTNgrid.append([GridPoint])
          grid.write("%7.2f %7.2f %2i %2i\n" % (xgrid[GridLine][GridPoint],ygrid[GridLine][GridPoint],GridLine,GridPoint))
    upt=upt+progress
 a.close()

 A=LLgrid[-1]
 B=LLgrid[0]
 ny= A[0]-B[0]+1
 nx= A[1]-B[1]+1
 print ("nx,ny",nnx,nny,nx,ny,A[0],B[0],A[1],B[1],len(A),len(B))
 
 GRIDXX=np.reshape((np.asarray(XXgrid)),(ny,nx))
 GRIDYY=np.reshape((np.asarray(YYgrid)),(ny,nx))
 GRIDLN=np.reshape((np.asarray(LINgrid)),(ny,nx))
 GRIDPT=np.reshape((np.asarray(PTNgrid)),(ny,nx))
 print("GRIDXX,GRIDYY,GRIDLN,GRIDPT", GRIDXX.shape,GRIDYY.shape,GRIDLN.shape,GRIDPT.shape)
 
 print  ("GRID VALUES", GRIDLN[0][0],GRIDLN[-1][-1])

 ntotal=len(XXgrid)
 a=PB(400,20)
 a.settitle("Sail lines Computation")
 a.open()
 upt=0
 progress=1./ny

 adv=int(nsources)
 if nsources==1:
     interv = int(dya/dyb)
 if nsources==2: 
     interv =int(2*adv)
 if nsources==3:
     interv=2
     adv=0

 sailint = 1
 sailflag= 0

 for jj in range(0,ny-1,interv):
    a.update(upt)
    for ii in  range(0,nx-interv,interv):
     InsidePoints  = polyshot.contains(Point([float(GRIDXX[jj][ii]),float(GRIDYY[jj][ii])]))
#     OutsidePoints = ring.contains(Point([float(GRIDXX[jj][ii]),float(GRIDYY[jj][ii])]))
     if InsidePoints: # or OutsidePoints:

      if nsources ==2:
        sht.write("%7.2f %7.2f %2i %2i\n" % ((GRIDXX[jj][ii]),(GRIDYY[jj][ii]),GRIDLN[jj][ii],GRIDPT[jj][ii]))
        sht.write("%7.2f %7.2f %2i %2i\n" % ((GRIDXX[jj+adv][ii+adv]),(GRIDYY[jj+adv][ii+adv]),GRIDLN[jj+adv][ii+adv],GRIDPT[jj+adv][ii+adv]))
        sail.write("%7.2f %7.2f %2i %2i\n" % ((GRIDXX[jj+1][ii+1]),(GRIDYY[jj+1][ii+1]),GRIDLN[jj+1][ii+1],GRIDPT[jj+1][ii+1]))
      if nsources ==1:
        sht.write("%7.2f %7.2f %2i %2i\n" % (float(GRIDXX[jj][ii]),float(GRIDYY[jj][ii]),GRIDLN[jj][ii],GRIDPT[jj][ii]))
        sail.write("%7.2f %7.2f %2i %2i\n" % (float(GRIDXX[jj][ii]),float(GRIDYY[jj][ii]),GRIDLN[jj][ii],GRIDPT[jj][ii]))
      if nsources ==3: 
        sht.write("%7.2f %7.2f %2.1f %2.1f\n" % ((GRIDXX[jj][ii]),(GRIDYY[jj][ii]),GRIDLN[jj][ii],GRIDPT[jj][ii]))
#        sht.write("%7.2f %7.2f %2.1f %2.1f\n" % ((GRIDXX[jj+adv][ii+adv]),(GRIDYY[jj+adv][ii+adv]),GRIDLN[jj+adv][ii+adv],GRIDPT[jj+adv][ii+adv]))
        sht.write("%7.2f %7.2f %2.1f %2.1f\n" % ((GRIDXX[jj+adv+1][ii+adv+1]),(GRIDYY[jj+adv+1][ii+adv+1]),GRIDLN[jj+adv+1][ii+adv+1],GRIDPT[jj+adv+1][ii+adv+1]))

# -------- Loop for sailines 

     if nsources == 3 and (jj+sailint) <ny-1:
        DentroPoints  = polyshot.contains(Point([float(GRIDXX[jj+sailint][ii]),float(GRIDYY[jj+sailint][ii])]))
        OutsidePoints = ring.contains(Point([float(GRIDXX[jj+sailint][ii]),float(GRIDYY[jj+sailint][ii])]))
        if DentroPoints or OutsidePoints:
          inc = sailint%2
          sail.write("%7.2f %7.2f %2i %2i\n" % ((GRIDXX[jj+sailint][ii+inc]),(GRIDYY[jj+sailint][ii+inc]),GRIDLN[jj+sailint][ii+inc],GRIDPT[jj+sailint][ii+inc]))
          sailflag = 1
    if sailflag == 1 :
      sailint=sailint+1
    upt=upt+progress
 a.close()

 upt=upt+progress
 a.close()
 grid.close()
 sail.close()
 sht.close()
 planout()

#--------------------------------------------------------------------------------------------------
def planout ():

# img = Image.open("geomagg3.bmp")
# r, g, b, a = img.split()
# img =Image.merge("RGB", (r,g,b))
# img.save('geomagg3.bmp')

 book = xlwt.Workbook(encoding="utf-8")

 sheet0 = book.add_sheet("Parameters")
 sheet1 = book.add_sheet("Nodes")
 sheet2 = book.add_sheet("Nodes_Polygon")
 sheet3 = book.add_sheet("Shots")
 sheet4 = book.add_sheet("Shots_polygon")
 sheet5 = book.add_sheet("Fold x Offset")
 sheet7 = book.add_sheet("SailLines")

# Defining styles
 style= xlwt.easyxf(' font: name Arial, bold on; borders: left thick,  right thick,top thick, bottom thick;  pattern: pattern solid, fore_colour gray25 ;')
 style1= xlwt.easyxf('font: name Arial, bold on; borders: left thick,  right thick,top thick, bottom thick;  pattern: pattern solid, fore_colour light-yellow;')
 style2= xlwt.easyxf(' font: name Arial, bold on; borders: left thick,  right thick,top thick, bottom thick;  pattern: pattern solid, fore_colour ivory ;')
 style3= xlwt.easyxf(' font: name Arial, bold on; borders: left thick,  right thick,top thick, bottom thick;  pattern: pattern solid, fore_colour lime ;')
 style4a= xlwt.easyxf(' font: bold on , height 220;')
 style4= xlwt.easyxf(' font: bold on , height 200; pattern: pattern solid, fore_colour white ;')
 style4d= xlwt.easyxf(' font: bold on , height 200; pattern: pattern solid, fore_colour light_turquoise ;')
 style4e= xlwt.easyxf(' font: bold on , height 200; pattern: pattern solid, fore_colour light-turquoise ;')
 style4f= xlwt.easyxf(' font: bold on , height 200; pattern: pattern solid, fore_colour light_green ;')
 style4b= xlwt.easyxf(' font: bold on , height 200; pattern: pattern solid, fore_colour ivory ;')
 style4c= xlwt.easyxf(' font: bold on , height 200; pattern: pattern solid, fore_colour light-blue ;')
 style5= xlwt.easyxf('font: name Arial, bold on; borders: left thick,  right thick,top thick, bottom thick;  pattern: pattern solid, fore_colour light-blue ')
 style6= xlwt.easyxf('font: name Arial, bold on, height 220; borders: bottom medium, top medium;  pattern: pattern solid, fore_colour light-orange ')
 style6a= xlwt.easyxf('font: name Arial, bold on, height 220; borders: bottom medium, top medium, right medium;  pattern: pattern solid, fore_colour light-orange ')
 style6b= xlwt.easyxf('font: name Arial, bold on, height 220; borders: bottom medium, top medium, left medium;  pattern: pattern solid, fore_colour light-orange ')
 style7= xlwt.easyxf('font: colour white, name Arial, bold on, height 200; borders: bottom medium, top medium;  pattern: pattern solid, fore_colour light-blue ')
 style7a= xlwt.easyxf('font: colour white, name Arial, bold on, height 200; borders: bottom medium, top medium, right medium;  pattern: pattern solid, fore_colour light-blue ')
 style7b= xlwt.easyxf('font: colour white, name Arial, bold on, height 200; borders: bottom medium, top medium, left medium;  pattern: pattern solid, fore_colour light-blue ')
 style9= xlwt.easyxf('font: colour white, name Arial, bold on, height 200; borders: bottom medium, top medium;  pattern: pattern solid, fore_colour green ')
 style9a= xlwt.easyxf('font: colour white, name Arial, bold on, height 200; borders: bottom medium, top medium, right medium;  pattern: pattern solid, fore_colour green ')
 style9b= xlwt.easyxf('font: colour white, name Arial, bold on, height 200; borders: bottom medium, top medium, left medium;  pattern: pattern solid, fore_colour green ')

 style8= xlwt.easyxf(' font: bold off , height 140;')

# sheet0.insert_bitmap('geomagg3.png',0,0)
 stylex= xlwt.XFStyle()
 stylex.num_format_str= 'M/D/YY' #'D-MMM-YY'
 sheet0.write(1,6,datetime.datetime.now(), stylex)

 sheet0.write(0,0, "      ",style6b)
 sheet0.write(0,1, "",style6)
 sheet0.write(0,2, "      ",style6)
 sheet0.write(0,3, "GEOMAGG",style6)
 sheet0.write(0,4, "      ",style6)
 sheet0.write(0,5, "      ",style6)
 sheet0.write(0,6, "      ",style6a)

 sheet0.write(9,1, "      ",style6)
 sheet0.write(9,0, "Nodes",style6b)
 sheet0.write(9,2, "      ",style6)
 sheet0.write(9,3, "      ",style6)
 sheet0.write(9,4, "Shots      ",style6)
 sheet0.write(9,5, "      ",style6)
 sheet0.write(9,6, "      ",style6a)

 sheet0.write(2,0, ProjName.get(),style4e)
 sheet0.write(4,0, Co.get(),style4e)
 sheet0.write(2,2, Option.get(),style4e)
 sheet0.write(2,4, Version.get(),style4e)
 sheet0.write(6,0, espg.get(),style4e)

 sheet0.write(30,0, "      ",style6b)
 sheet0.write(30,1, "      ",style6)
 sheet0.write(30,2, "      ",style6)
 sheet0.write(30,3, "       ",style6)
 sheet0.write(30,4, "      ",style6)
 sheet0.write(30,5, "      ",style6)
 sheet0.write(30,6, "      ",style6a)

# Nodes ------------------------------------------------------------------------
 numnodesline=[]
 kmline=[]
 dx = float(nodex.get())/1000.
 nodevel = float(velnode.get())*1.852
 for i in range(len(LNL)):
   element = LNL[i]-FNL[i]+1
   numnodesline.append(float(element))
   kmline.append((element-1)*dx)

 if v.get() == 1:
  geometry ='Alternated'
  apothema = nodex.get()
 if v.get() == 0:
  geometry ='Hexagonal'
  apothema = round((nodex.get()/2)*math.sqrt(3),2)
 if v.get() == 2:
  geometry ='Rectangular'
  apothema = nodex.get()

# Sheet 0 -------------------------------------------------------------------------------------------- 

# Nodes

 sheet0.write(10,0, "Node Line Interval (m):",style4f)                      # A11
 sheet0.write(10,1, "",style4f)                                             # B11
 sheet0.write(10,2, float(nodex.get()),style4b)                             # C11

 sheet0.write(11,0, "Node Interval (m):",style4f)                           # A12
 sheet0.write(11,1, "",style4f)                                             # B12
 sheet0.write(11,2, float(nodey.get()),style4b)                             # C12

 sheet0.write(12,0, "Number of nodes:",style4f )                            # A13
 sheet0.write(12,1, "",style4f )                                            # B13
 sheet0.write(12,2, sum(numnodesline),style4b)                              # C13

 sheet0.write(13,0, "Number of lines:",style4f)                             # A14
 sheet0.write(13,1, "",style4f)                                             # B14
 sheet0.write(13,2, len(LineNumber),style4b)                                # C14

 sheet0.write(14,0, "Total line length (Km):",style4e)                      # A15
 sheet0.write(14,1, "",style4e)                                            # B15
 sheet0.write(14,2, sum(kmline),style4b)                                    # C15

 sheet0.write(15,0, "Average line length (Km):",style4e)                    # A16
 sheet0.write(15,1, "",style4e)                                             # B16
 sheet0.write(15,2, round(sum(kmline)/len(kmline),2),style4b)               # C16

 sheet0.write(16,0, "Nodes density /sqKm:",style4e)                         # A17
 sheet0.write(16,1, "",style4e)                                             # B17
 sheet0.write(16,2, round(sum(numnodesline)/NodeArea,2),style4b)            # C17

 sheet0.write(17,0, "Avg nodes /line:",style4e)                             # A18
 sheet0.write(17,1, "",style4e)                                             # B18
 sheet0.write(17,2, round(sum(numnodesline)/len(LineNumber),1) ,style4b)    # C18

 sheet0.write(18,0, "Max nodes in line:",style4e)                           # A19
 sheet0.write(18,1, "",style4e)                                             # B19
 sheet0.write(18,2, max(numnodesline) ,style4b)                             # C19
 
 sheet0.write(19,0, "Min nodes in line:",style4e)                           # A20
 sheet0.write(19,1, "",style4e)                                             # B20
 sheet0.write(19,2,min(numnodesline) ,style4b)                              # C20

 sheet0.write(20,0, "Line dir (degrees):",style4e)                          # A21
 sheet0.write(20,1, "",style4e)                                             # B21
 sheet0.write(20,2, (float(anglex.get()+90.)-ort.get()*90.),style4b)         # C21

 sheet0.write(21,0, "Nodes area sqKm:",style4e)                             # A22
 sheet0.write(21,1, "",style4e)                                             # B22
 sheet0.write(21,2, round(NodeArea,2),style4b)                              # C22

 sheet0.write(22,0, "Geometry",style4e)                                     # A23
 sheet0.write(22,1, "",style4e)                                             # B23
 sheet0.write(22,2, geometry,style4b)                                       # C23

 sheet0.write(23,0, "Aphotema",style4e)                                     # A23
 sheet0.write(23,1, "",style4e)                                             # B23
 sheet0.write(23,2, apothema,style4b)                                       # C23

 sheet0.write(24,0, "Record length (s)",style4e)                            # A24
 sheet0.write(24,1, "",style4e)                                             # B24
 sheet0.write(24,2, 10.,style4b)                                            # C24

 sheet0.write(25,0, "Sample rate (ms)",style4e)                             # A25
 sheet0.write(25,1, "",style4e)                                             # B25
 sheet0.write(25,2, 2.,style4b)                                             # C25

 sheet0.write(26,0, "Component numbers",style4e)                            # A26
 sheet0.write(26,1, "",style4e)                                             # B26
 sheet0.write(26,2, 4.,style4b)                                             # C26

 tracespernode= (16000/50)*(16000/50)
 sheet0.write(27,0, "Trace/OBN - 8000m",style4e)                            # A27
 sheet0.write(27,1, "",style4e)                                             # B27
 sheet0.write(27,2, tracespernode,style4b)                                  # C27

 header = 3200+240     # bytes
 samples = 4*5000      # bytes
 trace = tracespernode*4*samples + header 
 sheet0.write(28,0, "Size of CRG - 8000m (GB)",style4e)                     # A27
 sheet0.write(28,1, "",style4e)                                             # B27
 sheet0.write(28,2, round(trace/(1024*1024*1024),2),style4b)                                            # C26


 sheet0.write(29,0, "Size survey (TB)",style4e)                             # A27
 sheet0.write(29,1, "",style4e)                                             # B27
 sheet0.write(29,2, round((sum(numnodesline)*trace)/(1024*1024*1024*1024),2),style4b)                                            # C26



#Shots
 nsources = nfontes.get()
 dxa=2*shotx.get()
 dya=shoty.get()

 sheet0.write(10,4, "Number of sources:",style4f)                           # E11
 sheet0.write(10,5, "",style4f)                                             # F11
 sheet0.write(10,6, nsources,style4b)                                       # G11

 sheet0.write(11,4, "Sail Line Interval (m):",style4f)                      # E12
 sheet0.write(11,5, "",style4f)                                             # F12
 sheet0.write(11,6, float(nsources*dya),style4b)                            # G12

 sheet0.write(12,4, "Shot Line Interval (m):",style4f)                      # E13
 sheet0.write(12,5, "",style4f)                                             # F13
 sheet0.write(12,6, float(shoty.get()),style4b)                             # G13

 sheet0.write(13,4, "Shot Point Int (m):",style4f)                          # E14
 sheet0.write(13,5, "",style4f)                                             # F14
 sheet0.write(13,6, float(shotx.get())*nfontes.get(),style4b)
# PORRA MOD2
                             # G14

 sheet0.write(14,4, "Bin X (m):",style4f)                                   # E15
 sheet0.write(14,5, "",style4f)                                             # F15
 sheet0.write(14,6, float(nfontes.get()*shotx.get()/2),style4b)                           # G15

 sheet0.write(15,4, "Bin Y (m):",style4f)                                   # E16
 sheet0.write(15,5, "",style4f)                                             # E16
 sheet0.write(15,6, float(shoty.get()/2),style4b)                           # G16

 sheet0.write(16,4, "Number of shots:",style4d)                             # E17
 sheet0.write(16,5, "",style4d)                                             # F17

 sheet0.write(17,4, "Number of shot lines:",style4d)                        # E18
 sheet0.write(17,5, "",style4d)                                             # F18

 sheet0.write(18,4, "Average Km Shot Line:",style4d)                        # E19
 sheet0.write(18,5, "",style4d)                                             # F19
# sheet0.write(20,6, AvShotKm_1,style4b)                                    # G19

 sheet0.write(19,4, "Total Linear Km of Shots:",style4d)                             # E20
 sheet0.write(19,5, "",style4d)                                             # F20
# sheet0.write(19,6, LinearShotKm,style4b)                                  # G20

 sheet0.write(20,4, "Total Shoot. time (hrs)",style4d)                      # E21
 sheet0.write(20,5, "",style4d)                                             # E21
# sheet0.write(20,6, round(TotalShootTimeHours,2),style4b)                  # G21

 sheet0.write(21,4, "Total Shoot. time (days)",style4d)                     # E22
 sheet0.write(21,5, "",style4d)                                             # E22
# sheet0.write(21,6, round(TotalShootTimeDays,2),style4b)                   # G22

 sheet0.write(22,4, "Shot density / sqKm:",style4d)                         # E23
 sheet0.write(22,5, "",style4d)                                             # E23

 sheet0.write(23,4, "Number of Sail Lines:",style4d)                        # E24
 sheet0.write(23,5, "",style4d)                                             # E24
# sheet0.write(23,6, AvSailKm_1,style4b)                                    # G24

 sheet0.write(24,4, "Avg length SailLine (Km):",style4d)                    # E25
 sheet0.write(24,5, "",style4d)                                             # E25
# sheet0.write(23,6, AvSailKm_1,style4b)                                    # G25

 sheet0.write(25,4, "Total Sail Linear Km:",style4d)                        # E26
 sheet0.write(25,5, "",style4d)                                             # F26
# sheet0.write(24,6, LinearSailKm,style4b)                                  # G26

 sheet0.write(26,4, "Min shots / line:",style4d)                            # E27
 sheet0.write(26,5, "",style4d)                                             # F27

 sheet0.write(27,4, "Max shots / line:",style4d)                            # E28
 sheet0.write(27,5, "",style4d)                                             # F28

 sheet0.write(28,4, "Line dir (degrees):",style4d)                          # E29
 sheet0.write(28,5, "",style4d)                                             # F29
 sheet0.write(28,6, float(anglexa.get()+ort1.get()*90.),style4b)            # G29

 sheet0.write(29,4, "Shot area sqKm:",style4d)                              # E30
 sheet0.write(29,5, "",style4d)                                             # F30
 sheet0.write(29,6, round(ShotArea,2),style4b)                              # G30

# Sheet 1 ------- Nodes and Nodes Lines ------------------------------------------

 sheet1.write(0,0, "Line",style6)
 sheet1.write(0,1, "LineNum",style6)
 sheet1.write(0,2, "1st Node ",style6)
 sheet1.write(0,3, "Lst Node ",style6)
 sheet1.write(0,4, "# Nodes",style6)
 sheet1.write(0,5, "Line-Km",style6)
 sheet1.write(0,6, "Line-Hrs",style6)
 sheet1.write(0,7, "Line-Days",style6a)

 nodevel = float(velnode.get())*1.852
 row =1
 for Inode in range(0,len(LineNumber)):
         sheet1.write(row,0,Inode+1,style4b)
         sheet1.write(row,1,LineNumber[Inode],style4b)
         sheet1.write(row,2,FNL[Inode],style4b)
         sheet1.write(row,3,LNL[Inode],style4b)
         sheet1.write(row,4,LNL[Inode]-FNL[Inode]+1,style4b)
         sheet1.write(row,5,(LNL[Inode]-FNL[Inode])*dx,style4b)
         sheet1.write(row,6,round((LNL[Inode]-FNL[Inode])*(dx/nodevel),3),style4b)
         sheet1.write(row,7,round(((LNL[Inode]-FNL[Inode])*(dx/nodevel))/24,3),style4b)
         row+=1


 s=""
 value=str(row)

 seqA=["COUNT(A2:A",value,")"]
 A=s.join(seqA)
 sheet1.write(row, 0, xlwt.Formula(A),style6a)

 seqE=["SUM(E2:E",value,")"]
 E=s.join(seqE)
 sheet1.write(row, 4, xlwt.Formula(E),style6a)

 seqF=["SUM(F2:F",value,")"]
 F=s.join(seqF)
 sheet1.write(row, 5, xlwt.Formula(F),style6a)

 seqG=["SUM(G2:G",value,")"]
 G=s.join(seqG)
 sheet1.write(row, 6, xlwt.Formula(G),style6a)

 seqH=["SUM(H2:H",value,")"]
 H=s.join(seqH)
 sheet1.write(row, 7, xlwt.Formula(H),style6a)

# Sheet 2 --  Nodes Polygon -----------------------------------------------------------------
 inext = 0
 sheet2.write(0,0, "X",style6)
 sheet2.write(0,1, "Y",style6a)
 for i in range(0,len(xp)):
    sheet2.write(i+1,0,float(xp[i]),style4b)
    sheet2.write(i+1,1,float(yp[i]),style4b)
    inext=i+1
 sheet2.write(inext+1,0, "Area sqKm",style6)
 sheet2.write(inext+1,1, round(NodeArea,2),style6a)

# Sheet 3 -- Shot Lines   --------------------------------------
# Rereading the shot.txt
 sxx,syy = [],[]
 sline,spoint = [], []
 with open('shots.txt','r') as fshot:
   next(fshot)
   reader = csv.reader(fshot, delimiter=' ')
   for row in reader:
     sxx.append(float(row[0]))
     syy.append(float(row[1]))
     sline.append(float(row[2]))
     spoint.append(float(row[3]))
 fshot.close()

# Find the line in the vector and sum how times many it happens(this is the numeber of shotpoints  in each line)
 new_shotline = []
 new_numbershots = []
 for isl in sline:
     if isl not in new_shotline:
        new_shotline.append(isl)
        new_numbershots.append(sline.count(isl))
 fsp,lsp = [],[]
 nn=len(spoint)-1
 for iss in range(0,nn):
    if (spoint[iss+1]-spoint[iss])<0: 
        lsp.append(spoint[iss])
 lsp.append(spoint[nn])

# Compute Sheet 0 values

 new_shotlinekm = []
 new_shotlinedays = []
 new_shotlinehours = []
 for iporra in range(0,len(new_numbershots)):
      km = (new_numbershots[iporra]-1)*(nfontes.get()*shotx.get()/1000.)
      new_shotlinekm.append(km)
      thours = km/(velshot.get()*1.852)
      tdays = thours/24
      new_shotlinedays.append(tdays)
      new_shotlinehours.append(thours)
 print ("new_shotlinekm", len(new_shotlinekm)*km)
# Now writing 
 sheet0.write(16,6, sum(new_numbershots),style4b)                              # G17
 sheet0.write(17,6, len(new_shotline),style4b)                                 # G18
 sheet0.write(18,6, round(sum(new_shotlinekm)/len(new_shotline),2),style4b)    # G19
 sheet0.write(19,6, sum(new_shotlinekm),style4b)                               # G20
 sheet0.write(22,6, round(sum(new_numbershots)/ShotArea,2),style4b)            # G23
 sheet0.write(26,6, min(new_numbershots),style4b)                              # G27
 sheet0.write(27,6, max(new_numbershots),style4b)                              # G28

 sheet3.write(0,0, "Line",style7)
 sheet3.write(0,1, "Sail Line",style7)
 sheet3.write(0,2, "Shots / line ",style7)
 sheet3.write(0,3, "Line-Km",style7a)
# sheet3.write(0,4, "Line-hours",style7a)
# sheet3.write(0,5, "Line-days",style7a)

 row = 1
 for Ishot in new_shotline:
     sheet3.write(row,0,row,style4b)
     sheet3.write(row,1,new_shotline[row-1],style4b)
     sheet3.write(row,2,new_numbershots[row-1],style4b)
#  PORRA MOD1
     sheet3.write(row,3,(new_numbershots[row-1]-1)*(nfontes.get()*shotx.get()/1000.),style4b)
     row+=1

 sheet3.write(row,0, "Line",style7)
 sheet3.write(row,1, "LineNum",style7)
 sheet3.write(row,2, "Shots/line ",style7)
 sheet3.write(row,3, "Line-Km",style7)

# sheet3.write(row+1,0, "",style7)
 sheet3.write(row+1,1, "",style7)

 s=""
 value=str(row)

 seqA=["COUNT(A2:A",value,")"]
 A=s.join(seqA)
 sheet3.write(row+1, 0, xlwt.Formula(A),style7)
 
 seqC=["SUM(C2:C",value,")"]
 C=s.join(seqC)
 sheet3.write(row+1, 2, xlwt.Formula(C),style7)

 seqD=["SUM(D2:D",value,")"]
 D=s.join(seqD)
 sheet3.write(row+1, 3, xlwt.Formula(D),style7)

# Sheet 4 ------ Shot Polygon ----------------------------------------------------------

 sheet4.write(0,0, "X",style7)
 sheet4.write(0,1, "Y",style7a)
 inext=0
 for i in range(0,len(xp3)):
    sheet4.write(i+1,0,float(xp3[i]),style4b)
    sheet4.write(i+1,1,float(yp3[i]),style4b)
    inext+=1
 sheet4.write(inext+1,0, "Area sqKm",style7)
 sheet4.write(inext+1,1, round(ShotArea,2),style7a)

#  ---  Sheet 5 Fold   ---------------------------------------------------------------

 sheet5.write(0,0, "Offset",style6)
 sheet5.write(0,1, "Fold",style6a)
 FoldOffset=[]
 FoldCount=[]
 OffInt=MaxOff.get()/20.
 for i in  range(0,21):
   FoldOffset.append (float(i*OffInt))
   FoldCount.append ((FoldOffset[i]/(nodex.get()*2))*(FoldOffset[i]/(nodey.get()*2))*math.pi) 
 for i in range(1,len(FoldOffset)):
    sheet5.write(i,0,float(FoldOffset[i]),style4b)
    sheet5.write(i,1,float(FoldCount[i]),style4b)
 sheet5.write(21,0, " ",style6)
 sheet5.write(21,1, " ",style6a)

#  ----  Sheet 7 Sail Lines  --------------------------------------------------------------------------------
# Rereading the sail.txt
 sailline,sailpoint = [], []
 with open('sail.txt','r') as fsail:
   next(fsail)
   reader = csv.reader(fsail, delimiter=' ')
   for row in reader:
     sailline.append(float(row[2]))
     sailpoint.append(float(row[3]))
 fsail.close()
# Find the line in hte vector and summ how many it happens(this is the numeber >
 new_sailline = []
 new_sailpoint = []
 for ksl in sailline:
     if ksl not in new_sailline:
        new_sailline.append(ksl)
        new_sailpoint.append(sailline.count(ksl))
 fsailp,lsailp = [],[]
 n=len(sailpoint)-1
 for kss in range(0,n):
    if (sailpoint[kss+1]-sailpoint[kss])<0: 
        lsailp.append(sailpoint[kss])
 lsailp.append(sailpoint[n])

# Compute Sheet 0 values
 new_saillinekm = []
 new_saillinedays = []
 new_saillinehours = [] 
 for ip in range(0,len(new_sailpoint)):
      kmsail = nfontes.get()*(new_sailpoint[ip]-1)*(shotx.get()/1000.)
      new_saillinekm.append(kmsail)
      tsailhours = chglinetime.get()+kmsail/(velshot.get()*1.852)
      tsaildays = tsailhours/24
      new_saillinehours.append(tsailhours)
      new_saillinedays.append(tsaildays)

# Now writing 
 sheet0.write(23,6, len(new_sailline),style4b)                                 # G24
### MODIDIEF FOR 3 SOURCES
 sheet0.write(25,6, sum(new_saillinekm),style4b)                               # G25
 sheet0.write(20,6, round(sum(new_saillinehours),2),style4b)                   # G21
 sheet0.write(21,6, round(sum(new_saillinedays),2),style4b)                    # G22

 #### MODIFIED FOR 3  source
 sheet0.write(24,6, round(sum(new_saillinekm)/len(new_sailline),2),style4b)    # G26
 print ( "sum(new_saillinekm)/len(new_sailline)",sum(new_saillinekm*nfontes.get())*len(new_sailline))

 sheet7.write(0,0, "Line",style9)
 sheet7.write(0,1, "Sail Line",style9)
 sheet7.write(0,2, "Line-Km",style9)
 sheet7.write(0,3, "Line-hours",style9a)
 sheet7.write(0,4, "Line-days",style9a)

# FF = 1.
 FF = shotx.get()*nfontes.get()/1000.
 FF = FF/(velshot.get()*1.852)
 
 srow = 1
 for Isail in new_sailline:
     sheet7.write(srow,0,srow,style4b)
     sheet7.write(srow,1,new_sailline[srow-1],style4b)
     sheet7.write(srow,2,nfontes.get()*(new_sailpoint[srow-1]-1)*(shotx.get()/1000.),style4b)
     sheet7.write(srow,3,round((new_sailpoint[srow-1]-1)*FF+chglinetime.get(),2),style4b)
     sheet7.write(srow,4,round((new_sailpoint[srow-1]-1)*FF/24,2),style4b)
     srow+=1


 sheet7.write(srow,0, "Line",style9)
 sheet7.write(srow,1, "LineNum",style9)
 sheet7.write(srow,2, "Line-Km",style9)
 sheet7.write(srow,3, "Line-hours",style9)
 sheet7.write(srow,4, "Line-days",style9a)

 sheet7.write(srow+4,0, "",style9)
 sheet7.write(srow+5,0, "",style9)
 sheet7.write(srow+4,1, "Knot-Km/h",style9)
 sheet7.write(srow+4,2, 1.852,style9)
 sheet7.write(srow+5,1, "Vel-Km/h",style9)
 sheet7.write(srow+5,2, velshot.get()*1.852,style9)
 sheet7.write(srow+4,3, "Line chg hrs",style9)
 sheet7.write(srow+4,4, chglinetime.get(),style9)
 sheet7.write(srow+5,3, "",style9)
 sheet7.write(srow+5,4, "",style9)


 s=""
 value=str(srow)
 seqA=["COUNT(A2:A",value,")"]
 A=s.join(seqA)
 sheet7.write(srow+1, 0, xlwt.Formula(A),style9)

 seqC=["SUM(C2:C",value,")"]
 C=s.join(seqC)
 sheet7.write(srow+1, 2, xlwt.Formula(C),style9)

 seqD=["SUM(D2:D",value,")"]
 D=s.join(seqD)
 sheet7.write(srow+1, 3, xlwt.Formula(D),style9)

 seqE=["SUM(E2:E",value,")"]
 E=s.join(seqE)
 sheet7.write(srow+1, 4, xlwt.Formula(E),style9a)


#---------------------------------------------------------------

 book.save("Spreadsheet.xls")

#-----------------Class  bar (Progress bar)--------------------
class PB:

    def settitle(self, title):
        self.__root.title(title)
    # Create Progress Bar
    def __init__(self, width, height):
#        self.__root = tk.Toplevel()
        self.__root = tkinter.Tk() #updated by Petr
        self.__root.resizable(False, False)
        self.__root.title('Wait please...')
        self.__canvas = tkinter.Canvas(self.__root, width=width, height=height)
        self.__canvas.grid()
        self.__width = width
        self.__height = height

    # Open Progress Bar
    def open(self):
        self.__root.deiconify()
        self.__root.focus_set()
        #self.__root.update()

    # Close Progress Bar
    def close(self):
        self.__root.withdraw()

    # Update Progress Bar
    def update(self, ratio):
        self.__canvas.delete(tkinter.ALL)
        self.__canvas.create_rectangle(0, 0, self.__width * ratio, \
                                       self.__height, fill='blue')
        self.__root.update()
        self.__root.focus_set()

#------------------- Call Fold ------------------------------
def foldm():
 os.system('./fold')
#------------------- Call Planilha----------------------------
def planilha():
 os.system('libreoffice Spreadsheet.xls&')
#------------------- Call Map PYQGIS----------------------------
def map():
 os.system('./map&')
#---------------------Call Pdiagram --------------------------
def pdiagram():
 diagram(nfontes.get(),shotx.get(),shoty.get(),velshot.get(),wd.get())

#------------------Plot-----------------------------------
def plot():


 if flaggridnode >0:
     fig, ax = plt.subplots(figsize=(8, 8))
     ax.set_title('OBN survey area')

     if var2a.get() == 1:
       ax.plot(xp3, yp3, color='blue', alpha=0.9,
        linewidth=2, solid_capstyle='round', zorder=1)


     if var1a.get() == 1:
       ax.plot(xp, yp, color='red', alpha=0.9,
         linewidth=2, solid_capstyle='round', zorder=1)

     if var1b.get() == 1:
       ax.scatter(XX,YY,s=3.5,color='red',alpha=.9)

     if var2b.get() == 1:
       ax.scatter(XXgrid,YYgrid,s=.3,color='black',alpha=.2)

## if var3b.get() == 1:
## ax.scatter(XXsail,YYsail,s=.3,color='green',alpha=.4)

     if var1c.get() == 1:
       ax.scatter(x0,y0,s=24.5,color='red',marker='s',alpha=.9)

     if var2c.get() == 1:
       ax.scatter(x0a,y0a,s=24.5,color='blue',marker='s',alpha=.9)

 else:
    print ("PLEASSE RUN THE NODES COMUTAION")
    messagebox.showwarning("Please run:", "NODES COMPUTATION") 
 
# if var3c.get() == 1:
#   ax.scatter(x0a,y0a,s=24.5,color='black',marker='s',alpha=.9)

 plt.show()


#-----------------------------------------------------------------------

Button(root,text="Nodes Computation",font=("Sans Bold", 9), command=rnodes).grid(row=9, column=5,sticky="w")

Button(root,text="Full Computation",font=("Sans Bold", 9), command=rshots).grid(row=20, column=5,sticky="w")

Button(root,text="PLOT DIAGRAM ",font=("Sans Bold", 7), command=pdiagram).grid(row=13, column=0, sticky="w")

Button(root,text="PLOT GRID      ",font=("Sans Bold", 7), command=plot).grid(row=11, column=0,sticky="w")

Button(root,text="EXIT",font=("Sans Bold", 10), command=exit).grid(row=28, column=5,sticky=E )

Button(root,text="MAP PYQGIS ",font=("Sans Bold", 7), command=map).grid(row=19, column=0, sticky="w")

Button(root,text="SpreadSheet",font=("Sans Bold", 7), command=planilha).grid(row=21, column=0,sticky="w")

Button(root,text="FOLD           ",font=("Sans Bold", 7), command=foldm).grid(row=23, column=0,sticky="w")

root.mainloop()

