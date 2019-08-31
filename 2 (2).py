n = int(input("Input a number: "))
i = 0
n = n*2-1
while(n):
    i+=1

    if(i<n):
        t=i
    else:
        t=n
    print("#"*t)
    n-=1
