x = [4,5,6,7]
r = ["h", "o", "l", "a"]
print(list(zip(x,r)))

m = [11,21,23]
n = ["edad", "edad", "edad"]
v = ["hermana", "hermano", "hermana"]
print(list(zip(n,m)))
print(list(zip(v,m)))
print(list(zip(v,n,m)))

for i,j in zip(n,m):
    print("i:", i, "-j:", j)

ls = [i+4 for i in m]
print(ls)

m_1 = [1,2,3]

ls_1 = [j +2**j for j in m_1]
print(ls_1)


ls_2 = [print(i) for i in range(3) if m[i]<m_1[i] ]
print(ls_2)