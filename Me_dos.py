ls = [7,6,1,4,0,5]

def me_2(lis):
    ar = len(lis)
    for i in range(ar):
        menor = lis[i]
        for j in range(i+1, ar-1):
            if lis[j] < lis[j+1]:
                men = lis[j]
            else:
                n = lis[j]
                lis[j] = lis[j+1]
                lis[j+1] = n

