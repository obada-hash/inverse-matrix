n = int(input('enter matrix size: '))
lower = []
upper = []
a = []
b = []

# get lower matrix
print("Enter lower matrix")
for i in range(n):
    row = []
    for j in range(n):
        v = int(input(f'{i} {j}: '))
        row.append(v)
    lower.append(row)

# get upper matrix
print('Enter upper matrix')
for i in range(n):
    row = []
    for j in range(n):
        v = int(input(f'{i} {j}: '))
        row.append(v)
    upper.append(row)


def isOne(itr, i):
    if itr == i:
        return 1
    return 0


def calcA(row):
    counter = 0
    for i in range(row):
        counter += a[i] * lower[row][i]
    return counter


def calcB(row):
    counter = 0
    for i in range(n-1, row, -1):
        counter += b[i] * upper[row][i]
    return counter


inverse = []
for i in range(n):
    a.clear()
    b = [0] * n
    for j in range(n):
        a.append(isOne(j, i)-calcA(j))

    for j in range(n-1, -1, -1):
        div = upper[j][j]
        b[j] = (a[j] - calcB(j)) / div
    inverse.append(b)


print('inverse matrix: ')
print('#' * (n * 2))
for i in range(n):
    for j in range(n):
        print(inverse[j][i], end=' ')
    print()
print('#' * (n * 2))
n = input('press enter to exit')  # to let you see the result
