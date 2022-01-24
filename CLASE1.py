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