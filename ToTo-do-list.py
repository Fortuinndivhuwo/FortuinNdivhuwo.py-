print("*" * 12+ "TO-DO_LIST program" + "*" * 13)
print()
def add_task():
    global all_task
    print("*" * 40)
    name_of_task = input("Enter new task: ")
    all_task.append(name_of_task)
            
def done_task():
    global all_task
    while True:
        try:
           done_task = int(input("Enter position of done task e.g 3.write homework is 3: "))
           break
        except ValueError:
            continue
    all_task.remove(all_task[done_task -1])
    

all_task = []

 
while True:
     print( "—" * 14+ " List of tasks " + "—" * 14)
     if len(all_task) == 0:
         print()
         print(" " * 15 +"(list empty)")
     else:
         n = 0
         for task in all_task:
             n += 1
             print(f"{n}. {task}")
             
     print()        
     print("Options:")       
     print("1. Add new task")
     print("2. Done task")
     print("3. Quit")
     while True:
         try:
            choice = int(input("Enter what you would like to do 1/2/3: ")) 
            break
         except ValueError:
              print("invalid input,try again")
              continue
     
     if choice == 1:
            add_task()
     elif choice == 2 and len(all_task) != 0:
            done_task() 
     elif choice  == 3:
         print("*" * 47)
         print("Dont forget what you need to do, BYE (^.^)")     
         print("—" * 47) 
         break 
     else:
         print("Error")  
