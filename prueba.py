import simpleaudio as sa
from sonido import get_sound_array
from plot import barplot
import matplotlib.pyplot as plt


lst_2 = [0, 8, 3, 5, 9, 7]
barplot(lst_2, 2, 5)
plt.show()


sonido = get_sound_array(20)

sa.play_buffer(sonido, 2, 2, 44100)
y = input('Teclea algo')
for i in range(20):
    sa.play_buffer(sonido[i], 2, 2, 44100)