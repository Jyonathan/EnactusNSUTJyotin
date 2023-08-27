import ErrorDetect
import csv
def CustDataInner(ReadFile):
    #Importing modules and creating variables
    open_file=open(ReadFile,'r',newline='')

    read_file=csv.DictReader(open_file)
    SNoList=[int(i["SNo."]) for i in read_file]
    SNo=None
    try:
        SNo=int(input("Enter SNo. of item you want to select: "))
    except:
        SNo=ErrorDetect.err(SNo,SNoList,f'Enter value from {SNoList[0]} to {SNoList[-1]}')
    if SNo not in SNoList:
        SNo=ErrorDetect.err(SNo,SNoList,f'Enter value from {SNoList[0]} to {SNoList[-1]}')

    open_file.seek(0)
    for i in read_file:
        if i["SNo."]=='SNo.':
            continue
        if int(i["SNo."])==SNo:
            global x
            x=int(i["Stock"])
    Stock=None      
    try:
        Stock=int(input("Enter quantity you want "))
    except:
        
        Stock=ErrorDetect.err(Stock,list(range(x+1)),f'Enter value from 0 to {x}')
    if Stock not in list(range(x+1)):
        Stock=ErrorDetect.err(Stock,list(range(x+1)),f'Enter value from 0 to {x}')
        
    open_file.seek(0)
    
    #Writing data to list object after reduction in stock value
    #Customer would buy certain items hence their stock needs to be changed
    new_data=[]
    for i in read_file:
        if i["SNo."]==str(SNo):
            i['Stock']=int(i['Stock'])-Stock     
        new_data.append(i)
        
    #Closing files
    open_file.close()

    #Opening target file from where customer has selected groceries and Customer Billing file
    open_file1=open(ReadFile, 'w')
    open_file2=open("CustData.csv", 'a',newline='')
    
    write_file1=csv.DictWriter(open_file1,['SNo.','Product','Price','Quantity Per Purchase','Stock'])
    write_file2=csv.writer(open_file2)
    
    #Writing data in list object to target file
    for i in new_data:
        write_file1.writerow(i)

    #Writing purchase to customer billing file    
    for i in new_data:
        if i['SNo.']==str(SNo):
            y=[]
            lst=list(i.values())
            for j in lst[1:4]:
                y.append(j)
            y.append(Stock)
            
            write_file2.writerow(y)
    #Closing file
    open_file1.close()
    open_file2.close()

def CustData(ReadFile):
    response=1
    while response==1:
        CustDataInner(ReadFile)
        response=None
        try:
            response=int(input("Do you want to select more products from this Aisle (0--no, 1--yes): "))
        except:
            response=ErrorDetect.err(response,[0,1],"'0' for no and '1' for yes ")
        if response not in [0,1]:
            response=ErrorDetect.err(response,[0,1],"'0' for no and '1' for yes ")

#Function to calculate total cost of purchase
def CustSum():
    open_file=open("CustData.csv",'r',newline='')
    reader_obj=csv.reader(open_file)
    total=0
    open_file.seek(0)
    for i in reader_obj:
        if i[0]=="Product":
            continue
        else:
            total+=int(i[1])*int(i[3])
    print("Your bill total is ",total)

#Function to delete previous purchase data
def CustDump():
    open_file=open("CustData.csv", 'w')
    write_file=csv.writer(open_file)
    write_file.writerow(['Product','Price','Quantity Per Purchase','Amount Purchased'])
