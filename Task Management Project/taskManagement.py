from prettytable import PrettyTable
from datetime import datetime
import re


class TaskManage:

    def is_valid_username(self, username):
        '''
        allowed:
        - A-Z, a-z  (alphabets)
        - 0-9       (digits)
        - @ . _ - # $ & * ! ?   (special character)
        - No spaces allowed
        '''
        if ' ' in username:
            return False
        
        # Check for at least one alphabet
        if not re.search(r'[A-Za-z]', username):
            return False

        # Check for at least one digit
        if not re.search(r'\d', username):
            return False

        # Check for at least one special character
        if not re.search(r'[@._\-#$%&*!?]', username):
            return False

        return True


    
    def addEmp(self):
        try:
            uname = input('enter new employee useerID:')

            if not self.is_valid_username(uname):
                print("Invalid username format! Allowed: alphabets, numbers, @ . _ - # $ % & * ! ?")
                return
            
            passwd = input('enter password:')

            with open('DEMOS/taskManagement Case STtudy/users.txt', 'r') as fp:
                for line in fp:
                    username_in_file= line.split(',')[0].strip()
                    if username_in_file.lower()==uname.lower():
                        print('user already eixist.')
                        return
                        
            
            with open('DEMOS/taskManagement Case STtudy/users.txt', 'a') as fp:
                fp.write(f'{uname}, {passwd}, user\n')
            
            print('employee onboarded successfully.')
        
        except Exception as e:
            print('Error onboarding employee :' , e)


    def alloactedTask(self):
        try:
            tid = input('Enter Task Id:')
            title = input('Enter Task title:')
            task_description = input('Enter task description:')
            assi_date = input('Enter date to assign a task (YYYY-MM-DD):')
            try:
                assi_date = datetime.strptime(assi_date, "%Y-%m-%d").date()
                #comp_date = datetime.strptime(comp_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")
                return
            
            comp_date = input('Enter the date to complete the task (YYYY-MM-DD):')

            try:
                #assi_date = datetime.strptime(assi_date, "%Y-%m-%d").date()
                comp_date = datetime.strptime(comp_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")
                return
            
            priority = input('Enter the priority for task (urgent/medium/low):')
            assignedto = input('enter to (username):')
            

            with open('DEMOS/taskManagement Case STtudy/users.txt','r') as fp:
                if assignedto  not in fp.read():
                    print('user does not exist.')
                    return
            
            with open('DEMOS/taskManagement Case STtudy/tasks.txt', 'a')as fp:
                fp.write(f'{tid} , {title} ,{task_description}, {assi_date}, {comp_date},{priority}, {assignedto} ,Pending\n')
                print('Task allocated successfully.')
        except Exception as e:
            print('Error allocating tasks:', e)

    
    def trackTasks(self):
        try:
            with open('DEMOS/taskManagement Case STtudy/tasks.txt', 'r') as fp:
                lines = [line.strip() for line in fp if line.strip()]

            if not lines:
                print('No tasks found.')
                return
            
            table  = PrettyTable()
            table.field_names = ['Task ID', ' Task Title', 'Assigned To', 'Status', 'completion date']

            for line in lines:
                parts =[x.strip() for x in line.split(',')]
                if len(parts) == 8:
                    tid, title,desc,assign_date,complete_date, priority, assigned_to, status = parts

                    if status.lower()== 'completed':
                        display_date = complete_date
                    else:
                        display_date ='__'

                    table.add_row([tid, title, assigned_to, status, display_date])
                else:
                    print(f'Skipped line due to invalid format:{line}')
            
            print("\n--- Task List ---")
            print(table)

        except FileNotFoundError:
            print('No tasks found.')
        except Exception as e:
            print('error:', e)

    def report(self):
        try:
            summary = {}
            with open ('DEMOS/taskManagement Case STtudy/tasks.txt', 'r') as fp:
                for line in fp:
                    line = line.strip()
                    if not line:
                        continue

                    parts = [x.strip() for x in line.split(',')]
                    if len(parts)!= 8:
                        print(f'Skipped line due to invalid format:{line}')
                        continue

                    tid, title,desc,assi_date, complete_date, priority,  user, status = parts

                    if user not in summary :
                        summary[user] = {'total': 0, 'completed': 0, 'in_progress':0}
                    
                    summary[user]['total'] +=1

                    if status.lower() == 'completed':
                        summary[user]['completed'] +=1
                    elif status in('inprogress', 'in progress'):
                        summary[user]['in_progress']+=1
            
            if not summary:
                print("No task data available.")
                return
            
            table = PrettyTable()
            table.field_names = ['Users', 'Total Tasks', 'Completed', 'In Progress', 'Pending']


            for user, status in summary.items():
                pending = status['total'] - status['completed'] - status['in_progress']
                table.add_row((user, status['total'], status['completed'],status['in_progress'],pending))

            print("\n--- Task Report ---")
            print(table)


        except Exception as e:
            print('Error generating report:', e)


    def myTasks(self, username):
        try:

            table = PrettyTable()
            table.field_names = ['Task ID', 'Title', 'Assigned Date', 'Target Date', 'Priority', 'Status']

            found = False


            with open('DEMOS/taskManagement Case STtudy/tasks.txt', 'r') as fp:
                for line in fp:  #  iterate over lines directly
                    line = line.strip()
                    if not line:
                        continue

                    parts = [p.strip() for p in line.split(',')]
                    if len(parts) != 8:
                        continue

                    tid, title,description,assi_date, complete_date, priority,  assignedTo, status = parts
                    
                    if assignedTo.lower() == username.lower():  # optional: case-insensitive match
                        table.add_row((tid, title, assi_date, complete_date, priority, status))
                        found = True
                
                if found:
                    print('\n ---My Tasks---')
                    print(table)
                else:
                    print('No tasks assigned.')


        except FileNotFoundError:
            print('no task data available.')

        except Exception as e:
            print('error:', e)


    def updateTaskStatus(self, username):
        try:
            with open ('DEMOS/taskManagement Case STtudy/tasks.txt', 'r') as fp:
                tasks = [line.strip() for line in fp if line.strip()]


            task_id = input('enter Task ID to update:').strip()
            updated = False
            new_task= []

            for t in tasks:
                parts = [p.strip() for p in t.split(',')]
                if len(parts) != 8:
                    new_task.append(t)
                    continue
                    
                tid, title, desc, assign_date, complete_date, priority, assignedto, status = parts

                if tid == task_id and assignedto.lower() == username.lower():
                    new_status = input('Enter new status (Pending/ In Progress / completed):')
                    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    

                    if new_status.lower() == 'completed':
                        user_date = input('Enter completion date(dd-mm-yyyy):')
                        
                        
                        try:
                            actual_date = datetime.strptime(user_date, "%d-%m-%Y")
                            complete_date = actual_date.strftime("%d-%m-%Y %H:%M:%S")
                        except ValueError:
                            print("Invalid date format! Please use dd-mm-yyyy.")
                            return   # STOP update completely

                        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                        print("\n --- Task Completion Report --- ")
                        print(f'Task updated on     :{current_time}')
                        print(f'Actual Completed on :{user_date}')

                    status = new_status
                    updated=True
                
                            
                new_task.append(f'{tid},{title},{desc},{assign_date},{complete_date},{priority},{assignedto},{status}')

            with open('DEMOS/taskManagement Case STtudy/tasks.txt', 'w') as fp:
                for line in new_task:
                    fp.write(line + '\n')

                    
            if updated:
                print('Task updated.')
            else:
                print('Task not found.')

        except Exception as e:
            print('Error updating task:', e)

        
    def taskSummary(self, username):
        try:
            total , completed , in_progress= 0, 0, 0

            with open('DEMOS/taskManagement Case STtudy/tasks.txt', 'r') as fp:
                for line in fp:
                    line = line.strip()
                    if not line:
                        continue

                    parts = [p.strip()for p in line.split(',')]
                    if len(parts)!=8:
                        continue

                    tid, title,desc,assign_date,complete_date, priority,assigned_to,status = parts

                    if assigned_to.lower()==  username.lower():
                        total +=1
                        if status.lower() == 'completed':
                            completed +=1
                        elif status.lower()== 'in progress':
                            in_progress +=1

                pending = total - completed - in_progress

                table = PrettyTable()
                table.field_names = ['Total Tasks', 'Completed', 'In Progress','Pending']

                table.add_row((total, completed, in_progress, pending))

                print('\n--- Tasks Summary---')
                print(table)


        except Exception as e:
            print('Error generatingg summary:', e)


        
if(__name__=='__main__'):
    em1 = TaskManage()
    em1.alloactedTask()

    
