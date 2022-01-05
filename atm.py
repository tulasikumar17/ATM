
l={100:0,200:0,500:0,2000:0}
ul={"user1":{"password":1111,"userbal":5000,"c1":0},
    "user2":{"password":2222,"userbal":5000,"c1":0}}
t=0;c=0
def admin():
    global t
    b=input("Enter user name: ")
    c=input("Enter pin: ")
    if b=="admin" and c=='1234':
        print("\tAdmin succesfully logged")
        while True:
            print("1.Load\n2.check\n3.exit")
            d=input("Enter choice: ")
            if d=="1":
                for i in l:
                    print("Number of",i,"notes: ")
                    e=int(input())
                    l[i]+=e
                    t=t+e*i
                input("\tloaded succesfully")
            elif d=="2":
                for i in l:
                    print(i,"-->",l[i])
                print("total amount",t)
                input("\tpress enter to continue")
            elif d=="3":
                break
            else:
                print("Invalid input")
def user():
    global ul,t
    e1=input("Enter username: ")
    while ul[e1]["c1"]<3:
        f=int(input("Enter password: "))
        if ul[e1]["password"]==f:
            print("succesfully logged In")
            while True:
                m={2000:0,500:0,200:0,100:0}
                print("1.Deposit\n2.Withdraw\n3.Balance enquiry\n4.pin change\n5.EXIT")
                print("Enter choice: ")
                g=int(input())
                if g==1:
                    print("Enter deposit amount: ")
                    amt=int(input())
                    if amt%100==0:
                        s=amt
                        cn=0
                        for i in m:
                            m[i]=s//i
                            s=s%i
                            l[i]+=m[i]
                        ul[e1]["userbal"]+=amt
                        t=t+amt
                        print("Succesfully added amount")
                        input("\tpress enter to continue")
                    else:
                        print("invalid amount")
                elif g==2:
                    print("Enter withdraw amount: ")
                    wdamt=int(input())
                    if wdamt%100==0:
                        if wdamt<=t:
                            if wdamt<=ul[e1]["userbal"]:
                                s=wdamt
                                cn=0
                                for i in m:
                                    m[i]=s//i
                                    s=s%i
                                for i in l:
                                    if l[i]>=m[i]:
                                        #l[i]=l[i]-m[i]
                                        cn+=1
                                if cn==4:
                                    ul[e1]["userbal"]-=wdamt
                                    t=t-wdamt
                                    for i in l:
                                        l[i]=l[i]-m[i]
                                    print("amount withdrawal succesful")
                                    input("\tpress enter to continue")
                                else:
                                    print("Invalid cash")
                                    print("Enter amount in",l)
                                    input("press Enter to continue")
                            else:
                                print("insuficient funds in your account")
                                input("\tpress enter to continue")
                        else:
                            print("insuficient balance in ATM")
                            input("\tpress enter to continue")
                    else:
                        print("Invalid amount")
                        input("\tpress enter to continue")
                elif g==3:
                    print("Your account balance is",ul[e1]["userbal"])
                    input("\tpress enter to continue")
                elif g==4:
                    print("Enter your old password :")
                    oldpass=int(input())
                    if oldpass==ul[e1]["password"]:
                        print("Enter new password: ")
                        newpass=int(input())
                        ul[e1]["password"]=newpass
                        print("\tSuccesfully updated password")
                        input("Press Enter to continue")
                        return
                    else:
                        print("your old password is in correct")
                        input("\tpress Enter to continue")
                elif g>5:
                    print("Invalid input")
                    input("\tpress enter to continue")
                else:
                    return
        else:
            ul[e1]["c1"]+=1
            print("wrong pin")
    else:
        print("\tyour account is temporarly blocked")
while True:
    print("WELCOME TO ATM")
    print("1.admin\n2.user\n3.EXIT")
    a=int(input("Enter your choice: "))
    if a==1:
        admin()
    elif a==2:
        user()
    elif a==3:
        break
    else:
        print("invalid input")