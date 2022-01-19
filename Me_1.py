import random
from plot import barplot
import simpleaudio as sa
from sonido import get_sound_array
import matplotlib.pyplot as plt


ls = [3,9,6,5,1,4]

ls_2 = [0,11,45,3,4,18,7]

ls_3 = []

for i in range(10):
    ls_3.append(random.randrange(20))
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

#me_1(ls_2)

print(me_1(ls_3))


"""
# Una vez que se ordenan los numeros se termina el programa
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
            sonido = get_sound_array(3)
            sa.play_buffer(sonido, 2, 2, 44100)
        if baner == True:
            baner = False
        else:
            baner = True

    return lis

print(metodo_1(ls_3))