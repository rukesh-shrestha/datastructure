class Factorial:
    """
        This class is used to find the factorial of the given number.
    """
    def __init__(self):
        """
            This is the constructor of the class. It is called auttomatically when the object is created. It just print the single line information.
        """
        print("Hello there, Here you can know the factorial of any number.")

    def factorial(self, value):
        """
            This function is used to calculate the factorial of the given number.        
        """
        mul = 1
        for x in range(1, value + 1):
            mul = x * mul
        return 'The factorial of {} is {}.'.format(value, mul)


if __name__ == '__main__':
    """
        Below code will run if only this class is run saperately. It also check if the input number is numeric or string. 
    """
    fact = Factorial()
    condition = True
    while condition:
        user = input(
            "Please enter the number to know their factorial or type anything to end the program. \n")

        if user.isnumeric():
            user = int(user)
            print(fact.factorial(user))

        elif isinstance(user, str):
            condition = False
