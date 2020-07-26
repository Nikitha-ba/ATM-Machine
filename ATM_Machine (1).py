import pandas as pd
url = 'https://raw.githubusercontent.com/Nikitha-ba/ATM-Machine/master/DS.csv'
#df = pd.read_csv("DS.csv")
df = pd.read_csv(url,error_bad_lines=False)
print (df)
p = df.Pin
flag = 0
print("Welcome to ATM")
print("WElcome to bankworld")
print("Swipe your valid card here:")
count = 0
chance = 2

while count<3:
    
    pin=int(input("enter your pin to proceed : "))
    for i in range(len(p)):
        if pin == p.iloc[i]:
            print("Welcome "+df.iloc[i]['CardHolder'])
            print("Card Type: "+df.iloc[i]['card'])
            flag = 1
            break
    if flag == 1:
        break
    else:
        print("Wrong PIN..! Chances: ",chance)
        chance = chance - 1
        count = count + 1

df = pd.read_csv(url,error_bad_lines=False)
#df = pd.read_csv("DS.csv")
quit1 = "N"
while quit1 != "Y":
    if count<3:
        print("choose your transaction:")
        print("1. Balance Enquiry")
        print("2. Withdrawl Money")
        print("3. Deposit")
        print("4. Change your PIN")
        print("5. Transfer Money")
        print("6. Quit")
        trans=int(input("transaction:"))
        if trans == 1:
            print("Balance : " , df.iloc[i]['Amount'])
            slip = input("Do you want Slip? Enter Y for yes ")
            if slip == "Y":
                print("Here is your Slip! Thanks for using Bankworld")
                quit1 = "Y"
            else:
                print("Thanks for using Bankworld")
                quit1 = "Y"
        elif trans == 2:
            amount = int(input("Enter your amount to proceed:"))
            if amount < (df.iloc[i]['Amount']):
                print("Collect your cash!")
                df.loc[i,'Amount'] = df.loc[i,'Amount']-amount
                df.to_csv("DS.csv")
                quit1 = "Y"
            else:
                print("No sufficient balance")
        elif trans == 3:
            deposit=int(input("Enter your amount to be deposited"))
            if deposit>0:
                print("Your amount has been successfully deposited to your account")
                print("Thanks for using bankworld")
                amt = df.iloc[i]['Amount'] + deposit
                df.loc[i,'Amount'] = amt
                df.to_csv("DS.csv")
                quit1 = "Y"
            else:
                print("Enter valid amount to proceed")
        elif trans == 4:
            change_pin = input("Enter new PIN here : ");
            length = len(change_pin) 
            if length == 4:
                print("Your PIN has been successfully changed..! ")
                print("Thanks for using Bankworld")
                print("New PIN: "+change_pin)
                df.loc[i,'Pin'] = change_pin
                df.to_csv("DS.csv")
                quit1 = "Y"
            else:
                print("Enter valid PIN to proceed.")

        elif trans == 5:
            transfer_money = int(input("Enter your amount to transfer:"))
            if transfer_money < df.iloc[i]['Amount'] :
                AC = input("Enter Account No.: ")
                print("Your money has been transfered..!")
                print("To Account : ",AC)
                tr = df.iloc[i]['Amount'] - transfer_money
                df.loc[i,'Amount'] = tr
                df.to_csv("DS.csv")
                print("Thaks for using Bankworld")
                quit1 = "Y"
            else:
                print("Enter valid amount to proceed")

        elif trans == 6:
            quit1 = input("Press wnter Y to quit...!")
            if quit1 == "Y":
                print("Quit")
            else:
                print("Choose any transaction please:")
