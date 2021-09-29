import random  # importing the random library


class Game:
    """
        This class is the sample game of scissor, paper and rock.
    """
    __val = None
    __game = ('scissor', 'paper', 'rock',)

    def __init__(self):
        """
            It is the contructor of the class. It is call automatically when the new object is created. It simple print the welcome message and operation to perform guide. and it also include the simple logic to play the game or quit the game. If the input value is not as per the guide it will trow the runtimeerror.
        """
        print("Welcome to the Game")
        print("  Do you want to play Scissor, Paper and Rock.")
        print("  If Yes, Please enter Yes otherwise you can enter No.")
        val = input("Please enter your choise: \n")
        v = val.lower().strip()

        if v == 'yes':
            print('Welcome to the game. Below you can find the rules of the game.')
            print('Rock wins against scissors.')
            print('Scissors win against paper.')
            print('Paper wins against rock.')
            print('\n')
        elif v == 'no':
            quit()
        else:
            raise RuntimeError(
                "The enter value is not as the above mention guide.")

    def __random(self):
        """
            This function find the random value from the tuple and assign the value to the private variable.
        """
        value = random.choice(self.__game).lower().strip()
        self.__val = value

    def __check(self, user):
        """
            This function check if the user input variable is in the game guide or not.
        """
        if user in self.__game:
            return True
        else:
            return False

    def play(self, name, user):
        """
            This is the main function to play the game. This function check the basic rules of the game as well as throw runtime error is the game is not as per the rules.
        """
        self.__random()

        print('user input', user)
        print('system generated', self.__val)

        if self.__check(user) == True:

            if user == self.__val:
                return 'Draw, Please try again. {}, and system has choose the  same choice {}.'.format(name, self.__val)

            elif user == 'rock' and self.__val == 'scissor':
                return 'Congratulation {}, you win.'.format(name)

            elif user == 'scissor' and self.__val == 'paper':
                return 'Congratulation {}, you win.'.format(name)

            elif user == 'paper' and self.__val == 'rock':
                return 'Congratulation {}, you win.'.format(name)

            else:

                return 'Oops. Try again, system wins. {}, beat the {}'.format(self.__val, user)

        else:
            raise RuntimeError("Please enter the value as per the game guide.")


if __name__ == '__main__':
    """
        Below code run if the class name is equal to main. If we import this class to another python file below code will not run.
    """
    g = Game()
    name = input("Please enter your name: \n")
    user = input(
        "Please enter your choise between scissor, paper and rock. \n")
    val = user.lower().strip()

    print(g.play(name, val))
import random  # importing the random library


class Game:
    """
        This class is the sample game of scissor, paper and rock.
    """
    __val = None
    __game = ('scissor', 'paper', 'rock',)

    def __init__(self):
        """
            It is the contructor of the class. It is call automatically when the new object is created. It simple print the welcome message and operation to perform guide. and it also include the simple logic to play the game or quit the game. If the input value is not as per the guide it will trow the runtimeerror.
        """
        print("Welcome to the Game")
        print("  Do you want to play Scissor, Paper and Rock.")
        print("  If Yes, Please enter Yes otherwise you can enter No.")
        val = input("Please enter your choise: \n")
        v = val.lower().strip()

        if v == 'yes':
            print('Welcome to the game. Below you can find the rules of the game.')
            print('Rock wins against scissors.')
            print('Scissors win against paper.')
            print('Paper wins against rock.')
            print('\n')
        elif v == 'no':
            quit()
        else:
            raise RuntimeError(
                "The enter value is not as the above mention guide.")

    def __random(self):
        """
            This function find the random value from the tuple and assign the value to the private variable.
        """
        value = random.choice(self.__game).lower().strip()
        self.__val = value

    def __check(self, user):
        """
            This function check if the user input variable is in the game guide or not.
        """
        if user in self.__game:
            return True
        else:
            return False

    def play(self, name, user):
        """
            This is the main function to play the game. This function check the basic rules of the game as well as throw runtime error is the game is not as per the rules.
        """
        self.__random()

        print('user input', user)
        print('system generated', self.__val)

        if self.__check(user) == True:

            if user == self.__val:
                return 'Draw, Please try again. {}, and system has choose the  same choice {}.'.format(name, self.__val)

            elif user == 'rock' and self.__val == 'scissor':
                return 'Congratulation {}, you win.'.format(name)

            elif user == 'scissor' and self.__val == 'paper':
                return 'Congratulation {}, you win.'.format(name)

            elif user == 'paper' and self.__val == 'rock':
                return 'Congratulation {}, you win.'.format(name)

            else:

                return 'Oops. Try again, system wins. {}, beat the {}'.format(self.__val, user)

        else:
            raise RuntimeError("Please enter the value as per the game guide.")


if __name__ == '__main__':
    """
        Below code run if the class name is equal to main. If we import this class to another python file below code will not run.
    """
    g = Game()
    name = input("Please enter your name: \n")
    user = input(
        "Please enter your choise between scissor, paper and rock. \n")
    val = user.lower().strip()

    print(g.play(name, val))
