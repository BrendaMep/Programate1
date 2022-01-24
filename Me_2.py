import random
from plot import barplot
import simpleaudio as sa
from sonido import get_sound_array

lis = [7,6,1,4,0,5,8,3,9]
#lis[0],lis[3] = lis[3],lis[0]
#print(lis)

def metodo_2(ls):
    am = len(ls)
    for i in range(am):
        menor = ls[i]
        for j in range(i, am):
            if ls[j] <= menor:
                menor = ls[j]
                n = j
                barplot(ls, j)
                sonido = get_sound_array(3)
                sa.play_buffer(sonido, 2, 2, 44100)
        ls[i],ls[n] = ls[n],ls[i]
    return ls

print("Lista")
print(lis)
print("Lista ordenada: ")
metodo_2(lis)
print(lis)

