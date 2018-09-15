#-*-coding:utf8;-*-
#qpy:3
#qpy:console

data = {}
data["global"] = [[],[]]

def get_name(nname, vname):
    if vname in data[nname][0]:
        print(nname)
    elif nname == "global":
        print("None")
    else:
        get_name(data[nname][1][0], vname)

n = int(input())
for i in range(n):
    line = [j for j in input().split()]
    #print(line)
    #print(data)
    if line[0] == "create":
        data[line[1]] = [[],[]]
        data[line[1]][1].append(line[2])
        #print(data)
    elif line[0] == "add":
        data[line[1]][0].append(line[2])
        #print(data)
    elif line[0] == "get":
        get_name(line[1], line[2])

