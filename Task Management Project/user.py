from taskManagement import TaskManage

class User:
    def __init__(self, username):
          self.username = username
          tm = TaskManage()

          ch = 0
          while(ch!='4'):
               print('''Please select options
               1.View My Task
               2.Update Task Status
               3. Task summary
               4. logout''')
               ch= input('Enter choice:')
               if (ch == '1'):
                    tm.myTasks(self.username)
               elif (ch == '2'):
                    tm.updateTaskStatus(self.username)
               elif (ch == '3'):
                    tm.taskSummary(self.username)
               elif(ch == '4'):
                    print('Logged out')
               else:
                    print('Invalid choice...')     
                
            
