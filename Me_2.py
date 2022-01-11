import random
from plot import barplot
import matplotlib.pyplot as plt


ls = [3,9,6,5,1,4]

ls_2 = [0,11,45,3,7,18,7]

ls_3 = []

for i in range(50):
    ls_3.append(random.randrange(150))
print(ls_3)

#El me_1 lleva mas tiempo
"""
#print(ls_3)
def me_1(lis):
    am = len(lis)
    for i in range(am+1):
        for j in range(am-1):
            if lis[j+1] < lis[j]:
                var = lis[j]
                lis[j] = lis[j+1]
                lis[j+1] = var
            barplot(lis,j)
        i +=1
    return lis

#x = me_1(ls)
#print(x)

me_1(ls_2)

print(me_1(ls_3))

"""


def metodo_1(lis):
    am = len(lis)
    baner = False
    while baner == False:
        for j in range(am-1):
            if lis[j+1] < lis[j]:
                baner = True
                var = lis[j]
                lis[j] = lis[j+1]
                lis[j+1] = var
            barplot(lis,j)
        if baner == True:
            baner = False
        else:
            baner = True

    return lis

print(metodo_1(ls_3))