

def find_one(find):
    switcher={
        1:'หนึ่ง',
        2:'สอง',
        3:'สาม',
        4:'สี่',
        5:'ห้า',
        6:'หก',
        7:'เจ็ด',
        8:'แปด',
        9:'เก้า'
        }
    return switcher.get(find)

def divide_chunks(l, n):   
    for i in range(len(l), 0, -n):
        yield l[0 if (i-n)<0 else i-n:i]

def find_number(In,CheckPos):
    Output = ""
    while int(len(In)) != 0 and CheckPos >= 0:
        if len(In) > 1:
            #---------- สิบ ----------
            if len(In) == 2:
                Temp=int(In)/10
                In=int(In)%10
                Out = find_one(int(Temp))
                In = str(In)
                if int(Temp) == 1:
                    Output = Output + "สิบ"
                elif int(Temp) == 2:
                    Output = Output + "ยี้สิบ"
                else:
                    Output = Output + Out + "สิบ"
                if int(In) == 1:
                    In = ""
                    CheckPos = CheckPos - 1
                    Output = Output + "เอ็ด"
            #---------- ร้อย ----------
            elif len(In) == 3:
                
                Temp=int(In)/100
                In=int(In)%100

                Out = find_one(int(Temp))
                In = str(In)
                Output = Output + Out + "ร้อย"
            #---------- พัน ----------
            elif len(In) == 4:
                
                Temp=int(In)/1000
                In=int(In)%1000

                Out = find_one(int(Temp))
                In = str(In)
                Output = Output + Out + "พัน"
            #---------- หมื่น ----------
            elif len(In) == 5:
                
                Temp=int(In)/10000
                In=int(In)%10000

                Out = find_one(int(Temp))
                In = str(In)
                Output = Output + Out + "หมื่น"
            #---------- แสน ----------
            elif len(In) == 6:
                
                Temp=int(In)/100000
                In=int(In)%100000

                Out = find_one(int(Temp))
                In = str(In)
                Output = Output + Out + "แสน"
            #---------- ล้าน ----------
            elif len(In) == 7:
                
                Temp=int(In)/1000000
                In=int(In)%1000000

                Out = find_one(int(Temp))
                In = str(In)
                Output = Output + Out + "ล้าน"
            else:
                Out = find_one(int(In))
                In = ""
                CheckPos = CheckPos - 1
                print("Loop else")
                Output = Output + Out            
        else:
            Out = find_one(int(In))
            In = ""
            CheckPos = CheckPos - 1
            Output = Output + Out
    return Output


Output = ""
In = input("Input : ")

CheckPos = int(len(In)) / 7
#print(int(CheckPos))

x = list(divide_chunks(In, 7))

#Number = []
if(CheckPos > 0):
    for i in range(0,len(x)):
        print(x[i])
        In = x[i]
        Output = find_number(In,CheckPos)
        print(Output)

print("Output : ", Output)
