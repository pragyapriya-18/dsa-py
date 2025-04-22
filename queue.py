class queue:
    def __init__ (self):
        self.queue = []
        self.front = -1
        self.rear = -1
    
    def enqueue(self,val):
        self.queue.append(val)
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
    def dequeue(self):
        if len(self.queue) == 0:
            print("queue is empty")
            return
        else:
            temp =self.queue.pop(self.front)
            self.rear -=1
            if len(self.queue) == 0:
                self.front=-1
                self.rear=-1
        return temp
        
    def display(self):
        if len(self.queue) == 0:
            print("queue is empty")
            return
        print("queue is")
        if self.front == self.rear:
            print(self.queue[self.front],"<-front<-rear")
            return
        print(self.queue[self.front],"<-front")
        i = self.front+1
        while i<self.rear:
            print(self.queue[i])
            i += 1
        print(self.queue[self.rear],"<-rear")
        print("queue ends")
a=queue()
while True:
    option = int(input("enter your choice \n 1.insert \n 2.delete \n 3.display \n 4.exit \n"))
    if option == 1:
        value = int(input("enter the value "))
        a.enqueue(value)
        continue
    elif option == 2:
        a.dequeue()
        continue
    elif option == 3:
        a.display()
        continue
    elif option == 4:
        print("exit")
        break
    else:
        print("wrong option")

    



    

