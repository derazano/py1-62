import math
Tri1 = int(input('Number 1 is: '))
Tri2 = int(input('Number 2 is: '))
Tri3 = int(input('Number 3 is: '))
S = (Tri1+Tri2+Tri3)/2
n = S*(S-Tri1)*(S-Tri2)*(S-Tri3)
area = (math.sqrt(n))
print('The area of Triangle is %.2f' %(area))
