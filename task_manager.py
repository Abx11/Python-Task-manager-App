#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime
#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
# Code in line 12 - 26 create Functions that check for valid users as well as their password.
           
def check_valid_user_and_password(valid_user, valid_password):
           
    with open('user.txt', 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            global username
            username = line.split(', ')[0]
            global password
            password = line.strip('\n').split(', ')[1]
            
            if valid_user == username and valid_password == password:
                    print(f'User, {valid_user} confirmed')
                    break
        else:
                print('User does not exist or incorrect password. Re-run program and try again.')
                exit()
# line 28 - 33 creates a functions that request the users username and password              
def general_access():
    
    global username_input
    
    username_input = input('Enter username: ')
    
    global valid_password
    
    valid_password = input('Enter password: ')
    
    check_valid_user_and_password(username_input, valid_password)
        
# line 36 - 71 creates a function that allows the user to add a new user and checks for existing users to ensure there is no duplication of users  
def user_registration(new_user, confirmed_password):
    
            new_file = open('user.txt', 'r')
            
            user_list = []
            password_list = []
            
    
            for user in new_file: 
                user_info = user.split(', ')
                active_users = user_info[0]
                active_passwords = user_info[1]
                password_list.append(user_info[1])
                user_list.append(user_info[0])
    
            print(user_list)
    
            active = True
            while active:
                
                new_user = input('Enter new username: ')
                
                if new_user in user_list or confirmed_password in password_list:
                    
                    print('Username already exist or password already in use. Please choose another username and password. ') 
                    new_user = input('Enter another username: ')
                    new_user_password = input('Enter new password: ')
                    confirmed_password = input('Confirm Password: ')   
                elif new_user not in user_list:
                    print('New username confirmed')
                    new_user_password = input('Enter new password: ')
                    confirmed_password = input('Confirm Password: ')
                    
                    active = False
                    
                new_file.close()  
                 
                if new_user_password == confirmed_password:
                    
                    with open('user.txt', 'a') as file:
                        
                        file = file.write(f'\n{new_user}, {confirmed_password}')
                else: 
                    print('Passwords did not match. Please try again')
                    exit()

# line 74 - 77 calls on the user_registration function to register a new user                    
def register_user():
    
    confirmed_new_user = ''
    confirmed_password = ''
    user_registration(confirmed_new_user, confirmed_password)
     
# Code in line 81 - 104 creates Functions that create the tasks that will be added to the task file 
            
def create_task():
            task_assignee = input('To whom is the task assigned? ')
            task_title = input('What is the task title? ')
            task_description = input('What are the requirements of the task? ')
            task_date = datetime.datetime.today()
            task_due_date = input('Date format: 25 Dec 2033\nOn which date is the task due? ')
            task_complete = input('Is the task complete? ').capitalize()
            
            
            written_date = datetime.datetime.strftime(task_date,'%d ' '%b ' '%Y' )
            task_due_date = datetime.datetime.strptime(task_due_date, '%d %b %Y')
            due_date = task_due_date.strftime('%d %b %Y')

            


            
            with open('tasks.txt', 'a') as file:
                file.write(f'\n{task_assignee}, {task_title}, {task_description}, {written_date}, {due_date}, {task_complete}')
        
def add_task():
    create_task()
    
# line 110 - 126 creates functions that allows users view their all tasks
def view_tasks():
             with open('tasks.txt', 'r') as file:
                lines = file.readlines()
                task_number = 0
                num_of_tasks = len(lines)
            
                for i in range(num_of_tasks):
                    line = lines[task_number].strip('\n').split(', ')
                    task_number += 1
                    print('--------')
                    print(f'Task number: {task_number}')
                    print(f'Task assignee: ', line[0])
                    print(f'Task title: ', line[1])
                    print(f'Task description: ', line[2])
                    print(f'Task date: ', line[3])
                    print(f'Task due date: ', line[4])
                    print(f'Task complete: ', line[5])

# line 141 - 173 creates a function that allows the user to view their specific task and to edit features of their task by calling on the task editor function         
def view_edit_task():
   
   with open('tasks.txt', 'r+') as file:
      lines = file.readlines()
      choice_assignee = username_input
      task_number = 0
      chosen_task_num = 0
      all_users_tasks = {}
      global all_tasks
      all_tasks = {}
      
      for line in lines:
         assignee, task_title, task_description, task_date, task_due_date, task_complete = line.split(', ')
         task_number += 1
         chosen_task_num += 1
         all_tasks[task_number] = line.strip('\n').split(', ')
         if choice_assignee == assignee:
            all_users_tasks[task_number] = line.strip('\n').split(', ')
            # print(f'Number of tasks assigned to {assignee}: {task_number}')
            print('--------')
            print(f'Task number: {task_number}')
            print(f'Task assignee: ', assignee)
            print(f'Task title: ', task_title)
            print(f'Task description: ', task_description)
            print(f'Task date: ', task_date)
            print(f'Task due date: ', task_due_date)
            print(f'Task complete: ', task_complete)
            print(f'Number of tasks assigned to {assignee}: {task_number}')
            
      print('User Tasks')
      print(all_users_tasks)
    
      task_editor(all_users_tasks)
      
        
# line 190 - 240 creates a function that allows users to edit feature of their task and writes those changes to the tasks.txt   
def task_editor(all_users_tasks):
      tasks = all_tasks
    
      chosen_task_num = int(input('Enter task number or -1 to exit program:'))
      
      if chosen_task_num <= -1:
        exit()
      task_chosen = all_users_tasks[chosen_task_num]
      print(task_chosen)
      print(task_chosen[-1])
      
    
      if chosen_task_num >= 1:
        task_chosen = all_users_tasks[chosen_task_num]
        # print(task_chosen)
        task_edit = input('''How would you like to update your task?
                            Chose your option below:
                            ma - Mark task as complete
                            ed - Edit your task
                            Input here: ''').lower()
        
        if task_edit == 'ma':
            
            task_chosen[-1] = 'Yes'
        elif task_edit == 'ed':
            edit = input('''Would you like to change the task assignee or
                            change the due date of task?
                            
                            a - assignee
                            dd - due date
                            Input here: ''').lower()    
            if edit == 'a':
                updated_assignee = input('Enter new username: ')
                task_chosen[0] = updated_assignee
                print('New assignee to task: ', updated_assignee)
                
            elif edit == 'dd':
                due_date_index = -2
                print('Date format: 12 Oct 2012')
                updated_due_date = input('Enter new due date: ')
                task_chosen[due_date_index] = updated_due_date
                print('Updated due date: ', updated_due_date)
                
        print('\n'.join([', '.join(t) for t in all_users_tasks.values()]))
        
        all_users_tasks
        all_tasks

        for key, value in all_users_tasks.items():
            all_tasks[key] = value

        print(all_tasks)
               
        with open('tasks.txt', 'w+') as file:
            file.write('\n'.join([', '.join(t) for t in all_tasks.values()]))
            
# Code in line 243 - 280 creates functions that create overview files that output the stats of the task manager   
def task_report():
      tasks = {}
        
      complete_tasks = 0                        
      incomplete_tasks = 0 
      overdue_tasks = 0
      
       
      with open('tasks.txt', 'r') as file:
         lines = file.readlines()
         total_tasks = len(lines)
         
         for line in lines:
               date = datetime.datetime.today()
               task_due_date = line.split(', ')[4]
               due_date = datetime.datetime.strptime(task_due_date, '%d ' '%b ' '%Y' )
               task = line.strip('\n').split(', ')
            
               if task[-1].strip('\n') == 'No':
                        incomplete_tasks += 1
               elif task[-1].strip('\n') == 'Yes':
                        complete_tasks += 1
               if due_date <= date and task[-1].strip('\n') == 'No':
                  overdue_tasks += 1 
                        
         percentage_complete_tasks = (complete_tasks/total_tasks)*100
         percentage_incomplete_tasks = (incomplete_tasks/total_tasks)*100     
         percentage_overdue_tasks  = (overdue_tasks/total_tasks)*100      
         with open('tasks_overview.txt', 'w+') as file:
            file.write(f'Tasks Manager Task Reports\nNumber of tasks: {total_tasks}\nNumber of complete task: {complete_tasks}\nNumber of incomplete task: {incomplete_tasks}\nNumber of overdue tasks for user: {overdue_tasks}\nPercentage of complete tasks: {percentage_complete_tasks:.2f}%\nPercentage of incomplete tasks: {percentage_incomplete_tasks:.2f}%\nPercentage of overdue tasks: {percentage_overdue_tasks:.2f}%')
            
      print(f'''Tasks Manager Task Reports:
            Number of tasks: {total_tasks}
            Number of complete task: {complete_tasks}
            Number of incomplete task: {incomplete_tasks}
            Number of overdue tasks for user: {overdue_tasks}
            Percentage of complete tasks: {percentage_complete_tasks}%
            Percentage of incomplete tasks: {percentage_incomplete_tasks}%
            Percentage of overdue Tasks: {percentage_overdue_tasks}%''')                    

# line 283 - 332 creates a function that reads the task.txt to write the stats of each individual user to a user_overview.txt file 
def check_users_task():
    users_tasks = {}

    with open('tasks.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        task = line.strip('\n').split(', ')
        user_with_task = task[0]
        task_status = task[-1].strip('\n')

        if user_with_task not in users_tasks:
            users_tasks[user_with_task] = {
                'num_of_tasks': 0,
                'complete_tasks': 0,
                'incomplete_tasks': 0,
                'overdue_tasks': 0
            }

        users_tasks[user_with_task]['num_of_tasks'] += 1

        if task_status == 'Yes':
            users_tasks[user_with_task]['complete_tasks'] += 1
        elif task_status == 'No':
            users_tasks[user_with_task]['incomplete_tasks'] += 1
            due_date = datetime.datetime.strptime(task[4], '%d %b %Y')
            if due_date <= datetime.datetime.today():
                users_tasks[user_with_task]['overdue_tasks'] += 1

    with open('user_overview.txt', 'w') as file:
        for user, stats in users_tasks.items():
            
            num_of_tasks = stats['num_of_tasks']
            complete_tasks = stats['complete_tasks']
            incomplete_tasks = stats['incomplete_tasks']

            percentage_of_tasks_complete = (complete_tasks / num_of_tasks) * 100 if num_of_tasks > 0 else 0
            
            percentage_of_tasks_incomplete = (incomplete_tasks / num_of_tasks) * 100 if num_of_tasks > 0 else 0
            
            percentage_overdue_tasks = (stats['overdue_tasks'] / num_of_tasks) * 100 if num_of_tasks > 0 else 0

            file.write(f'{user}, {num_of_tasks}, {complete_tasks}, {incomplete_tasks}, '
                       f'{percentage_of_tasks_complete:.2f}%, {percentage_of_tasks_incomplete:.2f}%, '
                       f'{percentage_overdue_tasks:.2f}%\n')

            print(f'''Username: {user}
                Number of tasks: {num_of_tasks}
                Number of complete tasks: {complete_tasks}
                Number of incomplete: {incomplete_tasks}
                Percentage of tasks complete: {percentage_of_tasks_complete:.2f}%
                Percentage of tasks incomplete: {percentage_of_tasks_incomplete:.2f}%
                Percentage of overdue tasks: {percentage_overdue_tasks:.2f}%''')
            
# line 334 - 342 creates function that reads the user.txt and calls on the check_users_task function to display the task manager stats of each user    
def user_overview():
   
   with open('user.txt', 'r') as file:
      lines = file.readlines()
      for line in lines:
         username = line.split(', ')[0]
        
      print(f'\nTask Manager User Reports:')
      check_users_task()                     
# Code in lines 344 - 378 creates a function that displays stats from overview files to the terminal                                  
def display_stats():
    
   with open('tasks_overview.txt', 'r') as file:
      lines = file.readlines()

      for line in lines:
         total_tasks = lines[1] 
         complete_tasks = lines[2]
         incomplete_tasks = lines[3]
         overdue_tasks = lines[4]
         percentage_complete_tasks = lines[5] 
         percentage_incomplete_tasks = lines[6]
         percentage_overdue_tasks = lines[7] 
         
      print(f'''Tasks Manager Task Reports:
                  {total_tasks}
                  {complete_tasks}
                  {incomplete_tasks}
                  {overdue_tasks}
                  {percentage_complete_tasks}
                  {percentage_incomplete_tasks}
                  {percentage_overdue_tasks}''')
      
   with open('user_overview.txt', 'r') as file:
      lines = file.readlines()
      
      print(f'\nUser reports:')
      
      for line in lines:
         username, num_of_users_tasks, complete_tasks, incomplete_tasks, percentage_complete_tasks, percentage_incomplete_tasks, percentage_overdue_tasks = line.strip('\n').split(', ')
          
         print(f'''
                  Username: {username}
                  Number of users tasks: {num_of_users_tasks}
                  Number of complete tasks: {complete_tasks} 
                  Number of incomplete tasks: {incomplete_tasks}
                  Percentage of complete tasks: {percentage_complete_tasks}
                  Percentage of incomplete tasks:{percentage_incomplete_tasks}
                  Percentage of overdue tasks: {percentage_overdue_tasks}''')
    


# line 383 - 419 creates a function the implements the user's menu choices
def menu_action(menu):
    
    if menu == 'r':
        pass
            
        register_user()
        

    elif menu == 'a':
        pass
            
        add_task()

    elif menu == 'va':
        pass
                    
        view_tasks()
        

    elif menu == 'vm':
        pass
        view_edit_task()

    elif menu == 'gr':
        task_report()
        user_overview()
                    
    elif menu == 'ds':
        display_stats()
        # before displaying stats make sure to run gr to ensure creation of overview files if they do not exist 
        

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")

        
        
# line 424 - 449 creates a function that checks how the user accessing the program and displays the relevant menu
def active_user(access_type):
    
    general_access()
    
    if access_type == 'admin':
        
        if username_input == 'admin' and username_input == username and valid_password == password and  valid_password == 'adm1n':
            
            print('Running Program as Admin: ')
            global menu
            while True:
                menu = input('''Select one of the following options:
                r - register a user
                a - add task
                va - view all tasks
                vm - view my tasks
                gr - generate report
                ds - display stats
                e - exit
                : ''').lower()
                menu_action(menu)
                
    elif access_type == 'user':
        
        if  username_input == username and valid_password == password:
            
            while True:
                menu = input('''Select one of the following options:
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
        : ''').lower()
                menu_action(menu)

            
# line 452 - 458 requests how the will be accessing the program and calls on the active_user function to display the relevant menu           
access_type = input('Are you accessing the program as an admin or user? ').lower()

if access_type == 'user':

    active_user('user')
elif access_type == 'admin':
    active_user('admin')
else:
    print('Incorrect Input. Re-run program and try again.')