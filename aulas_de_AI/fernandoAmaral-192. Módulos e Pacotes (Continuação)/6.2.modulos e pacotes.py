from statistics import mean, median

# from statistics import *    ele nao está aceitando esta sintax
#from statistics import mean, median -> assim eu posso chamar
#  diretamente as funções pelo nome

z=[10,20,30,40]

x=mean(z)
y=median(z)
# odd number = quantidade impar de elementos
# even number = quantidade par de elementos
print(z)
print('even list z mean ',x)
print('even list  z median ',y)

a=[10,20,30,40,50]

b=mean(a)
c=median(a)
print(a)
print('odd list a mean ',b)
print('odd list a median ',c)





