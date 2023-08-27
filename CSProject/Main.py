import EditandAppend 
import RandD
import ErrorDetect
import CustomerData
import csv

print('Welcome!')
User=input("Are you a customer or employee ('0' for customer and '1' for employee): ")

#Asking User whether they are a customer
if User not in ['0','1']:
    User=ErrorDetect.err(User,['0','1'],"Enter '0' for customer and '1' for employee")
#Customer interface
if User=='0':
    DWBM='1'
    while DWBM=='1':
        
        RandD.RandD("AISLES.csv")
        Aisle=input("Enter the corresponding number for the aisle you want to browse: ")
        if Aisle not in [str(i) for i in range(1,6)]:
            Aisle=ErrorDetect.err(Aisle,[str(i) for i in range(1,6)],"Put values from 1 to 5")
        
        if Aisle == '1':
            RandD.RandD("FruitsAndVeggies.csv")
            CustomerData.CustData("FruitsAndVeggies.csv")
        elif Aisle == '2':
            RandD.RandD("Dairy.csv")
            CustomerData.CustData("Dairy.csv")
        elif Aisle == '3':
            RandD.RandD("PULSES AND STAPLES.csv")
            CustomerData.CustData("PULSES AND STAPLES.csv")
        elif Aisle == '4':
            RandD.RandD("Packed Foods.csv")
            CustomerData.CustData("Packed Foods.csv")
        else:
            RandD.RandD("Beverages and Desserts.csv")
            CustomerData.CustData("Beverages and Desserts.csv")
        
        DWBM=input("Do you want to browse more ('1' for yes, '0' for no): ")
        if DWBM not in ['0','1']:
            DWBM=ErrorDetect.err(DWBM,['0','1'],"Enter '0' for no and '1' for yes")
    
    RandD.RandD("CustData.csv")
    CustomerData.CustSum()
    CustomerData.CustDump()
    print('Thank you for your purchase')


#Employee Interface
else:
    DWTE='1'
#Login ID system
    count=0
    #Acessing fields
    with open('LoginID.csv') as  myfile:
            f=csv.reader(myfile)
            Name=[k for k in f]
            IDlst=[i[0] for i in Name]

    #Login Attempt
    while count!=3:
        ID=input("Enter 6 digit login id: ")
        if ID in IDlst:
            break
        else:
            count+=1
            
    #Alert if incorrect 
    else:
        x=0
        while x!=1:
            print("Alert!")

    for i in Name:
        if i[0]==ID:
            print(f"Welcome {i[1]}")

    while DWTE=='1':       
        RandD.RandD("AISLES.csv")
        Aisle=input("Enter the corresponding number for the aisle you want to edit: ")
        if Aisle not in [str(i) for i in range(1,6)]:
            Aisle=ErrorDetect.err(Aisle,[str(i) for i in range(1,6)],"Put values from 1 to 5")

        if Aisle == '1':
            RandD.RandD("FruitsAndVeggies.csv")
            response=input("Do you want to edit(Press 0) or append(Press 1)? ")
            response=ErrorDetect.err(response,['0','1'], "Press 0 to edit or 1 to append.")
            if response=='1':
                EditandAppend.Append("FruitsAndVeggies.csv")
            else:
                EditandAppend.Edit("FruitsAndVeggies.csv")
        elif Aisle == '2':
            RandD.RandD("Dairy.csv")
            response=input("Do you want to edit(Press 0) or append(Press 1)? ")
            response=ErrorDetect.err(response,['0','1'], "Press 0 to edit or 1 to append.")
            if response=='1':
                EditandAppend.Append("Dairy.csv")
            else:
                EditandAppend.Edit("Dairy.csv")
        elif Aisle == '3':
            RandD.RandD("Pulses and Staples.csv")
            response=input("Do you want to edit(Press 0) or append(Press 1)? ")
            response=ErrorDetect.err(response,['0','1'], "Press 0 to edit or 1 to append.")
            if response=='1':
                EditandAppend.Append("Pulses and Staples.csv")
            else:
                EditandAppend.Edit("Pulses and Staples.csv")
        elif Aisle == '4':
            RandD.RandD("Packed Foods.csv")
            response=input("Do you want to edit(Press 0) or append(Press 1)? ")
            response=ErrorDetect.err(response,['0','1'], "Press 0 to edit or 1 to append.")
            if response=='1':
                EditandAppend.Append("Packed Foods.csv")
            else:
                EditandAppend.Edit("Packed Foods.csv")
        else:
            RandD.RandD("Beverages and Desserts.csv")
            response=input("Do you want to edit(Press 0) or append(Press 1)? ")
            response=ErrorDetect.err(response,['0','1'], "Press 0 to edit or 1 to append.")
            if response=='1':
                EditandAppend.Append("Beverages and Desserts.csv")
            else:
                EditandAppend.Edit("Beverages and Desserts.csv")
        
        DWTE=input("Do you want to edit more ('1' for yes, '0' for no): ")
        if DWTE not in ['0','1']:
            DWTE=ErrorDetect.err(DWTE,['0','1'],"Enter '0' for no and '1' for yes")

