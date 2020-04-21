num = int(input())
n = 1
a = '+___ '
b = '|' + str(n) + ' / '
c = '|__\ '
d = '|    '
print(a * num)
while n <= num:
    print(b, end='')
    n += 1
    b = '|' + str(n) + ' / '
    if n > num:
        print(end='\n')
print(c * num)
print(d * num)
