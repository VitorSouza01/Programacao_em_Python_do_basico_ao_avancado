"""
Debugando com PDB

PDB → Python Debugger

Vida de Inseto → Life’s Bug

Bug → Inseto

Obs: a utilização do print(( para debugar código é uma prática ruim.

def dividir(a, b):
    print(f"a={a}, b={b}")
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um problema: {err}"

print(dividir(4, 7))




Existem formas mais profissionais de ser fazer esse ‘debug’,  utilizando o debugger.

Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando o PDB - Python Debugger

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um problema: {err}"

print(dividir(4, 7))




Exemplo com o PDB - Python Debugger - Exemplo 1

Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

Comando básicos do PDB:

l (listar onde estamos no código)

n (próximo linha)

p (imprime variável)

c (continua a execução - finaliza o debugging),




import pdb

nome = "Angelina"
sobrenome = "jolie"
pdb.set_trace()
nome_completo = nome + " " + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + " faz o curso " + curso
print(final)



Exemplo com o PDB - Python Debugger - Exemplo 2

nome = "Angelina"
sobrenome = "jolie"
import pdb; pdb.set_trace()
nome_completo = nome + " " + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + " faz o curso " + curso
print(final)

Por quê utilizar este formato?

R: O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas no início de
arquivo. Por isso, ao invés de colocarmos o import do pdb no início do arquivo, nós colocamos somente onde vamos
debuggar, e ao finalizar já fazemos a remoção.




Exemplo com o PDB - Python Debugger - Exemplo 3

Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

*A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado como
função built-in (integrada) chamada breakpoint()

nome = "Angelina"
sobrenome = "jolie"
breakpoint()
nome_completo = nome + " " + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + " faz o curso " + curso
print(final)




# Obs: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))
"""

# Como os nomes das variáveis são os mesmos dos comandos pdb, devemos utilizar o comando p para imprimir as variáveis.
# Ou seja, p nome_da_varíavel

# Nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos.

def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4









