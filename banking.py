import mysql.connector as m
md = m.connect(host='localhost',user='root',passwd='root',database='bankingsystem')
if md.is_connected():
    print('You can now access your banking procedures')
mc = md.cursor()
try:
    mc.execute("create table bankacc(name varchar(20),bal int,lasdeponum int,laswithnum int)")
except:
    pass
def mainmenu():
    print("\n")
    print('1. Create a new account\n2. Withdraw\n3. Balance\n4. Deposit\n5. Show all accounts\n6. Last transaction\n7. Exit')
    print("\n")
    choice = int(input('Enter your choice: '))
    if choice == 1:
        print('\n')
        newacc()
    elif choice == 2:
        print('\n')
        withdraw()
    elif choice == 3:
        print('\n')
        bal()
    elif choice == 4:
        print('\n')
        deposit()
    elif choice == 5:
        print('\n')
        showacc()
    elif choice == 6:
        lastrans()
    elif choice == 7:
        print("Thank you for using our services")
        md.close()
        exit()
    else:
        print('Invalid choice')
        mainmenu()
def wannacont():
    ans = input('\nDo you want to continue? (y/n): ')
    if ans == 'y':
        mainmenu()
    elif ans == 'n':
        print("Thank you for using our services")
        md.close()
        exit()
def showacc():
    mc.execute('select name from bankacc')
    for i in mc.fetchall():
        for j in i:
            print(j)
    wannacont()
def newacc():
    name = input('Enter your name: ')
    bal = int(input('Enter your account balance: '))
    mc.execute('insert into bankacc values(%s,%s,%s,%s)',(name,bal,0,0))
    print('Your account has been created successfully')
    md.commit()
    wannacont()
def deposit():
    natoac = input("Enter your account name with correct spelling to proceed: ")
    amtodep = int(input("Enter the amount to deposit: "))
    mc.execute('update bankacc set lasdeponum = %s where name = %s',(amtodep,natoac))
    mc.execute('update bankacc set bal = bal + %s where name = %s',(amtodep,natoac))
    md.commit()
    wannacont()
def withdraw():
    natoac = input("Enter your account name with correct spelling to proceed: ")
    amtowit = int(input("Enter the amount to withdraw: "))
    mc.execute('update bankacc set laswithnum = %s where name = %s',(amtowit,natoac))
    mc.execute('update bankacc set bal = bal - %s where name = %s',(amtowit,natoac))
    md.commit()
    wannacont()
def bal():
    name = input("Enter your account name with correct spelling to proceed: ")
    mc.execute('select name,bal from bankacc where name = %s',(name,))
    for i in mc.fetchall():
        print(f"Name: {i[0]}\nBalance: {i[1]}")
        print('\n')
    wannacont()
def lastrans():
    name = input("Enter your account name with correct spelling to proceed: ")
    mc.execute('select name,lasdeponum,laswithnum from bankacc where name = %s',(name,))
    for i in mc.fetchall():
        print(f"Name: {i[0]}\nLast deposit: {i[1]}\nLast withdraw: {i[2]}")
        print('\n')
    wannacont()
mainmenu()
md.commit()