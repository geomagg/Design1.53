def planout (ProjName,Co,Option,Version,espg,
             nodex,nodey,velnode,v,anglex,
             ort,nfontes,shotx,shoty,
             anglexa,ort1,velshot,MaxOff,chglinetime,
             LNL,FNL,LineNumber,NodeArea,ShotArea,
             xp,yp,xp3,yp3):





# img = Image.open("geomagg3.bmp")
# r, g, b, a = img.split()
# img =Image.merge("RGB", (r,g,b))
# img.save('geomagg3.bmp')
 import numpy as np
 import xlwt
 import datetime
 import math
 import csv

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

 sheet0.write(2,0, ProjName,style4e)
 sheet0.write(4,0, Co,style4e)
 sheet0.write(2,2, Option,style4e)
 sheet0.write(2,4, Version,style4e)
 sheet0.write(6,0, espg,style4e)

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
 dx = float(nodex)/1000.
 nodevel = float(velnode)*1.852
 for i in range(len(LNL)):
   element = LNL[i]-FNL[i]+1
   numnodesline.append(float(element))
   kmline.append((element-1)*dx)

 if v == 1:
  geometry ='Alternated'
  apothema = nodex
 if v == 0:
  geometry ='Hexagonal'
  apothema = round((nodex/2)*math.sqrt(3),2)
 if v == 2:
  geometry ='Rectangular'
  apothema = nodex

# Sheet 0 -------------------------------------------------------------------------------------------- 

# Nodes

 sheet0.write(10,0, "Node Line Interval (m):",style4f)                      # A11
 sheet0.write(10,1, "",style4f)                                             # B11
 sheet0.write(10,2, float(nodex),style4b)                             # C11

 sheet0.write(11,0, "Node Interval (m):",style4f)                           # A12
 sheet0.write(11,1, "",style4f)                                             # B12
 sheet0.write(11,2, float(nodey),style4b)                             # C12

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
 sheet0.write(20,2, (float(anglex+90.)-ort*90.),style4b)         # C21

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
 nsources = nfontes
 dxa=2*shotx
 dya=shoty

 sheet0.write(10,4, "Number of sources:",style4f)                           # E11
 sheet0.write(10,5, "",style4f)                                             # F11
 sheet0.write(10,6, nsources,style4b)                                       # G11

 sheet0.write(11,4, "Sail Line Interval (m):",style4f)                      # E12
 sheet0.write(11,5, "",style4f)                                             # F12
 sheet0.write(11,6, float(nsources*dya),style4b)                            # G12

 sheet0.write(12,4, "Shot Line Interval (m):",style4f)                      # E13
 sheet0.write(12,5, "",style4f)                                             # F13
 sheet0.write(12,6, float(shoty),style4b)                             # G13

 sheet0.write(13,4, "Shot Point Int (m):",style4f)                          # E14
 sheet0.write(13,5, "",style4f)                                             # F14
 sheet0.write(13,6, float(shotx)*nfontes,style4b)
# PORRA MOD2
                             # G14

 sheet0.write(14,4, "Bin X (m):",style4f)                                   # E15
 sheet0.write(14,5, "",style4f)                                             # F15
 sheet0.write(14,6, float(nfontes*shotx/2),style4b)                           # G15

 sheet0.write(15,4, "Bin Y (m):",style4f)                                   # E16
 sheet0.write(15,5, "",style4f)                                             # E16
 sheet0.write(15,6, float(shoty/2),style4b)                           # G16

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
 sheet0.write(28,6, float(anglexa+ort1*90.),style4b)            # G29

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

 nodevel = float(velnode)*1.852
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
      km = (new_numbershots[iporra]-1)*(nfontes*shotx/1000.)
      new_shotlinekm.append(km)
      thours = km/(velshot*1.852)
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
     sheet3.write(row,3,(new_numbershots[row-1]-1)*(nfontes*shotx/1000.),style4b)
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
 OffInt=MaxOff/20.
 for i in  range(0,21):
   FoldOffset.append (float(i*OffInt))
   FoldCount.append ((FoldOffset[i]/(nodex*2))*(FoldOffset[i]/(nodey*2))*math.pi) 
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
      kmsail = nfontes*(new_sailpoint[ip]-1)*(shotx/1000.)
      new_saillinekm.append(kmsail)
      tsailhours = chglinetime+kmsail/(velshot*1.852)
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
 print ( "sum(new_saillinekm)/len(new_sailline)",sum(new_saillinekm*nfontes)*len(new_sailline))

 sheet7.write(0,0, "Line",style9)
 sheet7.write(0,1, "Sail Line",style9)
 sheet7.write(0,2, "Line-Km",style9)
 sheet7.write(0,3, "Line-hours",style9a)
 sheet7.write(0,4, "Line-days",style9a)

# FF = 1.
 FF = shotx*nfontes/1000.
 FF = FF/(velshot*1.852)
 
 srow = 1
 for Isail in new_sailline:
     sheet7.write(srow,0,srow,style4b)
     sheet7.write(srow,1,new_sailline[srow-1],style4b)
     sheet7.write(srow,2,nfontes*(new_sailpoint[srow-1]-1)*(shotx/1000.),style4b)
     sheet7.write(srow,3,round((new_sailpoint[srow-1]-1)*FF+chglinetime,2),style4b)
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
 sheet7.write(srow+5,2, velshot*1.852,style9)
 sheet7.write(srow+4,3, "Line chg hrs",style9)
 sheet7.write(srow+4,4, chglinetime,style9)
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

