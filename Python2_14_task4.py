#-*-coding:utf8;-*-
#qpy:3
#qpy:console

n = int(input())
data = []

class Classes:
    def __init__(self, value, parents = []):
        self.value = value
        self.parents = parents
        self.ancestors = [value]
        
    def allparents(self):
        if self.parents == []:
            self.ancestors.extend(self.parents)
        else:
            return list(map(allparents(), self.parents))          
            
    def hasancestor(self, whois):
        if whois in self.ancestors:
            print("Yes")
        else:
            print("No")

for i in range(n):
    line = input()
    if ":" not in line:
        data.append(Classes(line))
    else:
        line = [j for j in line.split(": ")]
        if " " in line[1]:
            line[1] = [j for j in line[1].split()]
        data.append(Classes(value=line[0], parents=line[1]))

data = list(map(allparents(), data))

q = int(input())

for i in range(q):
    line = input().split()
    for k in data:
        if line[1] == data[k].value and line[0] in data[k].ancestors:
            print("Yes")
        else:
            print("No")