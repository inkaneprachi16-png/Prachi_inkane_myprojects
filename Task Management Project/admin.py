from taskManagement import TaskManage

class Admin:
    def __init__(self):
        tm = TaskManage()
        ch = 0
        while(ch!='5'):
            print('''Please select option
            1.Onboard Employee
            2.Allocate Task
            3. Track Task
            4. View Report
            5. logout''')
            ch = input('Enter choice:')
            if(ch == '1'):
                tm.addEmp()
            elif(ch == '2'):
                tm.alloactedTask()
            elif(ch=='3'):
                tm.trackTasks()
            elif(ch== '4'):
                tm.report()
            elif(ch == '5'):
                print('Logged out')
            else:
                print('Invalid choice...')     
                
                  

                
