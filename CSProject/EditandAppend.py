#Defining function to perform edits
def Edit(file_name):
  from ErrorDetect import err
  import csv
  open_file=open(file_name,'r',newline='')
  read_file=csv.DictReader(open_file)
  reply='1'
  edits={}
  Items=[r['SNo.'].lower() for r in read_file]
  Columns=['sno.','product','price','quantity per purchase','stock']

  while reply.lower() in ['y','yes','1']:


  #Asking the user for edits
    try:
      select=input('Enter Serial number of grocery you want to edit in this aisle:')
    except:
      select=err(select,Items,f'Enter value from {Items[0]} to {Items[-1]}')
    #Error detection
    if select.lower() not in Items:
      select=err(select,Items,f'Enter value from {Items[0]} to {Items[-1]}')
    column=input("Enter columns you want to edit (Seperate columns by comma): ")
    column= column.lower().split(',')

    #Error detection
    for i in column:
      if i not in Columns:
        column=err(column,Columns,"Column not in table OR Columns not seperated by comma")

    #Creating dictionary to store edits
    edits_column={}
    for i in column:
      value=input(f"Enter revised value of {i}: ")
      edits_column[i.title()]=value
    edits[select]=edits_column
    reply=input("Do you want to edit more in this Aisle (Yes--1/No--0):")
  open_file.close()

  #Creating temporary file for updating  
    #Opening target file and recording old data
  with open(file_name,'r',newline='') as open_file:
      read_file=csv.DictReader(open_file)
      ndata=[{'SNo.':'SNo.','Product':'Product','Price':'Price','Quantity Per Purchase':'Quantity Per Purchase','Stock':'Stock'}]
      for i in read_file:
          ndata.append(i)

  #Performing edits
  for rows in ndata:
    if rows['SNo.'] in edits:
      for j in edits[rows['SNo.']]:
        rows[j]=edits[rows['SNo.']][j]

  #Overwriting new data
  with open(file_name,'w') as open_file:
      write_file=csv.DictWriter(open_file,['SNo.','Product','Price','Quantity Per Purchase','Stock'])
      write_file.writerows(ndata)

#Defining function to perform appends
def Append(file_name):
  #Importing files
  from ErrorDetect import err
  import csv

  #Creating list with all Serial Numbers
  open_file=open(file_name,'r',newline='')
  read_file=csv.reader(open_file)
  Items=[r[0] for r in read_file]
  open_file.close()

  #Appending data to the file
    #Opening files
  open_file=open(file_name,'a+',newline='')
  read_file=csv.reader(open_file)
  write_file=csv.writer(open_file)

    #Defining Vriables
  reply='1'
  n=len(Items)

    #Asking for row values
  while reply.lower() in ['y','yes','1']:
    column=['product','price','quantity per purchase','stock']
    row=[n]
    for i in column:
      field=input(f'Enter {i}: ')
      row.append(field)
    write_file.writerow(row)
    reply=input("Do you want to add more in this aisle ('1' for yes, '0' for no): ")
    if reply not in ['0','1']:
      reply=err(reply,['0','1'],"Enter '0' for yes and '1' for no")
    n+=1
  open_file.close() 
