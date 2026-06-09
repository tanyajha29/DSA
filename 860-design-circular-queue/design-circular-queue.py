class MyCircularQueue(object):

    def __init__(self, k):
        self.k = k
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0
        

    def enQueue(self, value):
        if self.isFull() :
           return False
        
        # move rear
        self.rear = (self.rear + 1) % self.k

        # insert value
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty() :
            return False

        # move front
        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True

    def Front(self):
        if self.isEmpty() :
            return -1

        return self.queue[self.front]
        

    def Rear(self):
        if self.isEmpty() :
            return -1

        return self.queue[self.rear]
        

    def isEmpty(self):
        return  self.count == 0
        

    def isFull(self):
        return self.count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()