class Calculator:
    """
        This class is used for the calculating the basic operation such as addition, substraction, multiplication and division.
    """

    def __init__(self):
        """
            It is the contructor of the class. It is call automatically when the new object is created. It simple print the welcome message and operation to perform guide.
        """
        print("Welcome to the simple calculator.")
        print("   Enter Add for the Addition.")
        print("   Enter Sub for the Substraction.")
        print("   Enter Mul for the Multiplication.")
        print("   Enter Div for the Division.")
        print('\n')

    def __isdecimal(self, a, b):
        """
            This is the private function cannot access from outside of the class. It is used to check weather the user input number are floor division or not. 
        """
        if a % b == 0:
            return True
        else:
            return False

    def __isnegative(self, a, b):
        """ 
            This is the private function cannot access from outside of the class. It is used to check weather the user input value 
            after substraction give positive or negative value. 
        """
        val = a-b

        if val > 0:
            return True
        else:
            return False

    def addition(self, a, b):
        """
            This function takes two parameter and return the additional value of those two number.
        """
        val = a+b
        return 'The additional value is: {}'.format(val)

    def multiplication(self, a, b):
        """
            This function takes two parameter and return the multiplication value of those two number.
        """
        val = a*b
        return 'The multiplication value is: {}'.format(val)

    def division(self, a, b):
        """
            This function takes two parameter and return the divison of those value also check if the user input number is floor divisible or not.
        """
        if self.__isdecimal(a, b) == True:
            val = a/b
            return 'The division value is: {}'.format(val)
        else:
            val = a//b
            rem = a % b
            return 'The enter number cannot be exactly divided. Therefore, the quotient is: {} and the remainder is: {}'.format(val, rem)

    def substraction(self, a, b):
        """
            This function takes two parameter and return the substraction of those two number also check if the substracction value is negative or not. If negative, it swap the first numbe from the second.  
        """
        if self.__isnegative(a, b) == True:
            val = a-b
            return 'The substraction value is: {}'.format(val)
        else:
            a, b = b, a
            val = a-b
            return 'The first number is less than the second number. Therefore, we swap the value the result is: {}'.format(val)


if __name__ == '__main__':
    """
        Below code run if the class name is equal to main. If we import this class to another python file below code will not run.
    """
    cal = Calculator()
    user = input("Enter your choice: \n")
    if user == 'mul' or user == 'add' or user == 'sub' or user == 'mul':
        a = int(input("Enter the first number: \n"))
        b = int(input("Enter the second number: \n"))
    value = user.lower()
    if value == 'add':
        print(cal.addition(a, b))
    elif value == 'sub':
        print(cal.substraction(a, b))
    elif value == 'div':
        print(cal.division(a, b))

    elif value == 'mul':
        print(cal.multiplication(a, b))
    else:
        raise RuntimeError(
            'The enter value doesnot match to the above mention value.')
