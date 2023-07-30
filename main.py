from collections import Counter
import datetime
#GeeksforGeeks. (2023). Queue in Python. GeeksforGeeks. https://www.geeksforgeeks.org/queue-in-python/
import copy
####################################################################################
#program start
def mainProgram():

  list01 = []
  with open("text_file1.txt" ,"r+") as file:
    for line in file :
      ticket_info = line.strip().split(",")
      list01.append(ticket_info)

  #print(list01)
  # the info within the tickit are separated by a comma
    
  # convert the text file to a dictionary 

  list01_copy = copy.deepcopy(list01) # as list01 is needed later
  dictText = {}
  dictText = {lst[0]:lst[1:] for lst in list01_copy}
  #print(dict00)


############################################
####### Admin 
############################################

  def admin():
    print("welcome admin !")


    def systemDisplay(): 
  
    
      print("which of the following choice you would like to choose:\n" + 
        "1-Display Statistics\n " +
        "2-Book a Ticket\n" +
        "3-Display all Tickets\n" +
        "4-Change Ticket Priority\n"
        "5-Disable Ticket\n"
        "6-Run Events\n"
        "7-Exit\n")

      print("----------------------")
      choice = input("please choose one of the following choices to proceed: ")
      print("----------------------")
      print("----------------------")

###################
######### choice 1 
###################

      list02 = []  
      def choice1():
        for key, value_tuple in dictText.items():
          event = value_tuple[0]
          list02.append(event)

        event_count = Counter(list02)
        most_event= event_count.most_common(1)[0][0]
        print("the event containing most tickets is:",most_event)
        print("----------------------")
        systemDisplay()
        
#Python, R. (2023). Python’s Counter: The Pythonic Way to Count Objects.realpython.com.https://realpython.com/python-counter/

###################
######### choice 2 
###################

      def choice2():
        ticket = "tick"+ str(len(dictText)+1)
        
# usen the length of dictText i know how many tickits i have, put we need it in string not int
        while True :
          try:
              event_id_number= int(input("enter the event ID number"))
              if 1 <= event_id_number <= 100 :
                event_id_number_new = str(event_id_number).zfill(3) 
                event_id ="ev" + event_id_number_new
                break 
#Python 3 - String zfill() Method. (n.d.). Tutorialspoint. https://www.tutorialspoint.com/python3/string_zfill.htm

              else: 
                print("invalid input,Please enter a valid event ID")

          except ValueError:
            print("INvalid input, please enter a valid integer")
      
        username = input("enter the username:")

       
        
        while True :
          try:
              date_year = int(input("please enter the year of the event taking place"))
              if isinstance(date_year,int):   
                date_year2 = str(date_year).zfill(4)
              else:
                print("invalid input please enter a numerical date")
                choice3()
            
            
              date_month = int(input("please enter the month the event takes place"))
              if isinstance(date_month,int): 
                date_month2= str(date_month).zfill(2)
              else:
                print("invalid input please enter a numerical date")
                choice3()
                
              date_day = int(input("please enter at which day of the month the event takes place "))
              if isinstance(date_day,int): 
                date_day2= str(date_day).zfill(2)
                break
              else:
                print("invalid input please enter a numerical date")
                choice3()
          except ValueError:
            print("Invalid input, please enter the date as a numerical expression")
          
        date1 = date_year2 + date_month2 + date_day2   
        
        priority = input("Enter the priority:") 
        new_ticket_info = [ticket, event_id, username, date1, priority]
        dictText[ticket] = tuple(new_ticket_info)
        print(dictText[ticket])
        systemDisplay()

###################
######### choice 3
###################

#### time filter 
      def is_future_date(date_str):
    # Get the current date as a datetime object
        today = datetime.date.today()
    # Convert the date string from the format "YYYYMMDD" to a datetime object
        date = datetime.datetime.strptime(date_str, "%Y%m%d").date()
        return date >= today 

    # choice 3 
      def choice3():
        
      # sort build in function uses timesort which is a merge algortihm and           the fastest for partially reversed data as in that case 

      # Sorting based on index 1 (event) and then index 3 (date)
        sorted_data = sorted(filtered_list, key=lambda x:(x[1],x[3]),reverse =False)
        print(sorted_data)

###################
######### choice 4
###################
      def choice4():
        user_ticket = int(input("please enter only the ticket number you are searching for"))
        user_ticket1 = str(user_ticket).zfill(3)
        ticket_find = "tick" + user_ticket1
        print(ticket_find)
        priority_ticket = input("please enter the priority of the following ticket number you entered")
        
        found = False 
        for i in list01:
          id = i[0]
          id = id.strip()
          priortyy = i[4]
          priortyy = priortyy.strip()
          #print(list01)
          if ticket_find in id and priority_ticket in priortyy :
            print("the ticketid you are searching for is:",i)
            found = True
            break
          
        if not found :
          print("ticket id or priority do not match please try again")
          systemDisplay()
        print("--------------------")
        print("--------------------")
        new_priority = input("please enter the new priority you want to assign for the ticketID:")
        
        dictText[ticket_find][3] = new_priority
        print("the new information to ticket",ticket_find,"is:\n", dictText[ticket_find])
        systemDisplay()

###################
######### choice 5
###################
      def choice5():
        print("-------------------")
        remove_tick = int(input("please enter only the ticket number for the ticket you want to remove"))
        remove_tick1 = str(remove_tick).zfill(3)
        remove1 = "tick" + remove_tick1
        print(remove1)

        if remove1 in dictText.keys():
          del dictText[remove1]
          print(remove1,"was removed from the list")

        else:
          print("the ticket ID was not found")
          systemDisplay()
        
        
        #print(dictText)

###################
######### choice 6
###################
      def today_date(date_str):
    # Get the current date as a datetime object
          today1 = datetime.date.today()
    # Convert the date string from the format "YYYYMMDD" to a datetime object
          date01 = datetime.datetime.strptime(date_str, "%Y%m%d").date()
          return date01 == today1

          
         



      def choice6():
        
        sorted_data1 = sorted(new_list, key=lambda x:int(x[4]),reverse =False)
        print(sorted_data1)

      
###################
######### calling choices 
###################
      while True :
        

        try:
          choice = int(choice)
          if choice == 1:
            choice1()
            systemDisplay()
          elif choice == 2:
            choice2()
            
          elif choice == 3:
            #print(list01)
            filtered_list=[]
            for i in list01:
              date_str =i[3]
              date_str=date_str.strip()

              if is_future_date(date_str):
                filtered_list.append(i)

            #print(filtered_list)
            choice3()
            systemDisplay()
        
                
          elif choice == 4:
            choice4()
                
          elif choice == 5:
            choice5()
                
          elif choice == 6:
            new_list=[]
            for i in list02_copy:
              date_str =i[3]
              date_str=date_str.strip()

              if today_date(date_str):
                new_list.append(i)
            #print(new_list)
        
            choice6()
          
                
          elif choice == 7:
            print("Exiting the program. Goodbye!")
            exit()
          else:
            print("Invalid choice. Please try again.")
            systemDisplay()

        except ValueError :
          print("please enter one of the following choices as a numerical value")
          systemDisplay()
      
      

                   
    systemDisplay()

############################################
####### User
############################################
  def user():

    print("welcome ", user_name1)

    def menueOption():
      print("__________Menue system________")
      print("1) Book a Ticket \n2) Exit")

      choice = input("please choose one of the following ")
      print("-------------------")

#######################
######### choice 1 user
#######################
      def choice1_user():
        ticket = "tick"+ str(len(dictText)+1)
        
# usen the length of dictText i know how many tickits i have, put we need it in string not int
        while True :
          try:
              event_id_number= int(input("enter the event ID number"))
              if 1 <= event_id_number <= 100 :
                event_id_number_new = str(event_id_number).zfill(3) 
                event_id ="ev" + event_id_number_new
                break 
#Python 3 - String zfill() Method. (n.d.). Tutorialspoint. https://www.tutorialspoint.com/python3/string_zfill.htm

              else: 
                print("invalid input,Please enter a valid event ID")

          except ValueError:
            print("INvalid input, please enter a valid integer")
      
        username = user_name1

       
        
        while True :
          try:
              date_year = int(input("please enter the year of the event taking place"))
              if isinstance(date_year,int):   
                date_year2 = str(date_year).zfill(4)
              else:
                print("invalid input please enter a numerical date")
                choice1_user()
            
            
              date_month = int(input("please enter the month the event takes place"))
              if isinstance(date_month,int): 
                date_month2= str(date_month).zfill(2)
              else:
                print("invalid input please enter a numerical date")
                choice1_user()
                
              date_day = int(input("please enter at which day of the month the event takes place "))
              if isinstance(date_day,int): 
                date_day2= str(date_day).zfill(2)
                break
              else:
                print("invalid input please enter a numerical date")
                choice1_user()
          except ValueError:
            print("Invalid input, please enter the date as a numerical expression")
          
        date1 = date_year2 + date_month2 + date_day2   
        
        priority = ("0")
        new_ticket_info = [ticket, event_id, username, date1, priority]
        dictText[ticket] = tuple(new_ticket_info)
        print(dictText[ticket])
        menueOption()

#######################
######### choice 2 user
#######################
      def choice2_user():
        with open("text_file1.txt", "w") as file:
          for ticket_id, ticket_info in dictText.items():
            line = ticket_id + "," + ",".join(ticket_info) + "\n"
            file.write(line)
            exit()


###############################
######### calling choices user 
###############################
      while True :
        
        try:
          choice = int(choice)
          if choice == 1 :
            choice1_user()

          elif choice ==2 :
            choice2_user()
                   
          else: 
            print("please choose one of the above choices")
            menueOption()

            menueOption()
        
        except ValueError: 
          print("please enter one of the following choices as a numerical value")
          menueOption()
          
    menueOption()

##########################################
##### login type 
##########################################
  user_name1 = input("please enter the username:  ")
  password1 = input("please enter the password:  ")

  if user_name1 != "admin" or password1== " " : 
    user()

  max_attempts = 5 # this is the maximum he can enter
  attempts = 1 # this is the current counting 

  while user_name1 == "admin" :
    password = "admin123123"
    if password1 == password :
      admin()
    elif password1 != password :
      print("incorrect login please try again")
      user_name1 = input("please enter the username:  ")
      password1 = input("please enter the password:  ")
      attempts += 1
      if attempts > max_attempts: 
        print("you have exeeded the maximum number of logins")
        exit() # will terminate the programm(python build in function1)

mainProgram()