class Day:
    """
        This class is used to find out your gym day. If you want to take 2 days holiday in a week it will give you two day holiday. 
    """
    def __init__(self):
        """
            This is the constructor is the class. It is automaticaly called when the object of the class is created. In this constructor, one message is printed.
        """
    
        print("Hello there, You can find the day routine of your gym.")
    

    @property
    def sunday(self):
        """
            This is the method of the class. It only return the string value.
        """
        first = 'chest'
        second = 'shoulder'
        return 'Today is your {} and {} day.'.format(first,second)

    @property
    def monday(self):
        """
            This is the method of the class. It only return the string value.
        """
        first = 'bicep'
        second = 'tricep'
        return 'Today is your {} and {} day.'.format(first,second) 

    @property
    def tuesday(self):
        """
            This is the method of the class. It only return the string value.
        """
        first = 'back'
        second = 'leg'
        return 'Today is your {} and {} day.'.format(first,second)

    @property
    def wednesday(self):
        """
            This is the method of the class. It only return the string value.
        """
        first = 'bicep'
        second = 'tricep'
        return 'Today is your {} and {} day.'.format(first,second) 
        
    @property
    def thrusday(self):
        """
            This is the method of the class. It only return the string value.
        """
        first = 'chest'
        second = 'shoulder'
        return 'Today is your {} and {} day.'.format(first,second)

    @property
    def friday(self):
        """
            This is the method of the class. It only return the string value.
        """
        first = 'back'
        second = 'leg'
        return 'Today is your {} and {} day.'.format(first,second)

    @property
    def saturday(self):
        """
            This is the method of the class. It only return the string value.
        """
        return 'Today is your holiday.'



if __name__=='__main__':
    """
        Below code will run if the class name is equal to main. If we import this class to another python file below code will not run. It check some condition and call the methods.
    """
    g = Day()
    condition = True
    day = int(input("How many days you want holiday? \n"))
    

    while condition:

        if day <  0 : 
            raise RuntimeError("Holiday cannot be negative.")
        
            
        elif day > 0 and day < 3:
            user = input("Please enter your day. \n")


            if user.lower() == 'sunday':
                print(g.sunday)
            elif user.lower() == 'monday':
                print(g.monday)
            elif user.lower() == 'tuesday':
                print(g.tuesday)
            elif user.lower() == 'wednesday':
                if day == 2:
                    print(g.saturday)
                elif day == 1:
                    print(g.wednesday)
            
            elif user.lower() == 'thrusday':
                print(g.thrusday)
            elif user.lower() == 'friday':
                print(g.friday)
            elif user.lower() == 'saturday':
                print(g.saturday)

            elif user.lower() == 'exit':
                quit()

            else:
                condition = False

        elif day >=3 :
            raise RuntimeError("Go home and get fatty.")








