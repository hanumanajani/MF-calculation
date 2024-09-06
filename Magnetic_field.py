import sys
import _input as input
import json as _json
import math






def Magnetic_field(filename):
#     print(filename)
  k = 5880
  while k<=5900:
     data =[]
     if(k%50==0):
          print(k)
     with open(filename,'r') as file1:
         data1 = file1.read()
         data = data1.split("\n")
     with open(filename,'w') as file2:
            for i in range(len(data)):
                 if(i==30):
                      break
                 if(i==21):
                      file2.write("atm1_id = "+str(k)+"\n")
                     
                 else:
                     file2.write(data[i]+"\n")
               
            
     input_data = input.InputReader(filename)
     Magnetic_field_calculate(k,input_data)
     k = k+1
     
  with open("magnetic_field.out",'a') as ofile:
         ofile.write("-----------------------------------------------------------------------------------------"+"\n")





def Magnetic_field_calculate(k,input_data):
#     print("magnetic field calculation function")
#     print(input_data.vx1,'\n')
#     print(input_data.vx2,'\n')
#     print(input_data.time_int,'\n')
    list = input_data.crd_list2
    Mx,My,Mz = calculate_magnetic_field_crd_atpt(input_data.vx1,input_data.vy1,input_data.vz1,input_data.crd_list1,input_data.crd_list2,input_data.time_int,input_data.N_terminal,input_data.C_terminal)
    # for i in range(10):
    #     for j in range(len(list[i])):
    #         print(list[i][j])
        # print('\n')
    M = math.sqrt(Mx*Mx + My*My + Mz*Mz)
#     print("Magnetic field x,y,z component:")
#     print("Mx ->  ",Mx)
#     print("My ->  ",My)
#     print("Mz ->  ",Mz)
#     print("M-------------  ",M*1000000)
    x = M*1000000
    # if x>20:
    # print("M-------------> ",k,"  ---------   ",x)
    # print(k,x)
    with open("magnetic_field.out",'a') as ofile:
         if x>0:
              ofile.write(str(k)+"  "+str(x)+"\n")


def calculate_magnetic_field_crd_atpt(vx1,vy1,vz1,crd_list1,crd_list2,time,nter,cter):
    Mx,My,Mz = 0.0,0.0,0.0
#     print("calculation of magnetic fields component xyz on point point p")
    with open("amber_library.json", "r", encoding="utf-8") as json_file:
            amber_library = _json.load(json_file)
    # print(amber_library["CALA N"])
    # print(time)
    # print(vx1,vy1,vz1)
#     print(crd_list1[0])
#     print(cter,nter)
    for i in range(len(crd_list1)):
         dmx,dmy,dmz = 0.0,0.0,0.0
         charge = 0
         if(len(crd_list1[i])<7):
              break
         if(int(crd_list1[i][4])==nter):
              
              charge = amber_library["N" + crd_list1[i][3]+" "+crd_list1[i][2]]
         elif(int(crd_list1[i][4])==cter):
              
              charge = amber_library["C"+crd_list1[i][3]+" "+crd_list1[i][2]]
         else:
              
              charge = amber_library[crd_list1[i][3]+" "+crd_list1[i][2]]
     #     print(charge,"---->charge",i)
         x1 = crd_list1[i][5]
         y1 = crd_list1[i][6]
         z1 = crd_list1[i][7]
         x2 = crd_list2[i][5]
         y2 = crd_list2[i][6]
         z2 = crd_list2[i][7]
         dmx,dmy,dmz = calculate_magnetic_field_duetosingleatm(vx1,vy1,vz1,time,charge,x1,y1,z1,x2,y2,z2)
         Mx = Mx + dmx
         My = My + dmy
         Mz = Mz + dmz

         
    return Mx,My,Mz




def calculate_magnetic_field_duetosingleatm(px,py,pz,time,charge,x1,y1,z1,x2,y2,z2):
     px = float(px)
     py = float(py)
     pz = float(pz)
     time = float(time)
     charge=float(charge)
     x1 = float(x1)
     y1 = float(y1)
     z1 = float(z1)
     x2 = float(x2)
     y2 = float(y2)
     z2 = float(z2)
     # dimension of vx,vy,vz is Angustom/nanosecond
     # vx,vy,vz is the velocity of middle point c which position is mx,my,mz(Angustom)
     vx = (x2-x1)/time
     vy = (y2-y1)/time
     vz = (z2-z1)/time

     mx = (x1+x2)/2
     my = (y1+y2)/2
     mz = (z1+z2)/2

     # calculation of rx,ry,rz(component of r vector) dimension is Angustom
     rx = (px-mx)
     ry = (py-my)
     rz = (pz-mz)
    
     # calculation of magnitude of r (rm)
     rm = math.sqrt((rx*rx) + (ry*ry) + (rz*rz))

     # component of cross product o vector v and r component of (VXR) is vrx,vry,vrz
     vrx = (vy*rz - vz*ry)
     vry = (vz*rx - vx*rz)
     vrz = (vx*ry - vy*rx)
     # conversion of charge in columb
     charge = (charge*1.602176634)/(10**(19))
     Bx = ((10**12)*charge*vrx)/(rm**3)
     By = ((10**12)*charge*vry)/(rm**3)
     Bz = ((10**12)*charge*vrz)/(rm**3)

     return Bx,By,Bz
    
   







if __name__ == '__main__':
    #get input parameter
    if len(sys.argv[1:])==1:
        filename = sys.argv[1]
        Magnetic_field(filename)