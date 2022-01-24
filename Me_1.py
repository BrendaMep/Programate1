import random
from plot import barplot
import simpleaudio as sa
from sonido import get_sound_array


ls_2 = [0,11,45,3,4,18,7]

ls_3 = []

for i in range(10):
    ls_3.append(random.randrange(20))


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

print("Lista")
print(ls_3)
print("Lista ordenada: ")
metodo_1(ls_3)
print(ls_3)
