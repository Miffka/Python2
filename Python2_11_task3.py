#-*-coding:utf8;-*-
#qpy:3
#qpy:console

objects = [0,1,'a',True,False,'a','a','a',[1,2],[1,2]]
ans = 0
flag1 = 0
repobj = []
if len(objects) != 1:
    for i in objects:
        if i not in repobj:
            for j in objects:
                if i is j:
                    repobj.append(i)
                    ans += 1
                    flag1 = 1
            if flag1 == 1:
                ans -= 1
                flag1 = 0
else:
    ans = 0

print(len(objects) - ans)