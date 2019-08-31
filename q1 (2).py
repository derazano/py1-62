s1 = input("Input a string: ")
s2 = input("Input a string: ")
n=0
v=0
l=""
for c in s1:
    if c.isdigit():
        n+=int(c)
        pass
print("The Summation of digit in str1 is: ",n)

for c in s2:
    if c.isdigit():
        v+=int(c)
        pass

print("The Summation of digit in str2 is: ",v)
