import matplotlib.pyplot as plt


def met_cuadrados(n, x0, y0):
    i = 1
    x = x0
    y = y0
    lst_raices = []
    if x*y == n:
        while x != y and i<10:
            x = (x + y) / 2
            y = n / x
            lst_raices.append(y)
            i = i+1
        plt.plot(lst_raices, '.', linestyle='dotted', color='blue')
        plt.title('La raíz cuadrada de ' + str(n) + ' es: ' + str(lst_raices[-1]))
        plt.xlabel('Iteraciones')
        plt.ylabel('Raíz')
        plt.show()
    else:
        print("El producto de x0 e y0 debe ser igual al numero que se obtendra la raiz.")


met_cuadrados(45,9,5)

