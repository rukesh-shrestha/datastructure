
class Banking:
    """
        This class prototype the basic operation of the bank such as deposit, withdrawn and the check balance.
    """

    def __init__(self):
        """
            This is the constructor is the class. It is automaticaly called when the object of the class is created. In this constructor, two list is created and two message is printed.
        """
        self.balance = list()
        self.finalbalance = list()
        print("Welcome to the Hamro Sewa.")
        print("You can deposit,withdraw and check your amount from this system. \n")

    def __isemtpy(self):
        """
            This is the private function. It cannot be access outside of the class. This function check wheather the balance is null or not.
        """
        if len(self.balance) == 0:
            return True
        else:
            return False

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

    def deposit(self, amount):
        """
            This function is used to deposit the amount. It also checks wheather the user enter amount is valid or not. If not valid it throws the error otherwise it shows the deposit amount value.
        """
        if self.__isnegative(amount) == False:
            if self.__isemtpy() == True:
                self.balance.append(amount)
                self.finalbalance.append(sum(self.balance))

                return 'You have successfully deposit amount {},Now your total balance is {}.'.format(amount, *self.finalbalance)
            elif self.__isemtpy() == False:
                val = self.finalbalance[0]
                self.finalbalance.clear()
                self.finalbalance.append(val+amount)
                return 'You have successfully deposit amount {},Now your total balance is {}.'.format(amount, *self.finalbalance)

            else:
                raise RuntimeError("Cannot Deposit the Fund.")
        elif self.__isnegative(amount) == True:
            raise RuntimeError("There is no such cash.")

    def withdrawn(self, amount):
        """
            This function is used to withdrawn the amount. First, this function check if the amount is valid or not. If the amount is not valid it throws the error otherwise it deposit the amount. 
        """
        if self.__multiple(amount) == True and self.__isnegative(amount) == False:

            if self.__isemtpy() == True:
                return RuntimeError("The Bank balance is empty. Please deposit your amount then try to withdrawn it.")
            else:
                val = self.finalbalance[0]
                self.finalbalance.clear()
                self.finalbalance.append(val-amount)
                if self.__isnegative(*self.finalbalance) == False:
                    return 'You have successfully withdrawn {}. Now your total balance is {}'.format(amount, *self.finalbalance)
                elif self.__isnegative(*self.finalbalance) == True:
                    return RuntimeError("You donot have sufficient amount in your balance please deposit the fund then try to withdrawn it.")
        else:
            return RuntimeError("The withdrawn amount should be multiple of five and it should not be negative.")

    @property
    def checkbalance(self):
        """
            This function display the total balance. 
        """
        try:
            return 'Your total balance is, {}'.format(*self.finalbalance)
        except:
            return 'Your total balance is, 0'


if __name__ == '__main__':
    """
        Below code will run if the class name is equal to main. If we import this class to another python file below code will not run.
    """
    b = Banking()
    print(b.deposit(699))

    print(b.withdrawn(-510))
    print(b.checkbalance)

    # b.withdrawn()
