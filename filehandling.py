"""
    import json
mydict = dict()
with open("text.txt",'r+') as file:
    data = file.read().split(' ')
for x in data:
    if x == "":
        continue
    else:

        if x not in mydict:
            mydict[x] = 1
        else:
            mydict[x] +=1

print(json.dumps(mydict,indent=4))
"""


class ConvertDict:
    def __init__(self):
        __mydict = dict()
        __data = None
        print("Here you can read the file and findout the world repeating.")

    def __reading(self,file):
        with open(file,'r+') as file:
            self.__data = file.read()
            if self.__data != None:

                return self.__data
            # else:
            #     raise RuntimeError("Data is None")

    def count(self,file):
        for x in self.__reading(file):
            if x != None:

                if x not in self.__mydict:
                    self.__mydict[x] = 1
                else:
                    self.__mydict[x] +=1
                    
        return self.__mydict


        

if __name__ == '__main__':
    c = ConvertDict()
    print(c.count("text.txt"))