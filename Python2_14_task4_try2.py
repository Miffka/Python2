#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#data = {'A':[[],[]], 'B':[[],[]], 'C':[['A', 'B'],[]], 'D':[['C'],[]]}

# ошибка Failed test 2: wrong answer
# необходимо добавить добавление необъявленного родителя в словарь с данными
# все еще Failed test 2: wrong answer
# бьютифицировали список
# все еще Failed test 2: wrong answer
# попробовали добавить вывод "Yes" при проверке равенства предка и потомка, даже если они не в списке
# все еще Failed test 2: wrong answer 

data = {}
lost = []

def getanc(k):
    if data[k][0] != []:
    # если список родителей не пуст
        for p in data[k][0]:
        # перебираем родителей
            if p in data.keys():
            # если родитель был объявлен ранее
                if data[p][1] == []:
                # и если у родителя пуст список предков
                    getanc(p)
                    # выполняем эту функцию для родителя
                data[k][1].extend(data[p][1])
                # добавляем предков родителя в свой список предков
                
            else:
            # иначе, то есть когда родитель не был объявлен ранее
                if p not in lost:
                # если родителя еще нет в потеряшках
                    lost.append(p)
                    # добавляем его в потеряшки
                
                data[k][1].append(p)
                # добавляем такого родителя в предки
            
            if k not in data[k][1]:
                data[k][1].append(k)
                #и себя добавляем в список своих предков
    else:
    # иначе, то есть если список родителей пуст
        data[k][1].append(k)
        # добавляем себя в список своих предков


n = int(input())

for i in range(n):
    line = input().strip()
    if ":" not in line:
        data[line] = [[],[]]
    else: #необходимо добавить добавление в список родителей по известному ключу
        line = [j for j in line.split(" : ")]
        line[0] = line[0].strip()
        if " " in line[1]:
            line[1] = [j for j in line[1].split()]
            line[1] = list(map(lambda silly: silly.strip(), line[1]))
        else:
            line[1] = line[1].strip()
        
        if line[0] in data.keys():
            data[line[0]][0].extend(line[1])
        else:
            data[line[0]] = [[],[]]
            data[line[0]][0].extend(line[1])
    #print(data)

for i in data.keys():
    getanc(i)

for i in lost:
    data[i] = [[],[i]]

#print(data)

q = int(input())

for i in range(q):
    line = [j for j in input().strip().split()]
    line = list(map(lambda sin: sin.strip(), line))
    if line[0] in data.keys() and line[1] in data.keys():
        if line[0] in data[line[1]][1]:
            print('Yes')
        else:
            print('No')
    else:
        #if line[0] == line[1]:
        # проводим эксперимент - если ключей нет в словаре, но они одинаковые
            #print('Yes')
        print('No')



'''
lst_mro = ['G : F','A','B : A','C : A','D : B C','E : D','F : D','X','Y : X A','Z : X','V : Z Y','W : V']
lst_q = ['A G','A Z','A W','X W','X QWE','A X','X X','1 1']

'''
'''
lst_mro = ['A : B C D G H','B : C E G H K L','C : E D H K L','E : D F K L','D : G H','F : K','G : F','H : L','K : H L','L']
lst_q = ['K D','D A','G D','H A','E E','H G','E L','B D','D L','D G','D E','A F','A C','K A','A H','K D','H B','K B','D L','G G','A H','K L','G E','B A','C K','K L','C L','H L','G C','D D','C G','E A','F K','B G','H L','L F','H G','D A']
lst_res = ['Yes','Yes','Yes','Yes','Yes','Yes','No','No','No','No','Yes','No','No','Yes','No','Yes','Yes','Yes','No','Yes','No','No','Yes','Yes','No','No','No','Yes','Yes','No','Yes','No','No','No','Yes','Yes','Yes','No']

for i in lst_mro:
    if ":" not in i:
        data[i] = [[],[]]
    else:
        i = [j for j in i.split(" : ")]
        if " " in i[1]:
            i[1] = [j for j in i[1].split()]
        data[i[0]] = [[],[]]
        data[i[0]][0].extend(i[1])
    print(data)


for i in data.keys():
    getanc(i)

for i in lost:
    data[i] = [[],[i]]

print(data)

results = []

for i in lst_q:
    i = i.split()
    if i[0] in data.keys() and i[1] in data.keys():
        if i[0] in data[i[1]][1]:
            print('Yes')
            results.append('Yes')
        else:
            print('No')
            results.append('No')
    else:
        print("No")
        results.append('No')

from itertools import compress

if results == lst_res:
    print("Test correct")
else:
    print("Test incorrect")
    print(list(map(lambda i: print(results[i], lst_res[i], lst_q[i], sep = " "), range(len(results)))))
'''