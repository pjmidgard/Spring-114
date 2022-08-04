from time import time
cvf=0
import os
import binascii
self="'"

namez = input("for compress c or extract e? ")
#@Author Jurijus pacalovas
class compression:

    def cryptograpy_compression(self):
                
                self.name = "Author: Jurijus pacalovas"
                
                if namez=="c":
                    
                   
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    Deep=100
                    long_block=100
                        
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
           

                    nameas=name+".bin"
                
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    sw1=0
                    sw2=0
                    sw3=0
                    sw5=0
                    sw4=0
                    sw6=0
                    sw7=0
                    n1=0
                    n=0
                    n2=0
                    n3=0
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                 
                       

                  
                        s=str(data)
                        
                     
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)  
                                
                                size_data3=size_data2
                                long_file=len(size_data3)
                                size_data10=""
                                size_data9=""
                                size_data5=""
                                fda5=""
                                size_data4=""
                                size_data6=""
                                size_data7=""
                                size_data12=""
                                size_data19=""
                                size_data10=size_data3
                                predict=-1
                                predict2=-1
                                long_block=16
                                Find=1
                                Left_Right=0
                                predict3=1
                                
                                times_of_times=0
                                Where4=0
                                str_find=""
                          
                                

                                cvf1=1
  
                                if cvf1==1:
                                    times_compression=0  
                                    compress_no=0
                                    compress_yes=0
                                    long2=len(size_data3)
                                    Deep=long2//28
                                    times2=Deep
                                    long_block=15
                                    Where5=0
                                    before_block=0
                                    check_size_block=0
                                    before_block_After_check=0
                                    
                                
                                    
                                    
                                    block_compression2=0
                                    
                                    start=-1
                                    Left_Right=0
                                    Find_guess=0
                                    while Find_guess!=1:
                                        
                                        while  len(size_data3)>=896:


                                                    
                                                        

                                                    start=0
                                                    blocks=long_block
                                                    size_compress=63
                                                    end=blocks
                                                    
                                                    if predict3==1 or predict3==4:
                                                       predict=predict+1
                                                    elif predict3==2 or predict3==3:
                                                       predict=predict+2
                                                    if predict>=16:
                                                        predict=0
                                                        
                                                        predict3=predict3+1
                                                        if predict3==5:
                                                        	predict3=1
                                                        
                                                
                                                       
                                                    
                                                    predict=predict+1
                                                    if predict==16:
                                                        predict=0
                                                    
                                                    
                                                                                             
                                                                                                                                        
                
                                                    block=0
                                                    b=format(predict,'04b')
                                                    
                                                    if b[0:1]=="0":
                                                        b2="11"
                                                       
                                                    elif b[0:1]=="1":
                                                        b2="00"
                                                        
                                                    b="01"+b[2:4]
                                                        
                                                        
                                                    
                                                    
                                                    Find=1

                                                    Left_Right=Left_Right+1

                                                    if Left_Right==2:
                                                        Left_Right=1
                                                    
                                                    long=len(size_data3)
                                                    #print(long)
                                                    
                                                    while block<long:
                                                                                str_find=size_data3[block:block+blocks]
                                                                                size_of_block=len(str_find)

                                                                                if size_of_block!=blocks:
                                                                                    size_data4=str_find

                                                                                elif len(str_find)==blocks:

                                                                                    if Left_Right==1:
                         
                                                                                        if str_find[0:4]==b and str_find[4:6]==b2:

                                                                                            
                                                                                            size_data4=b+b[0:2]+str_find[6:]


                                                                                            if size_data4[0:4]==b and size_data4[4:6]==b2:
                                                                                                        print("Error1")
                                                                                                        raise SystemExit
                                                                                            

                                                                                            if size_data4[0:2]==b2:
                                                                                                    print("Error2")
                                                                                                    raise SystemExit

                                                                                            if size_data4[4:6]==b2:
                                                                                                print("Error3")
                                                                                                raise SystemExit

                                                                                            

                                                                              
                                                                                        elif str_find[0:4]==b:
                                                                                            size_data4=str_find[4:8]+b2+str_find[8:]
                                                                                            
                                                                                            
                                                                                        	
                                                                                            before_block=len(str_find)
                                                                                            check_size_block=len(size_data4)
                                                                                            before_block_After_check=before_block-2
                                                                                            if before_block_After_check!=check_size_block:
                                                                                                print("Error4")
                                                                                                raise SystemExit

                                                                                            if size_data4[4:6]!=b2:
                                                                                                print("Error5")
                                                                                                raise SystemExit

                                                                                            if size_data4[4:8]==b:
                                                                                                check=6
                                                                                                
                                                                                            if size_data4[0:2]==b2:
                                                                                                print("Error6")
                                                                                                raise SystemExit

                                                                                        elif str_find[4:6]==b2:

                                                                                            size_data4=b2+str_find[0:4]+str_find[6:]

                                                                                            before_block=len(str_find)
                                                                                            check_size_block=len(size_data4)
                                                                                            before_block_After_check=before_block
                                                                                            if before_block_After_check!=check_size_block:
                                                                                                print("Error7")
                                                                                                raise SystemExit

                                                                                            if size_data4[0:2]!=b2:
                                                                                                print("Error8")
                                                                                                raise SystemExit

                                                                                            if size_data4[0:4]==b:
                                                                                                check=8

                                                                                            if size_data4[4:6]!=b2:
                                                                                                check2="bits1"
                                                                                                
                                                                                            if size_data4[4:6]==b2:
                                                                                                check2="bits2"

                                                                                            if str_find[0:4]==b and str_find[4:6]==b[0:2]:
                                                                                                        print("Error461341")
                                                                                                        raise SystemExit


                                                                                                
                                                                                        elif str_find[0:4]!=b and str_find[4:6]!=b2:

                                                                                            size_data4=str_find

                                                                                            if size_data4[0:2]==b2:
                                                                                                if size_data4[0:2]=="00":
                                                                                                    size_data4="11"+size_data4[2:]
                                                                                                    if size_data4[0:2]==b2:
                                                                                                         print("Error9")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[4:6]==b2:
                                                                                                         print("Error10")
                                                                                                         raise SystemExit
                                                                                                        
                                                                                                    if size_data4[0:4]==b and size_data4[4:6]==b2:
                                                                                                        print("Error11")
                                                                                                        raise SystemExit

                                                                                                    if size_data4[0:4]==b and size_data4[4:6]==b[0:2]:
                                                                                                        print("Error12")
                                                                                                        raise SystemExit

                                                                                                elif size_data4[0:2]=="01":
                                                                                                    size_data4="10"+size_data4[2:]
                                                                                                    
                                                                                                    if size_data4[0:2]==b2:
                                                                                                         print("Error13")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[4:6]==b2:
                                                                                                         print("Error14")
                                                                                                         raise SystemExit
                                                                                                        
                                                                                                    if size_data4[0:4]==b and size_data4[4:6]==b2:
                                                                                                        print("Error15")
                                                                                                        raise SystemExit
                                                                                                    
                                                                                                    if size_data4[0:4]==b and size_data4[4:6]==b[0:2]:
                                                                                                        print("Error16")
                                                                                                        raise SystemExit 
                                                                                                   

   
                                                                                                elif size_data4[0:2]=="10":
                                                                                                    size_data4="01"+size_data4[2:]
                                                                                                    if size_data4[0:2]==b2:
                                                                                                         print("Error17")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[4:6]==b2:
                                                                                                         print("Error18")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[0:4]==b and size_data44[4:6]==b2:
                                                                                                        print("Error19")
                                                                                                        raise SystemExit

                                                                                                    if size_data4[0:4]==b and size_data4[4:6]==b[0:2]:
                                                                                                        print("Error20")
                                                                                                        raise SystemExit

                                                                                                elif size_data4[0:2]=="11":
                                                                                                    size_data4="00"+size_data4[2:]
                                                                                                    
                                                                                                    if size_data4[0:2]==b2:
                                                                                                         print("Error21")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[4:6]==b2:
                                                                                                         print("Error22")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[0:4]==b and size_data4[4:6]==b2:
                                                                                                        print("Error23")
                                                                                                        raise SystemExit
                                                                                                    
                                                                                                    if size_data4[0:4]==b and size_data4[4:6]==b[0:2]:
                                                                                                        
                                                                                                        

                                                                                                        if size_data4[0:4]==b:
                                                                                                            print("Error24")
                                                                                                            raise SystemExit
                                                                                                        
                                                                                                        if size_data4[4:6]==b[0:2]:
                                                                                                            print("Error25")
                                                                                                            raise SystemExit

                                                                                                
                                                                                            
                                                                                            
                                                                                    elif Left_Right==2:

                                                                                        if str_find[4:8]==b2 and str_find[0:2]==b:
                                                                                            size_data4=str_find
                                                                                                                              
                                                                                        elif str_find[4:8]==b:

                                                                                            size_data4=b2+str_find[0:4]+str_find[8:]
                                                                                            
                                                                                            before_block=len(str_find)
                                                                                            check_size_block=len(size_data4)
                                                                                            before_block_After_check=before_block-2
                                                                                            if before_block_After_check!=check_size_block:
                                                                                                print("Error3")
                                                                                                raise SystemExit

                                                                                            if size_data4[0:2]!=b2:
                                                                                                print("Error9")
                                                                                                raise SystemExit


                                                                                            if size_data4[2:4]==b2:
                                                                                                print("ErrorC")
                                                                                                raise SystemExit

                                                                                            if size_data4[0:4]==b:
                                                                                                check=10
                                                                                            
                                                                                                                                                                                                          
                                                                                        elif str_find[0:2]==b2:
                                                                                            size_data4=str_find[2:4]+b2+str_find[4:]
                                                                                            
                                                                                            before_block=len(str_find)
                                                                                            check_size_block=len(size_data4)
                                                                                            before_block_After_check=before_block
                                                                                            if before_block_After_check!=check_size_block:
                                                                                                print("Error4")
                                                                                                raise SystemExit

                                                                                            if size_data4[2:4]!=b2:
                                                                                                print("Error11")
                                                                                                raise SystemExit

                                                                                            if size_data4[2:6]==b:
                                                                                                check=12

                                                                                            if size_data4[0:2]==b2:
                                                                                                ckeck3="bits2"

                                                                                            if size_data4[0:2]!=b2:
                                                                                                ckeck3="bits1"
                                                                                                
                                                                                            
                                                                                        elif str_find[4:8]!=b2 and str_find[0:2]!=b:
                                                                                            size_data4=str_find

                                                                                           

                                                                                            if size_data4[2:4]==b2:
                                                                                                if size_data4[2:4]=="00":
                                                                                                    size_data4=size_data4[0:2]+"11"+size_data4[4:]
                                                                                                    if size_data4[2:4]==b2:
                                                                                                         print("Error022")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[0:2]==b2:
                                                                                                         print("Error462")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[4:8]==b2 and size_data4[0:2]==b:
                                                                                                        print("Error4162")
                                                                                                        raise SystemExit

                                                                                                elif size_data4[2:4]=="01":
                                                                                                    size_data4=size_data4[0:2]+"10"+size_data4[4:]
                                                                                                    if size_data4[2:4]==b2:
                                                                                                         print("Error022")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[0:2]==b2:
                                                                                                         print("Error462")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[4:8]==b2 and size_data4[0:2]==b:
                                                                                                        print("Error4162")
                                                                                                        raise SystemExit
                                                                                                         
                                                                                                elif size_data4[2:4]=="10":
                                                                                                    size_data4=size_data4[0:2]+"01"+size_data4[4:]
                                                                                                    if size_data4[2:4]==b2:
                                                                                                         print("Error022")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[0:2]==b2:
                                                                                                         print("Error462")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[4:8]==b2 and size_data4[0:2]==b:
                                                                                                        print("Error4162")
                                                                                                        raise SystemExit

                                                                                                elif size_data4[2:4]=="11":
                                                                                                    size_data4=size_data4[0:2]+"00"+size_data4[4:]
                                                                                                    if size_data4[2:4]==b2:
                                                                                                         print("Error022")
                                                                                                         raise SystemExit

                                                                                                    if size_data4[0:2]==b2:
                                                                                                         print("Error462")
                                                                                                         raise SystemExit

                                                                                                    if str_find4[4:8]==b2 and str_find4[0:2]==b:
                                                                                                        print("Error4162")
                                                                                                        raise SystemExit
                                                                                                        
                                                                                                
                                                                                                
                                                                                        
                                                                                
                                                                                size_data6=size_data6+size_data4        
                                                                                block=block+blocks
                                                                                #print(block)
                                                         
                                                    times_compression=times_compression+1
                                                    
                                                    #print(times_compression)
                                                    
                                                    
                                                    size_data24=bin(size_of_block)[2:]
                                                    lenf=len(size_data24)
                                                    if lenf>4:
                                                        print("File too big")
                                                        raise SystemExit
                                                                                                            
                                                                                                            
                                                                                                        
                                                    add_bits118=""
                                                    count_bits=4-lenf%4
                                                    z=0
                                                    if count_bits!=0:
                                                        if count_bits!=4:
                                                            while z<count_bits:
                                                                add_bits118="0"+add_bits118
                                                                z=z+1
                                                                                                                                    
                                                                                                                                                
                                                    
                                                                                                                                    
                                                                                                                                                
                                                    size_data6=add_bits118+size_data24+size_data6     
                                                        
                
                                                    size_data3=size_data6
                                                    
                                                    Where4=0
                                                    
                                                    
                                                    #print(len(size_data6))
                                                    size_data6=""
                                                    times_of_times=times_of_times+1
                                                    
                                        long_after=len(size_data3)
                                        
                                        size_data9=size_data3

                                        
                                        long_file=len(size_data10)
                                        long_after=len(size_data9)
                                        #print(long_after) 
                                       
                                        if long_file>long_after or long_block<=long_after:
                                           
                                            size_data11=size_data9
                                            Find_guess=1
                                            
                                        
       
                                    size_data24=bin(times_of_times)[2:]
                                    lenf=len(size_data24)
                                    if lenf>40:
                                        print("File too big")
                                        raise SystemExit
                                                                                            
                                                                                            
                                                                                        
                                    add_bits118=""
                                    count_bits=40-lenf%40
                                    z=0
                                    if count_bits!=0:
                                        if count_bits!=40:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                                                                                                    
                                                                                                                                
                                    lenf=len(add_bits118)
                                    size_data26=bin(lenf)[2:]
                                    lenf=len(size_data26)
                                    if lenf>6:
                                        print("File too big")
                                        raise SystemExit
                                                                                            
                                                                                            
                                                                                        
                                    add_bits118=""
                                    count_bits=6-lenf%6
                                    z=0
                                    if count_bits!=0:
                                        if count_bits!=6:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                                                                                                    
                                                                                                                                
                                    size_data11=add_bits118+size_data26+size_data24+size_data11
                                    
                                    size_data11="1"+size_data11
                                    
                                    
                           
                                    lenf=len(size_data11)
                                        
                                    add_bits118=""
                                    count_bits=8-lenf%8
                                    z=0
                                    if count_bits!=0:
                                            if count_bits!=8:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                                    
                                                                    
                                    size_data11=add_bits118+size_data11
                                    
                                    
                                    
                                    
                                    
                                    n = int(size_data11, 2)
                                
                                    qqwslenf=len(size_data11)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                
                                    size_after=len(jl)
                                   
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:

                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

    def cryptograpy_unpack(self):                      
                 if namez=="e":
                    
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    Portal=2
                    namea="file.W"
                    namem=""
                    namema="?"
                    Deep=0
                 
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    nac=len(nameas)
                    
                    Deep=1000
                    
                    
                    nac=len(nameas)
                    sw1=0
                    sw2=0
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    sw3=0
                    sw4=0
                    sw5=0
                    sw6=0
                    sw7=0
                    n=0
                    n1=0
                    n2=0
                    n3=0
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        
                        data = binary_file.read()
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                     	

                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)  
                                x4=1
                                if x4==1:

                                    size_data3=size_data2
                                    if size_data3[0:9]=="000000001":
                                        size_data3=size_data3[9:]
                                    elif size_data3[0:8]=="00000001":
                                        size_data3=size_data3[8:]
                                    elif size_data3[0:7]=="0000001":
                                        size_data3=size_data3[7:]
                                    elif size_data3[0:6]=="000001":
                                        size_data3=size_data3[6:]
                                    elif size_data3[0:5]=="00001":
                                        size_data3=size_data3[5:]
                                    elif size_data3[0:4]=="0001":
                                        size_data3=size_data3[4:]
                                    elif size_data3[0:3]=="001":
                                        size_data3=size_data3[3:]
                                    elif size_data3[0:2]=="01":
                                        size_data3=size_data3[2:]
                                    elif size_data3[0:1]=="1":
                                        size_data3=size_data3[1:]

                                    Times_extract_of_time_zeroes=size_data3[:6]
                                    #print(Times_extract_of_time_zeroes)
                                    
                                    times_of_times=int(Times_extract_of_time_zeroes,2)
                                    size_data3=size_data3[6:]

                                    Forty_bits=40
                                    Times_bits=Forty_bits-times_of_times

                                    Times_extract_of_time_times=size_data3[:Times_bits]
                                    Times_extract_of_time_times_number=int(Times_extract_of_time_times,2)
                                    size_data3=size_data3[Times_bits:]

                                       
                                    Times_count=0
                                    while Times_extract_of_time_times_number!=Times_count:



                                        Long_block2_not_compress_zeroes=size_data3[:6]
                                        Long_block2_not_compress_zeroes_number=int(Long_block2_not_compress_zeroes,2)
                                        #print(Long_block2_not_compress_zeroes_number)
                                        size_data3=size_data3[6:]

                                        Forty_bits=40
                                        Times_bits=Forty_bits-Long_block2_not_compress_zeroes_number

                                        Not_compress_size_of_block=size_data3[:Times_bits]
                                        Not_compress_size_of_block_number=int(Not_compress_size_of_block,2)
                                        size_data3=size_data3[Times_bits:]


                                        Long_block2_compress_zeroes=size_data3[:6]
                                        Long_block2_compress_zeroes_number=int(Long_block2_not_compress_zeroes,2)
                                        size_data3=size_data3[6:]

                                        Forty_bits=40
                                        Times_bits=Forty_bits-Long_block2_compress_zeroes_number

                                        compress_size_of_block=size_data3[:Times_bits]
                                        compress_size_of_block_number=int(compress_size_of_block,2)
                                        size_data3=size_data3[Times_bits:]


                                        Times_zeroes=size_data3[:6]
                                        Times_zeroes_number=int(Times_zeroes,2)
                                        size_data3=size_data3[6:]

                                        Forty_bits=40
                                        Times_bits=Forty_bits-Times_zeroes_number

                                        Times_zeroes_size_of_block=size_data3[:Times_bits]
                                        Times_zeroes_size_of_block_number=int(Times_zeroes_size_of_block,2)
                                        size_data3=size_data3[Times_bits:]
                                    

                                        if size_data3[0:9]=="000000001":
                                            size_data3=size_data3[9:]
                                        elif size_data3[0:8]=="00000001":
                                            size_data3=size_data3[8:]
                                        elif size_data3[0:7]=="0000001":
                                            size_data3=size_data3[7:]
                                        elif size_data3[0:6]=="000001":
                                            size_data3=size_data3[6:]
                                        elif size_data3[0:5]=="00001":
                                            size_data3=size_data3[5:]
                                        elif size_data3[0:4]=="0001":
                                            size_data3=size_data3[4:]
                                        elif size_data3[0:3]=="001":
                                            size_data3=size_data3[3:]
                                        elif size_data3[0:2]=="01":
                                            size_data3=size_data3[2:]
                                        elif size_data3[0:1]=="1":
                                            size_data3=size_data3[1:]

                                        Blocks_long=size_data3[0:40]
                                        size_data3=size_data3[40:]
                                        Blocks_long_number=int(Blocks_long,2)
                                        Read_times_compression_info=""
                                        
                                        Read_times_compression_info=size_data3[0:40]
                                        
                                        Save_predict_find=""
                                        Read_times_compression_number =int(Read_times_compression_info,2)
                                        
                                        size_data3=size_data3[40:]

                                        

                                        predict=-1
                                        count_times_compression=0
                                    

                                        while Read_times_compression_number!=count_times_compression:
                                            predict=predict+1
                                            if predict==16:
                                                predict=0
                                            b=format(predict,'04b')
                                            if b[0:2]=="01":
                                                b="10"+b[2:]
                                            Save_predict_find=b+Save_predict_find
                                            count_times_compression=count_times_compression+1
                                                    

                                        #print(Save_predict_find)

                                        if size_data3[0:9]=="000000001":
                                            size_data3=size_data3[9:]
                                        elif size_data3[0:8]=="00000001":
                                            size_data3=size_data3[8:]
                                        elif size_data3[0:7]=="0000001":
                                            size_data3=size_data3[7:]
                                        elif size_data3[0:6]=="000001":
                                            size_data3=size_data3[6:]
                                        elif size_data3[0:5]=="00001":
                                            size_data3=size_data3[5:]
                                        elif size_data3[0:4]=="0001":
                                            size_data3=size_data3[4:]
                                        elif size_data3[0:3]=="001":
                                            size_data3=size_data3[3:]
                                        elif size_data3[0:2]=="01":
                                            size_data3=size_data3[2:]
                                        elif size_data3[0:1]=="1":
                                            size_data3=size_data3[1:]

    

                                        extract=0
                                        
                                        if size_data3[0:1]=="0":
                                            extract=1
                                        elif size_data3[0:1]=="1":
                                            extract=2

                                        size_data3[1:]
                                        
                                        
                                        size_data12=""
                                        #print(extract)
                                        if extract==1:
                                            size_data12=size_data3

                                        elif extract==2:
                                            times_compression=0
                                            
                                            compress_no=0
                                            compress_yes=0
                                            long2=len(size_data3)
                                            Deep=Read_times_compression_number
                                            times2=Deep
                                            
                                        
                                            
                                            
                                            block_compression2=0
                                          
                                        
                                            start=-1
                                            while  times_compression<=Times_zeroes_size_of_block_number:

                                                        start=0
                                                        blocks=Blocks_long_number
                                                        end=blocks
                                                        
                                                        find_matches1_number1=0
                                                       
                                                        
                                                        
                                                                                                     
                                                                                                                                            
                    
                                                        block=0
                                                        b=Save_predict_find[times_compression*4:(times_compression*4)+4]
                                                        
                                                        Find=1
                                                        block_compression1=0
                                                        block_compression=0
                                                        block_compression2=0
                                                        long=len(size_data3)
                                                        #print(long)
                                                        
                                                        Binary_code1=""
                                                        Circle_count=Binary_code[0:1]
                                                        if Circle_count=="0":
                                                            Binary_code=Binary_code[1:]
                                                            Program=0
                                                            
                                                        Infromation_program=Binary_code
                                                        Long_Info=len(Infromation_program)

                                                        Blocks_count=0

                                                        size_data3=size_data3[1:]
                                                        
                                                        while block<long:
                                                                                    str_find_tree_maches1=size_data3[block:block+compress_size_of_block_number]
                                                                                    sub_info="01"
                                                                                    Blocks_count=Blocks_count+1

                                                                                    find_matches1=str_find_tree_maches1.find(sub_info, start, end)
                                                                                    find_matches1_1=int(find_matches1)

                                                                                    Binary_code2=""
                                                                                    blocks2=0
                                                                                    Have_number=-1
                                                                                    Program=0
                                                                                    
                                                                                    if Long_Info!=0:
                                                                                        Program_code1=Infromation_program[Program:Program+1]
                                                                                        if Program_code1=="1":
                                                                                            Program=Program+1
                                                                                            Not_compress_block_01=Infromation_program[:6]
                                                                                            Not_compress_block_01_number=int(Not_compress_block_01,2)
                                                                                            Infromation_program=Infromation_program[6:]

                                                                                            Sixty_bits=63
                                                                                            Times_bits=Sixty_bits-Not_compress_block_01_numbers

                                                                                            Not_compress_block_01_number_size_of_block=Infromation_program[:Times_bits]
                                                                                            Times_zeroes_size_of_block_number=int(Not_compress_block_01_number_size_of_block,2)
                                                                                            Infromation_program=Infromation_program[Times_bits:]
                                
                                                                                
                                                                                    if find_matches1_1==0 and Blocks_count!=Times_zeroes_size_of_block_number:
                                                                                        size_data4=str_find_tree_maches1[:0]+b+str_find_tree_maches[2:]
                                                                                        size_data12=size_data12+size_data4
                                                                                        
                                                                                       
                                                                                        blocks2=Not_compress_size_of_block_number
                                                                                        
                                                                                    else:
                                                                                        size_data4=str_find_tree_maches1
                                                                                        size_data12=size_data12+size_data4
                                                                                        
                                                                                        
                                                                                        blocks2=compress_size_of_block_number
                                                                                        
                                                                                    
                                                                                    block=block+blocks2
                                                                                    
                                                        times_compression=times_compression+1
                                                        #print(times_compression)
                                                        size_data3=size_data12
                                                        #print(size_data12)
                                                        
                                                        
                                                        
                                                        size_data12=""
                                                        

                                        Times_count=Times_count+1
                                        
                                        
                                    lenf=len(size_data3)
                                        
                                    add_bits118=""
                                    count_bits=8-lenf%8
                                    z=0
                                   
                                    if count_bits!=0:
                                          if count_bits!=8:
                                               while z<count_bits:
                                                   add_bits118="0"+add_bits118
                                                   z=z+1
                                                                    
                                                                    
                                    size_data3=add_bits118+size_data3
                                      
                                    n = int(size_data3, 2)
                                    
                                    
                                    qqwslenf=len(size_data3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                 
                               
                                    sssssw=len(jl) 
                                  
                                   

                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                                    
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:
                                        	
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

 
                  
self=""                                
d=compression()
    
xw=d.cryptograpy_compression()
print(xw)

xw1=d.cryptograpy_unpack()
print(xw1)
