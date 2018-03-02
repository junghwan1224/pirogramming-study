n = int(input())
n1 = 0
if n%2==0:
    n1 = int(n/2)
else:
    n1 = int(n/2) + 1

for i in range(n1):
    st =''
    for j in range(i,n1-1):
        st += ' '
    for k in range(0,2*i+1):
        st += '*'

    print(st)

for i in range(n1):
    st = ''
    for j in range(0,i+1):
        st += ' '
    for k in range(2*i,2*n1-3):
        st += '*'
    print(st)