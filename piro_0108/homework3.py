n = 4

for i in range(n+1):
    if i == 0:
        print(' '*(n-i)+'#')
    else:
        print(' '*(n-i)+'#'+'*'*(2*i-1)+'#')

for i in range(n):
    if i == (n-1):
        print(' '*(i+1)+'#')
    else:
        print(' '*(i+1)+'#'+'*'*(2*(n-i-1)-1)+'#')