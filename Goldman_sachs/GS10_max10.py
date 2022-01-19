import math

class PriorityQueue(object):
    queue=[]
    maxsize=0
    def __init__(self,size):
        self.maxsize=size;
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    def find_index(self,arr, n, K):
        start = 0
        end = n - 1
        while start<= end:
            mid =(start + end)//2
            if arr[mid] == K:
                return mid
            elif arr[mid] < K:
                start = mid + 1
            else:
                end = mid-1
        return end + 1

    def insert(self,value):
        if(len(self.queue)==0):self.queue.append(value)
        elif(value<=self.queue[0]):return
        elif(value>self.queue[-1]):
            self.queue.append(value)
            if(len(self.queue)>self.maxsize):self.queue.pop(0)
        else:
            f=self.find_index(self.queue,len(self.queue),value)
            self.queue.insert(f,value)
            if(len(self.queue)>self.maxsize):self.queue.pop(0)
    def value(self):
      return self.queue


def FindMax10(arr):
    a=PriorityQueue(10)
    for i in arr: a.insert(i)
    return a.value()

if __name__=="__main__":
    array=[i for i in range(1000000000)]
    print(FindMax10(array))