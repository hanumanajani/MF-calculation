class InputReader:
    def __init__(self,filename):

        self.filename = filename
        self.crd_list1 = self.generate_crd_list1()
        self.crd_list2 = self.generate_crd_list2()
        self.vx1,self.vy1,self.vz1 = self.generate_crd_v1()
        self.vx2,self.vy2,self.vz2 = self.generate_crd_v2()
        self.time_int = self.timeinterval()
        self.C_terminal = self.find_C_terminal()
        self.N_terminal = self.find_N_terminal()
        


    def generate_crd_list1(self):
        inp_file1 = ""
        
        with open(self.filename,'r') as file1:
            content1 = file1.read()
            line_list1 = content1.split("\n")
            
            for i in range(len(line_list1)):
                line_list1[i] = line_list1[i].split()
                if(line_list1[i][0]=="inp_file1"):
                    inp_file1 = line_list1[i][2]
                    break
        if(inp_file1==""):
            print("write coorect name of input file1")
            print("ERRRRROOOOORRRR")
        else:
            with open(inp_file1+".pdb",'r') as inpf1:
                crd_content1 = inpf1.read()
                crd_list1 = crd_content1.split("\n")
                for i in range(len(crd_list1)):
                    crd_list1[i] = crd_list1[i].split()
        return crd_list1
    


    def generate_crd_list2(self):
        inp_file2 = ""
        
        with open(self.filename,'r') as file1:
            content1 = file1.read()
            line_list1 = content1.split("\n")
            
            for i in range(len(line_list1)):
                line_list1[i] = line_list1[i].split()
                if(line_list1[i][0]=="inp_file2"):
                    inp_file2 = line_list1[i][2]
                    break
        if(inp_file2==""):
            print("write coorect name of input file2")
            print("ERRRRROOOOORRRR")
        else:
            with open(inp_file2+".pdb",'r') as inpf2:
                crd_content2 = inpf2.read()
                crd_list2 = crd_content2.split("\n")
                for i in range(len(crd_list2)):
                    crd_list2[i] = crd_list2[i].split()
        return crd_list2
    


    def generate_crd_v1(self):
        v1x,v1y,v1z = 0.0, 0.0, 0.0
        with open(self.filename,'r') as file1:
            content1 = file1.read()
            line_list1 = content1.split("\n")
            for i in range(len(line_list1)):
                line_list1[i] = line_list1[i].split()
            if line_list1[10][2]=="points":
                return line_list1[13][2],line_list1[14][2],line_list1[15][2]
            else:
                point_list = self.crd_list1
                atm1_id = line_list1[21][2]
                # print("atom id",atm1_id)
            
                for j in range(len(point_list)):
                   if(len(point_list[j])<8):
                    #    print("len of list",len(point_list[j]))
                    #    print(point_list[j])
                       continue
                #    print(point_list[j][1],'\n')
                #    if(j==5):
                #        break
                   if((point_list[j][1])==atm1_id):
                       v1x,v1y,v1z = point_list[j][5],point_list[j][6],point_list[j][7]
                    #    print(v1x,"---------------")
                       break
        return v1x,v1y,v1z
    


    def generate_crd_v2(self):
        v2x,v2y,v2z = 0.0, 0.0, 0.0
        with open(self.filename,'r') as file1:
            content1 = file1.read()
            line_list1 = content1.split("\n")
            for i in range(len(line_list1)):
                line_list1[i] = line_list1[i].split()
            if line_list1[10][2]=="points":
                return line_list1[16][2],line_list1[17][2],line_list1[18][2]
            else:
                point_list = self.crd_list2
                atm2_id = line_list1[22][2]
            
                for j in range(len(point_list)):
                  if(len(point_list[j])<8):
                       continue
                  if(point_list[j][1]==atm2_id):
                     v2x,v2y,v2z = point_list[j][5],point_list[j][6],point_list[j][7]
                     break
        return v2x,v2y,v2z
    



    def timeinterval(self):
        time = 0
        with open(self.filename,'r') as file1:
            content1 = file1.read()
            line_list1 = content1.split("\n")
            for i in range(len(line_list1)):
                line_list1[i] = line_list1[i].split(" ")
                time = line_list1[4][2]
        if(time==0):
            print("time interval is zero not possible")
            print("EEERRRROOOOOORRRR")
        return time
    


    
    def find_N_terminal(self):
         with open(self.filename,'r') as file1:
            content1 = file1.read()
            line_list1 = content1.split("\n")
            for i in range(len(line_list1)):
                line_list1[i] = line_list1[i].split()

            if(line_list1[25][2]==""):
                print("Errorrrrrrrrrr------------")
                print("write correct N terminal in input parameter file")

            return int(line_list1[25][2])
         



    def find_C_terminal(self):
         with open(self.filename,'r') as file1:
            content1 = file1.read()
            line_list1 = content1.split("\n")
            for i in range(len(line_list1)):
                line_list1[i] = line_list1[i].split()

            if(line_list1[26][2]==""):
                print("Errorrrrrrrrrr")
                print("write correct C terminal in input parameter file")

            return int(line_list1[26][2])



                
                    




        
        
