from plot import barplot
import simpleaudio as sa
from sonido import get_sound_array


def partition(array, ini, fin):
    pivot = array[fin]
    i = ini - 1
    for j in range(ini, fin):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            barplot(array, j)
            sonido = get_sound_array(3)
            sa.play_buffer(sonido, 2, 2, 44100)
    (array[i + 1], array[fin]) = (array[fin], array[i + 1])
    return i + 1


def metodo_4(array, ini, fin):
    if ini < fin:
        pos = partition(array, ini, fin)
        metodo_4(array, ini, pos - 1)
        metodo_4(array, pos + 1, fin)


array = [3,9,6,5,1,4]
print("Lista")
print(array)
tam = len(array)
metodo_4(array, 0, tam - 1)
print(' Lista ordenada: ')
print(array)
