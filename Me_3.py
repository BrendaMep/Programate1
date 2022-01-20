from plot import barplot
import simpleaudio as sa
from sonido import get_sound_array

lis = [3,44,38,5,47,27,2,46,19,16,0]
l2 = [2,4,1,8,7,6,20,9,18]


def metodo_3(ls):
    am = len(ls)
    for i in range(1,am):
       val = ls[i]
       j = i-1
       while j >= 0 and ls[j] >= val:
           ls[j+1] = ls[j]
           j = j-1
           barplot(ls, j)
           sonido = get_sound_array(3)
           sa.play_buffer(sonido, 2, 2, 44100)
       ls[j+1] = val
    return ls



c = metodo_3(lis)
print(c)