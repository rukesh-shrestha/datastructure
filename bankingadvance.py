class Banking:
    """
        This class prototype the basic operation of the bank such as create, deposit, withdrawn and the check balance.
    """

    def __init__(self):
        """
            This is the constructor of the class. It is automaticaly called when the object of the class is created. In this constructor, dictionary is created and two message is printed.
        """
        self.__account = dict()
        print("Welcome to the Hamro Sewa.")
        print("You can create,deposit,withdraw and check your amount from this system. \n")

    def __isnegative(self, amount):
        """
            This is the private function. It cannot be access outside of the class. This function check wheather user enter amount is null or not.
        """
        if amount < 0:
            return True
        else:
            return False

    def __multiple(self, amount):
        """
            This is also the private function. It cannot be access outside of the class. This function check wheather the user enter amount is multiple of 5 or not.
        """
        if amount % 5 == 0:
            return True
        else:
            return False

    def createaccount(self, name, amount=0):
        """
            This function is used to create the bank account and also check if the enter amount is negative or not. If negative it shows the error. 
        """
        if self.__isnegative(amount) == False:
            if name not in self.__account:
                self.__account[name] = amount
                return 'Hello,{} you have successfuly created account with {} balance.'.format(name.capitalize(), amount)
            else:
                raise RuntimeError("Account Already Exist.")
        elif self.__isnegative(amount) == True:
            raise RuntimeError("Fund Invalid. Negative Fund.")

    def deposit(self, name, amount):
        """
            This function is used to deposit the amount to the bank it also check if the amount is negative or not.
        """
        if self.__isnegative(amount) == False:
            if name in self.__account:
                val = self.__account[name]
                update = val + amount
                self.__account[name] = update
                return '{}, you have successfully deposit {} in your account.'.format(name.capitalize(), amount)
            else:
                return RuntimeError(
                    "Opps!...Please create the account First."
                )

        elif self.__isnegative(amount) == True:
            raise RuntimeError("Fund Invalid. Negative Fund.")

    def withdrawn(self, name, amount):
        """
            This function is used to withdrawn the amount from the concern particular account. If account is not found it shows an error. 
        """

        if self.__multiple(amount) == True:

            if self.__isnegative(amount) == False:
                if name in self.__account:
                    if self.__account[name] > amount:
                        val = self.__account[name]
                        update = val - amount
                        self.__account[name] = update
                        return '{}, you have successfully withdrawn {} from your account.'.format(name.capitalize(), amount)
                    else:
                        return RuntimeError("Yout donot have sufficient balance.")
                else:
                    return 'Opps! .... You donot have account. Please create the account first.'
            elif self.__isnegative(amount) == True:
                return RuntimeError("Fund Invalid. Negative Fund.")

        elif self.__multiple(amount) == False:
            return RuntimeError("Fund Invalid. It should be in multiple of five and should not be negative Fund.")

    def checkbalance(self, name):
        """
            This function is used to check the balance of the account. 
        """
        if name in self.__account:
            return '{}, your total balance is {}.'.format(name.capitalize(), self.__account[name])
        else:
            return 'There is no account with the name, {}.'.format(name.capitalize())


if __name__ == '__main__':
    """
        Below code will run if the class name is equal to main. If we import this class to another python file below code will not run.
    """
    condition = True
    Bank = Banking()

    while condition:

        print("\n")
        print("Do you want to create the account with this banking system? Type yes if you want to agree or type quit to quit the program.")
        print("To deposit the amount in your account type deposit.")
        print("To withdrawn the amount from your account type withdrawn.")
        print("To check your balance in your account type check")
        print("\n")

        choice = input("Enter your choice.\n")

        if choice.lower() == 'yes':
            name = input("Please enter your name.\n")
            print("\nDo you want to open your bank account with zero balance or with certian amount. If you want to open the account with zero balance type numeric 0 or type the amount. \n")
            amount = int(input("Please enter your amount. \n"))
            print(Bank.createaccount(name, amount))

        elif choice.lower() == 'deposit':
            name = input("Please enter your name.\n")
            amount = int(input("Please enter the amount\n"))
            print(Bank.deposit(name, amount))

        elif choice.lower() == 'withdrawn':
            name = input("Please enter your name.\n")
            amount = int(input("Please enter the amount\n"))
            print(Bank.withdrawn(name, amount))

        elif choice.lower() == 'check':
            name = input("Please enter your name.\n")

            print(Bank.checkbalance(name))

        elif choice.lower() == 'quit':
            condition = False

        else:
            raise RuntimeError("Invalid choice.")
