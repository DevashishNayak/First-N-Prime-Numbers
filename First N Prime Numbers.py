n=int(input("n"))
if n>0:
    print(2)
f=0
a=0
b=0
c=0
def p(n, m):
    global a
    global b
    f=0
    a=0
    b=0
    for i in range (m, m+n+n-2, 2):
        for j in range(2, i):
            if i%j!=0:
                f=1
            else:
                f=0
                break
        if f==1:
            print(i)
            b=i
        else:
            a+=1
            b+=2
p(n, 3)
while a>0:
    if b==2:
        b=c+2
    c=b
    p(a+1, b+2)