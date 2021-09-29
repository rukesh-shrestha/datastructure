class Multiply:
    def __init__(self):
        print("Here you can get multiplication table of any number.")


    def multiplication(self,number,table=10):
        for x in range(1,table+1):
            yield x * number


if __name__ == '__main__':
    m = Multiply()
    condition = True
    user = int(input("Please enter the number to get the multiplication."))
    table = int(input("Please enter the number to get the multiplication upto."))
    mu = m.multiplication(number=user,table=table)
    for x in range(1,15):
        print(next(mu))
    