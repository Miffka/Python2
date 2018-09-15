#-*-coding:utf8;-*-
#qpy:3
#qpy:console

# попытаемся сделать реализацию при помощи графов, т.е. структур "узел":["дети"]

import sys

sys.stdin = open('/storage/emulated/0/qpython/scripts3/Pytho2_14_task4_tests.txt')

data = {}

n = int(input())

#считываем данные со входа
for i in range(n):
    line = input().strip()
    if ":" in line:
        line = [j for j in line.split(":")]
        line = list(map(lambda sin: sin.strip(), line))
        if " " in line[1]:
            line[1] = [j for j in line[1].split()]
            
            for k in line[1]:
                if k in data.keys():
                    data[k].append(line[0])
                else:
                    data[k] = []
                    data[k].append(line[0])
        else:
            if line[1] in data.keys():
                data[line[1]].append(line[0])
            else:
                data[line[1]] = []
                data[line[1]].append(line[0])
        
        if line[0] not in data.keys():
            data[line[0]] = []
    else:
        if line not in data.keys():
            data[line] = []


# следующая функция ищет путь path в графе graph от start до end
def find_path(graph, start, end, path=[]):
    path.append(start)
    if start == end:
        print("Equals")
        return path 
    if graph[start] == []:
        print("Dead end", path)
        return False
    for node in graph[start]: 
        if node not in path: 
            newpath = find_path(graph, node, end, path) 
            if newpath: 
                print("Path change", path)
                return newpath
    print("Program end")
    return False

print(data)

q = int(input())

for i in range(q):
    line = [j for j in input().split()]
    line = list(map(lambda sin: sin.strip(), line))
    print(line)
    if line[0] in data.keys() and line[1] in data.keys():
        if line[0] == line[1]:
            ans = "Yes"
        elif find_path(data, line[0], line[1]) != False:
            ans = "Yes"
        else:
            ans = "No"
    else:
        ans = "No"
    print(ans)
    print(find_path(data, line[0], line[1]))
    print()