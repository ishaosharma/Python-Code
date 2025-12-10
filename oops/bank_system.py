class Bank:
    # set_balance = 30000
    def __init__(self,user_name, pan, address, set_balance):
            self.user_name = user_name
            self.pan = pan
            self.address = address
            self.set_balance = set_balance

    def deposit(self, amount):
         print("*******Deposit method called******")
         print("Initial balance of account = ",self.set_balance)
         print("Amount to deposit in bank is = ", amount)
         self.set_balance += amount
         print("After depositing some amount = ", self.set_balance)

    def withdrawal(self, amount):
         print("*******withdrawal method called******")
         print("Initial balance of your account = ",self.set_balance)
         print("Amount to withdraw from bank is = ", amount)
         if(amount < self.set_balance):
             self.set_balance -= amount
         else:
             print("OOPSIE!!!!Insufficient balance!!!!!!")
         print(f"After withdrawing {amount},now amount left = ", self.set_balance)
    
    def ministatement(self):
          print("*******MINISTATEMENT******")
          print("Account holder name is : ", self.user_name)
          print("PAN ID of USER1 is : ", self.pan)
          print(f"Account balance of {self.user_name} is : ", self.set_balance)
          print("Address of user1 is : ",self.address)


user1 = Bank("Shree", 237890, "kvnagar", 30000) # Create user account first
print("Welcome to HDFC BANK! We are ready to serve you!")
while True:
    print("Press '1' for amount deposit")
    print("Press '2' for amount withdraw")
    print("Press '3' to view Bank statement")
    print("Press '4' for Logging Out from process")
    choice = int(input("Enter your choice : "))
    
    match choice:
         case 1:
            amount = int(input("Enter amount for deposit : "))
            user1.deposit(amount)
      
         case 2:
            withdraw_amount = int(input("Enter withdraw amount: "))
            user1.withdrawal(withdraw_amount)
         
         case 3:
          user1.ministatement()

         case 4:
          print("Thanks for being with HDFC. We are happy to serve you")
          break  # Now 'break' will exit the loop
         case _: 
          print("Invalid choice")

            