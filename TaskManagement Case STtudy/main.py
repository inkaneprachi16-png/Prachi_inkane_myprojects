from admin import Admin
from user import  User

ch = 0
while(ch != '3'):
    print('''Please select choice:
    1. Admin
    2. user(Employee)
    3.Exit''')
    ch = input('Enter choice:')
    try:
        if(ch == '1'):
            uname = input('enter user name:')
            passw = input('enter password:')
            if(uname == 'admin' and passw == '1234'):
                print('loged in successful...')
                Admin()
            else:
                print('Invalid credentials...')
            
        elif(ch=='2'):
            uname = input('enter user name:')
            passw = input('enter password:')

            logged_in = False

            with open('DEMOS/taskManagement Case STtudy/users.txt', 'r') as fp:
                for line in fp:
                    line  = line.strip()
                    if not line:
                        continue
                    parts = [x.strip() for x in line.split(',')]
                    if len(parts) != 3:
                        print(f'skipping malformed line:{line}')
                        continue

                    u,p,role =parts
                    if uname == u and passw == p and role == 'user':
                        confirm_username = input("Enter your username again to confirm: ")

                        if confirm_username != uname:
                            print('Invalid username , Please try again.')
                            logged_in = True
                            break
                        else:
                            print('Username confirmed succcessfully...')
                            print('Logged in successfully...')

                            User(uname)
                            logged_in = True
                            break
                        
            if not logged_in:
                print('Invalid credentials...')


        elif(ch=='3'):
            print('Thanks for choosing us!')

        else:
            print('Invalid choice...')

    except Exception as e:
        print('error:', e)       