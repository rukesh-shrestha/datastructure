class Guess:
    __value = None
    __guessword = ['China']
    __val = list()
    __dincval = None
    __key = list()
    __up = list()
    __value = None
    __point = 10
        

    
    def __init__(self):
        __file = 'country.txt'
        print("Welcome to the Guesing the word game. \n")
        print("Are you excited to play the game? \n If you want to play the game please type Yes or you can type NO.\n")
        self.__value = input("Please enter your choice \n").lower().strip('')
        self.__quit()
        
        
        

    def __quit(self):
        if self.__value == 'yes':
            return False
        elif self.__value == 'no':
            print("The program has been terminated.")
            quit()
        else:
            raise ValueError("You have not enter as per the guide line.")

    def guidelines(self,path=None):
        with open("rules.txt",'r') as file:
            data = [x for x in file.readlines()]
            for x in data:
                print(x)
            

        

    def guessword(self,word):
        if self.__quit() == False:
            self.__guessword.append(word)


    def guess_hint(self,*hint):            
        if self.__quit() == False:
            for x in hint:                
                for j in x:
                    if j.isnumeric():
                        self.__key.append(j)
                    else:
                        self.__up.append(j)
        self.__val.extend("".join(self.__up).split("."))      
        self.__dincval = [x.strip() for x in self.__val if len(x) > 4]
        self.__value = zip(self.__key,self.__dincval)


    def display(self):            
        for x in self.__value:
            print(*x,".")

    def check(self,value):
        if value in self.__guessword:
            print("Hip Hip Hurray! You have win the game.")
        elif self.__point == 0:
            print("Better luck next time.")
            quit()
        else:
            self.__point -=1

        

        
        

    



       


            
    


        



if __name__=='__main__':
    g = Guess()
    # g.guidelines()
    # g.guessword(input("Please enter the word\n"))
    # print("\n\n")
    # print("===================================================")
    # print("Guide to Type the hint for the game.")
    # print("---------------------------------------------------")
    # print("You have to type the hint followed by number and the hint. \n You do not need to hit enter after the sentence is complete.")
    # print("---------------------------------------------------")
    # print("For eg: 1. It is one of the country name of Asia. 2. It has the unique flag.")
    # print("===================================================")
    # g.guess_hint(input("Please enter the hints.\n"))
    # g.display()
   
    g.check('India')
    g.check('India')
    g.check('India')
    g.check('India')
    g.check('India')
    g.check('India')
    g.check('India')
    g.check('India')
    g.check('India')
    g.check('India')
    g.check('India')
    