#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, element):
        super(LoggableList, self).append(element)
        self.log(element)

m = LoggableList()
m.append(34)