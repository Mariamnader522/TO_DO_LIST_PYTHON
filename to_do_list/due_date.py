
import json
import datetime
def due_date ():
  name=input("enter the task ")
  try:
    with open ("tasks.json","r") as file :  #access the file in read mood
        data=json.load(file)
  except FileNotFoundError:
    print("tasks file not found")
    
  for task in data ["Tasks"]:
    if 'task_name' in task and task['task_name']==name: #check if there is task in that name or not
     task_date=task['due_date']                                                           
     target_date=datetime.datetime.strptime(task_date,'%Y-%m-%d').date()    #transmit date from string into opject
     today_date=datetime.datetime.now().date()      # the date of today
     date_diff=target_date-today_date           #the deadline in days, time form  
     print("the remaining time for the task is ", date_diff.days)  
    else:
        print("there is no task in this name")
  
 
