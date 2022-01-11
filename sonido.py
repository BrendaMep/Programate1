import numpy as np

SF = 128000  # HZ sampling frequency
DELAY = 50  # ms
MAXSOUND = 20000  # sound volumn
MAXF = 4000  # max frequency
MINF = 400  # min frequency


def make_sound(frequency, time_delay=DELAY, sampling_frequency=SF, max_sound=MAXSOUND):
    t = 2 * np.pi * frequency * np.arange(time_delay * sampling_frequency / 1000) / sampling_frequency
    marray = max_sound * np.sin(t)
    marray = marray.astype(np.int16)
    return marray


def get_sound_array(n, min_f=MINF, max_f=MAXF,
                    time_delay=DELAY, sampling_frequency=SF, max_sound=MAXSOUND):
    step = (max_f - min_f) // n
    sound_list = []
    for idx, f in enumerate(range(min_f, max_f, step)):
        if idx < n:
            sound_list.append(make_sound(f, time_delay=time_delay))
    return np.stack(sound_list, axis=0)
