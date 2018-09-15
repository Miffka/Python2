#-*-coding:utf8;-*-
#qpy:3
#qpy:console

class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.added = []
    
    def add(self, *a):
        # добавить следующую часть последовательности
        self.added.extend(a)
        while len(self.added) >=5:
            print(sum(self.added[0:5]))
            self.added = self.added[5:]                

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.added

'''
mybuf = Buffer()
mybuf.add(5,6,5,6,5,67)
print(mybuf.get_current_part())
mybuf.add(56)
'''

buf = Buffer() 
buf.add(1, 2, 3) 
buf.get_current_part() # вернуть [1, 2, 3] 
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов 
buf.get_current_part() # вернуть [6] 
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов 
buf.get_current_part() # вернуть [] 
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки 
buf.get_current_part() # вернуть [1]