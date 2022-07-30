# funcao simples sem argumentos
def imprime():
    print('esta funcao imprime mermo . ')

print('funcao imprime() ',imprime())


print('=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=')
# funcao que imprime texto que recebe na chamada da funcao como parametro
# acrescentei um return, return sempre retorna um int.
# já o parametro (n) pode ser String, int, operação ou expressão matemática
# variável operator recebendo uma chamada de funcao, e dei um print na variável

def imprime_comparametro(n):
    print(n)
    return (2**10 + 1000*8)


imprime_comparametro("""
Fellow-citizens of the United States:
In compliance with a custom as old as the government itself, 
I appear before you to address you briefly, and to take, in your presence,
the oath prescribed by the Constitution of the United States, to be taken 
by the President "before he enters on the execution of this office."
  """)

imprime_comparametro('bora tomar um vege de limao, irmao')
imprime_comparametro(2**10)
imprime_comparametro(2**10 + 1000*8)
operator = imprime_comparametro('Querido operator\n calculate 2**10 + 1000*8 = ')
print(operator)

print('=-=-=-=quando uma função retorna um valor-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=')
# quando uma função retorna um valor
# tenho que atribuir seu chamado a uma variavel

def potencia(n):
    return n * n

#executando a função
x = potencia(3)
print(x)

def power(n):
    return 2 ** n

#executando a função return 2 ** n
print('=-=-=-=-=função power return 2 ** n=-=-=-=-=-=')

x2 = power(2)
x2 = power(3)
x2 = power(4)
x2 = power(5)
x2 = power(6)
x2 = power(7)
x2 = power(8)
x2 = power(9)
x2 = power(10)
x2 = power(11)
print('funcao power ',x2)

print('=-=-=-=magic numbers executados na funcao power dentro de um for  loop=-==-=-=-=-=-=-=-=-=-=-=-=-=-=')
powerList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
for elemento in powerList:
    print(power(elemento))
    

print('=-=-=-=-=-Fim dos magic numbers=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

# funções com parametros-padrao

def intervalo(inicio=1, fim=10):
    #esta funcao imprime qualquer intervalo    
    for inicio in range(1, fim+1):
        print(inicio,'-> ',end='')
        #return inicio



print(intervalo(),'fim')
print(intervalo(300,800),'fim')
print(intervalo(100, 1000),'fim')

#one = intervalo()
#two = intervalo(3,8)
#three = intervalo(10,15)

#print('argumentos padrao var one  ',one)
#print('passando novos args ',two)
#print('intervalo de 100 a 1000  ',three)
