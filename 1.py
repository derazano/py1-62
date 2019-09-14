snum = ("Zero","One","Two","Three","Four","Five","Six","Seven","Eight","nine")
num  = input('Enter a number: ')

for i in num:
    print(snum[int(i)], end=" ")
