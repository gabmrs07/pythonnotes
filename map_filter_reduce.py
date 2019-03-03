1. Map: aplica uma função para todos os items duma input_list.
Sintaxe: << map(function_to_apply, list_of_inputs) >>.

Exemplo sem uso do map:

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
	squared.append(i**2)

print(squared)

Exemplo com map:

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
#squared = [x ** 2 for x in range(1, 6)] list comprehension
print(squared)


Exemplo com map e funções:

def multiply(x):
	return (x * x)
def add(x):
	return (x + x)

funcs = [multiply, add]
for i in range(5):
	value = list(map(lambda x: x(i), funcs))
	print(value)


2. Filter: cria uma lista de elementos, cuja função tem o retorno verdadeiro.
Sintaxe: << filter(function_to_apply, list_of_inputs) >>.

Exemplo:

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
#less_than_zero = [x for x in range(-5, 5) if x < 0] list comprehension
print(less_than_zero)


3. Reduce: aplica uma função de dois argumentos cumulativamente a um dos items da sequência, da esquerda para
a direita, de modo que se reduza a sequência a um único valor.
Sintaxe: << reduce(function, iterable[, initializer]) >>.

Exemplo sem reduce:

sum = 0 # initializer
list = [1, 2, 3, 4, 5]
for num in list:
	sum = sum + num
print(sum)

Exemplo com reduce:

from functools import reduce
sum = reduce((lambda x, y: x + y), [1, 2, 3, 4, 5]) # ((((1 + 2) + 3) + 4) + 5)
print(sum)
