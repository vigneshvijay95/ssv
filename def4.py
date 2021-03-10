#add of two matrrix
a = [[12,15,14],
    [7,15,20],
    [15,16,35]]
b = [[12,15,14],
    [7,15,20],
    [15,16,35]]
Result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range (len(a)):
    for j in range (len(b)):
        Result[i][j] = a[i][j] + b[i][j]
    for r in Result:
        print(r) 