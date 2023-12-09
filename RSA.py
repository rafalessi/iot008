# IOT 008
# Rafael Alessi Muntsch
# rafalessi87@gmai.com

# Codigo para RSA dado numeros primos do usuario a serem utilizados na criptografia RSA de uma mensagem predefinida
# Tem algum erro que se a mensagem for um numero maior que o produto dos numeros primos, ela nao eh corretamente criptografada.

import random

# Funcao da internet para verificar se eh numero primo
def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

while True:
    try:
        p1 = int(input('Primeiro numero primo:'))
        while isPrime(p1) != True:
            print('Numero nao primo. Tente novamente! Primeiro numero primo:')
            input_p1 = input()
            p1 = int(input_p1)
        break
    except ValueError:
        print('Numero nao valido. Tente novamente! Primeiro numero primo:')

while True:
    try:
        p2 = int(input('Segundo numero primo:'))
        while isPrime(p2) != True:
            print('Numero nao primo. Tente novamente! Segundo numero primo:')
            input_p2 = input()
            p2 = int(input_p2)
        break
    except ValueError:
        print('Numero nao valido. Tente novamente! Segundo numero primo:')


print("Numeros primos selecionados:",p1,",",p2)

n = p1*p2 # produto dos numero primos selecionados
print("Valor derivante dos numeros selecionados:",n)

z = (p1-1)*(p2-1) # valor do tociente
print("Tociente: ",z)

# Sugerir o outro valor de chave baseado em fatores que tem que ser primo, menor que o tociente e nao pode ser fator do tociente 
primes = [i for i in range(1,z) if z%i != 0 and isPrime(i)] 
#print(primes)
pu1 = random.choice(primes) # selecionar alguns dos valores calculados aleatoriamente

pr1_t = 1 # valor inicial de chave privada iniciar verificacao
cont_inicial = 0
cont_final = random.randint(1,5) # valor aleatorio para selecionar a x iteracao desse calculo (usei ate 10 para nao gerar calculos muito grandes)
# funcao para achar a primeira chave privada que atenda a restricao de (pu1*pr1)%z
while True:
    mod = (pu1*pr1_t)%z
    if mod == 1:
        if cont_inicial == cont_final:
            break        
        cont_inicial += 1
    pr1_t +=1

pr1 = pr1_t

print("Chave Publica (PU) : ", pu1)
print("Chave Privada (PR) : ", pr1)

m = [80, 70, 20, 30] # mensagem


print("Mensagem Enviada: ", m)
m_crp = []
m_dcrp = []

# Gerar mensagem criptografada
for i in m:
   i1=pow(i,pu1)
   i2=i1%n
   m_crp.append(i2)
print("Mensagem Encriptada: ", m_crp)

# decodificar mensagem criptograda
for j in m_crp:
   j1 = pow(j,pr1)
   j2 = j1%n
   m_dcrp.append(j2)
print("Mensagem Decriptada: ", m_dcrp)

if m_dcrp == m:
   print("Mensagem recebida e corretamente decriptada")
else:
   print("Mensagem recebida, mas nao corretamente decriptada")
   

