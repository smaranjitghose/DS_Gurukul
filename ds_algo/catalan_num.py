n = int(input())

catalan = [0] * (n+1)
catalan[0] = 1
catalan[1] = 1
for i in range(2, n+1,1):
    catalan[i] = 0
    for x in range(0,i,1):
        catalan[i] += catalan[x] * catalan[i-1-x]

print(catalan)