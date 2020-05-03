'''Example will be the ATM machine
As we know ATM machine performs multiple operations and those are:
1.Account Information
2.PIN Change
3.Balance Inquiry
4.Withdrawal
5. Deposit
Now, What you need to do, You need to create a class of ATM and methods/functions is nothing but your operations that means your code will have 5 methods
One More important note, as you know if you enter wrong pin for three time it get block , that means you need to write a program in this way if I give wrong pin three times, Your account should get blocked. If you have any doubts, drop a comment or just text me on whats-app.
Do the same post your link in comment section

Now, How you will store data/Account information
store it in terms of dictionary or file as per your convenience.
1.If You are using dictionary:
key will be your name
value will be your - Acc. No, Mobile No., PIN
e.g. D={"ABC":5212485411,123454562,4545, "DEF":4559845253,1234567895,8989}

2.If you are using files include following:
Name:
Account No.
Mobile NO.
Address:
PIN'''

#CODE

class Atm:

def init (self,name,acc_no,mobileno,pin): 
    self.acc_no=acc_no
    self.pin=pin
    self.balance= randint(0,10000) 
    self.name=name 
    self.mobileno=mobileno


def pin_authentication(self): 
    userpin= int(input("EnterPIN:"))
    count=1 
    flag=0
    while(userpin != self.pin): 
        print("PIN INCORRECT")
        userpin=int(input("EnterPIN:")) count=count+1
        if(count==3 and userpin!=self.pin): 
            print("ACCOUNTBLOCKED")
            flag=1 
            break 
    if flag == 0:
        print("User Authenticated") return

    flag


def account_info(self):

    print(f"Name: {self.name}\nAccount Number: {self.acc_no}\nMobile no.:
    {self.mobileno}\nBalance(in Rs): {self.balance}\nPIN:{self.pin}")


def pin_change(self): 
    print("Old Pin details")
    new_pin=self.pin confirm_new_pin=0
    temp=self.pin_authentication() 
    if (temp==0):
        while(new_pin != confirm_new_pin): 
            while True:
                try:

                new_pin=int(input("Enter new 4-digit pin: ")) except:
                print("INVALID INPUT")

                continue else:

                break 
        while True:
            try:

            confirm_new_pin=int(input("Re-enter new 4-digit pin: ")) 
            except: print("INVALID INPUT")
            continue else:

            break

    if(new_pin == confirm_new_pin): dataframe[self.name][2]= str(new_pin):
        print("PIN successfully changed!")
    
    break else:
        print("PIN DID NOTMATCH!")

    return temp,new_pin


defbalance_inquiry(self):

    print(f"Your Account balance is Rs {self.balance}")


def withdrawal(self): 
    while True:
        try:

            w_amount=int(input("EntertheamounttobewithdrawninRs:")) 
        except:
            print("INVALID INPUT")
            continue
        else:
            break
            
    if (w_amount > self.balance): 
        print("Funds unavailable! ")
    elif(w_amount<100):
        print("Minimum withdrawal limit is Rs 100\nWithdrawal Denied!") 
    elif (self.balance- w_amount <100):
        print("Minium balance should be Rs.100\nWithdrawal Denied!") 
    else: 
        self.balance=self.balance-w_amount 
        print("Withdrawal Successful\nNew Balance-") 
        self.balance_inquiry()


def deposit(self): 
    while True:
        try:

        d_amount=int(input("EnteramounttobedepositedinRs:")) 
        except: 
            print("INVALID INPUT")
            continue

        else:

            break 
    if(d_amount<100):
        print("MinimumamountfordepositionisRs.100\nDeposition Denied!")
    else:
        self.balance=self.balance+d_amount print("DepositionSuccessful!\nNewBalance-") 
        self.balance_inquiry()
        


def start(Atm): 
    option=0 
    while True:
        try:

            name=input("Enter your name: ").capitalize() except: print("USER NOT FOUND!")
            continue

        else:

            break




obj=Atm(name,dataframe[name][0],dataframe[name][1],dataframe[name][2])

    user=obj.pin_authentication() 
    if user==0:
        op_dict={1:"Account Information",2:"Pin Change",3:"Balance Inquiry",4:"Withdrawal",5:"Cash Deposit",6:"Exit"}
        while(option!=6): 
          for i in op_dict:
              print("{:<2}-{:<15}".format(i,op_dict[i]))
              option=int(input("\nEnter yourchoice:"))
              if(option==1): 
                  obj.account_info() 
              elif(option==2):
                  check,new=obj.pin_change() 
              if(check==1):
                  break dataframe[name][2]=new

obj=Atm(name,dataframe[name][0],dataframe[name][1],dataframe[name][2])

    elif(option==3): 
        obj.balance_inquiry()
    elif(option==4): 
        obj.withdrawal() 
    elif(option==5):
          obj.deposit()
    elif(option==6):
        break

from random import*
 
dataframe = { "Ishika":[32456,7679068432,4444] , "Abhishek":[45673,8654758533,8181],"Sayali":[32478,9890007654,5432],"Ishaan":[89760,7654 328904,1122],"Deepali":[54789,9995674382,5555]}
start(Atm)
          
    
