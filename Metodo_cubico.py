import matplotlib.pyplot as plt

def met_cubico(n):
    i = 1
    x = 1
    y = n
    lst_raices = []
    if x*x*y == n:
        while x != y and i<10:
            x = (2*x + y) / 3
            y = n / (x*x)
            lst_raices.append(y)
            i = i+1
        plt.plot(lst_raices, '.', linestyle='dotted', color='green')
        plt.title('La raíz cubica de ' + str(n) + ' es: ' + str(lst_raices[-1]))
        plt.xlabel('Iteraciones')
        plt.ylabel('Raíz')
        plt.show()

met_cubico(45)

