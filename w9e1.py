def triangle(n):
   m = n*2-1 #m is num star
   c = m//2 #c is mid of column
   for i in range(n):
       le = c - i
       re = c + i
       print(end="         ")
       for j in range(m):
           if(j < le or j > re):
               print("_",end="")
           else:
               print("*",end="")

       print()
    

#
n = int(input("Enter your number: "))
print("Triangle Star")
triangle(n)
print("End Star")
