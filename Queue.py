class Queue:
    def __init__(self):
        self.queue = list()

    def __isempty(self):
        """
            Check is the queue is empty or not.
        """
        if len(self.queue) == 0:
            return True
        else:
            return False
            
    def enqueue(self,item):
        """
            Add item of the queue.
        """
        val = self.queue.append(item)
        return val

    @property
    def dequeue(self):
        """
            Remove the first item from the queue.
        """
        if self.__isempty() == False:
            val = self.queue.pop(0)
            return val
        else:
            raise RuntimeError('The Queue is empty.')
        
    @property
    def front(self):
        """
            Get the front item of the queue.
        """
        if self.__isempty() == True:
            raise RuntimeError('The queue is empty.')
        else:
            val = self.queue[0]
            return '{}, is the front of queue.'.format(val)
    
    @property
    def back(self):
        """
            Get the back item of the queue. 
        """
        if self.__isempty() == True:
            raise RuntimeError('The queue is empty.')
        else:
            val = self.queue[-1]
            return '{}, is the back of queue.'.format(val)


    @property
    def display(self):
        """
            Get the items of the queue. 
        """
        return '{}'.format(self.queue)

Q = Queue()
Q.enqueue(45)
Q.enqueue(5)
Q.enqueue(4)
Q.enqueue(45)
Q.enqueue(45)
Q.enqueue(45)
Q.enqueue(45)
Q.enqueue(45)
print(Q.back)
print(Q.front)
print(Q.display)
print('class size',Q.__sizeof__())








