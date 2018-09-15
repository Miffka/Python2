#-*-coding:utf8;-*-
#qpy:3
#qpy:console

class ExtendedStack(list):
    #не описываем добавление и снятие с вершины - эти методы уже есть в классе список
    
    def sum(self):
        # операция сложения
        self.append(self.pop() + self.pop())

    def sub(self):
        # операция вычитания
        self.append(self.pop() - self.pop())

    def mul(self):
        # операция умножения
        self.append(self.pop() * self.pop())

    def div(self):
        # операция целочисленного деления
        self.append(self.pop() // self.pop())

core = ExtendedStack()
core.extend([6, 24, 4])
print(core)
core.div()
print(core)
core.sum()
print(core)
