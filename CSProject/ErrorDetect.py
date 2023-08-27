def err(input_var,paralist,reason):

  #Initial variables
  x=0

  #Defining conditions for various data types to be used
    #String
  if type(input_var)== str:
    while input_var not in paralist: 
        input_var=input(f'Enter appropiate value ({reason}): ')

    #List
  elif type(input_var)== list:
    while x==0: 
        input_var=input(f'Enter appropiate value ({reason}): ')
        input_var= input_var.lower().split(',')
        for i in input_var:
          x=1
          if i not in paralist:
            x=0
            break

    #Integer
  else:
     while input_var not in paralist: 
        input_var=int(input(f'Enter appropiate value ({reason}): '))

  #Returning value
  return input_var