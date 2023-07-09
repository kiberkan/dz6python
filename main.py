a = int(input('1'))
d = int(input('2'))
n = int(input('3'))
result = [a + (i - 1)*d for i in range(1, n+1)]
print(result)