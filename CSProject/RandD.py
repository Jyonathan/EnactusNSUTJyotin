def RandD(file):
    #Importing modules
    import csv

    #Opening target file
    open_file= open(file,'r')
    read_file= csv.reader(open_file)

    #Initial Variables
    long_1=long_2=long_3=long_4=long_5=' '
    s='*'
    
    #Finding longest strings in each column
    if file=="AISLES.csv":
        for i in read_file:
            if len(long_1)<len(i[0]):
                long_1=i[0]
            if len(long_2)<len(i[1]):
                long_2=i[1]
        open_file.seek(0)
    #Printing rows
        for l in read_file:
            print(l[0],' '*(len(long_1)-len(l[0])),s, end=' ')
            print(l[1],' '*(len(long_2)-len(l[1])), s,end=' ')
            print()

    #Closing file
        open_file.close()
    elif file=="CustData.csv":
        for i in read_file:
            if len(long_1)<len(i[0]):
                long_1=i[0]
            if len(long_2)<len(i[1]):
                long_2=i[1]
            if len(long_3)<len(i[2]):
                long_3=i[2]
            if len(long_4)<len(i[3]):
                long_4=i[3]
        open_file.seek(0)
    #Printing rows
        for l in read_file:
            print(l[0],' '*(len(long_1)-len(l[0])),s, end=' ')
            print(l[1],' '*(len(long_2)-len(l[1])), s,end=' ')
            print(l[2],' '*(len(long_3)-len(l[2])), s,end=' ')
            print(l[3],' '*(len(long_4)-len(l[3])), s,end=' ')
            print()

    #Closing file
        open_file.close()
    else:
        
        for i in read_file:
            if len(long_1)<len(i[0]):
                long_1=i[0]
            if len(long_2)<len(i[1]):
                long_2=i[1]
            if len(long_3)<len(i[2]):
                long_3=i[2]
            if len(long_4)<len(i[3]):
                long_4=i[3]
            if len(long_5)<len(i[4]):
                long_5=i[4]
        open_file.seek(0)
    #Printing rows
        for l in read_file:
            print(l[0],' '*(len(long_1)-len(l[0])),s, end=' ')
            print(l[1],' '*(len(long_2)-len(l[1])), s,end=' ')
            print(l[2],' '*(len(long_3)-len(l[2])), s,end=' ')
            print(l[3],' '*(len(long_4)-len(l[3])), s,end=' ')
            print(l[4],' '*(len(long_5)-len(l[4])), s,end=' ')
            print()

    #Closing file
        open_file.close()
