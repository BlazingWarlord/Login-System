import mysql.connector as con
conobj = con.connect(host = 'localhost',username='root',password = '',database = 'Login')
cursorobject = conobj.cursor()

print("MENU: \n\nPress 1 for Register\n\nPress 2 for login\n\n")

userinput = int(input("Enter your choice: "))

if userinput == 1:

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursorobject.execute(f"SELECT * FROM credentials where Username = '{username}'")
    data = cursorobject.fetchall()

    if len(data) > 0:
        for x in data:
            if username == x[0]:
                print("Username exists")
                break
        else:
            cursorobject.execute(f'INSERT INTO credentials VALUES("{username}","{password}")')
            conobj.commit()
    else:
        cursorobject.execute(f'INSERT INTO credentials VALUES("{username}","{password}")')
        conobj.commit()

elif userinput == 2:
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursorobject.execute(f"SELECT * FROM credentials where Username = '{username}'")
    data = cursorobject.fetchall()

    if len(data) > 0:
        for x in data:
            if username == x[0]:
                if password == x[1]:
                    print("Login Successful... Welcome !")
                    break
                else:
                    print("Login Failed, Try Again or Register.")
                    break
        else:
            print("Login Failed, Try Again or Register.")
    else:
        print("Login Failed, Try Again or Register.")
            
        
