#-*-coding:utf8;-*-
#qpy:3
#qpy:console

closest_mod_5 = lambda x: x if x%5 == 0 else (x + 5 - x%5)

n = int(input())
print(closest_mod_5(n))