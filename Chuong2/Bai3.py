import math
print("Nhap hai canh ke cua tam giac vuong:")
a=int(input(""))
b=int(input(""))
h=a*a+b*b
x=math.sqrt(h)
print("Canh ke thu nhat la:",a,', canh ke thu hai la:',b,', co canh huyen=',round(x,2),sep='')
