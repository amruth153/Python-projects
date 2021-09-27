#Name: Amruth Kanakaraj
#Student ID: 201547293

import random
import datetime
expdate=[]



#----------------------------------------------------------------
#                     Basic Account Settings
#----------------------------------------------------------------




class BasicAccount:
    def __init__(self, theaccountNumber,theName,theBalance,theCardNum,theCardExp):
        #Initialization of the attributes of class.
        self.acNum=theaccountNumber
        self.name=theName
        self.balance=theBalance
        self.cardNum=theCardNum
        self.cardExp=theCardExp
    def __str__(self):
        #printing the attribute of class instance
        return " The Account bearing the number :{self.acNum} is associated to {self.name} and has a balance of:  {self.balance}.\n with a Card Number :{self.cardNum} \n Card exp: {self.cardExp}".format(self=self)

    def getBalance(self):
        #To return customer balance.
        return self.balance

    def getAvailableBalance(self):
        #to return customer present balance.
        return self.balance

    def setBalance(self,amount):
        self.balance=amount

    def setAvailableBalance(self,amount):
        #stores available balance to amount.
        self.balance=amount

    def deposit(self,amount):
        #stores balance to already available balance and amount passed
        print("Deposit of £" ,amount, "received.")
        self.balance+=amount

    def withdraw(self,amount):

        if amount>self.getAvailableBalance():
            print("Withdrawal of £", amount, "is denied. Insufficient balance.")
        else:

            self.setBalance(self.getBalance()-amount)
            print(self.name ,"has withdrawn £",amount, ". Revised available balance is £" ,self.getBalance())

    def getName(self):
        return self.name

    def getAcnum(self):
        return self.acNum

    def closeAccount(self):
        
        self.withdraw(self.balance)
        print("Your Account has been sucessfully closed.")

    def issueNewCard(self):
        #A card number with random 16 numbers
        self.cardNum=random.randint(1000000000000000,9999999999999999)

        #Expiry date of card is set to 3 years from date of issue.
        today=datetime.datetime.now()
        expdate.append(today.month)
        expdate.append(str(today.year+3)[-2:])
        self.cardExp=tuple(expdate)
        



#----------------------------------------------------------------
#                     Premium Account Settings
#----------------------------------------------------------------


class PremiumAccount(BasicAccount):
    def __init__(self, theaccountNumber,theName,theBalance,thecardnum,thecardExp,theoverDraft,theoverDraftLimit ):
        #Initialization of the attributes of class using functions.
        super().__init__(theaccountNumber,theName,theBalance,thecardnum,thecardExp)
        self.overDraft=theoverDraft
        self.overDraftLimit=theoverDraftLimit

    def __str__(self):
        #Functions to print the attributes of class
        if self.overDraft ==True:

            return "Premium Account number :{self.acNum} associated to {self.name} has a balance of £:  {self.balance} .\n Your overDraftLimit: {self.overDraftLimit} ".format(self=self)
        else:
            return "Account number :{self.acNum} associated to {self.name} has an balance of £:  {self.balance}".format(self=self)

    def setOverdraftLimit(self, odLimit):
        self.overDraftLimit=odLimit

    def getAvailableBalance(self):
        #For a premium account the Overdraft feature is enabled then available balance = balance + od limit
        if self.overDraft==True:
            return self.balance+self.overDraftLimit
        else:
            return self.balance

    def getBalance(self):
        #returns customer balance
        return self.balance

    def setBalance(self,amount):
        self.balance=amount


    def closeAccount(self):

        if (self.balance<0):
            print("Cannot close account due to customer being overdrawn by £", self.balance)
        else:
            self.withdraw(self.balance)
            print("The account can be closed now")

def main():
    # We assume that kyle already has bank account with the bank which was already created.
    acc1 = BasicAccount('3687', 'Kyle',100, 5355220596098404,(1,24))
    print(acc1,"\n")
    
    acc1.withdraw(100)

    acc1.deposit(800)

    acc1.issueNewCard()
    print(acc1,"\n")

    acc1.withdraw(2000)

    acc2 = PremiumAccount('8879','Lee',360, random.randint(1000000000000000,9999999999999999) ,1/24,True,1500.00)
    
    print(acc2,"\n")
    

    acc2.withdraw(1500)
    print(acc2,"\n")

    acc2.deposit(200)
    print(acc2,"\n")

    acc2.closeAccount()


##calling main function
main()
