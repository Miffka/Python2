#-*-coding:utf8;-*-
#qpy:3
#qpy:console

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        
    def can_add(self, v):
        return self.capacity >= v
        
    def add(self, v):
        self.capacity -= v

mycap, addit = map(int, input().split())
mybox = MoneyBox(mycap)
print("1st " + str(mybox.capacity))

print(mybox.can_add(addit))

if mybox.can_add(addit):
    print(mybox.can_add(addit))
    mybox.add(addit)
    
print("2nd " + str(mybox.capacity))
