1. Lambda function ou lambda operador é uma forma de criar uma função anônima e pequena.
Lambda sintaxe = << lambda argument_list: expression >>

Exemplo:

sum = lambda x, y: x + y
print(sum(3, 4))


2. List comprehension é uma maneira de criar uma lista a partir dum iterable.
Sintaxe = << list_variable = [x for x in iterable] >>.

Exemplo:

shark_letters = [letter for letter in 'shark']
print(shark_letters)

-> Condicionais 'if' em list comprehensions:
Sintaxe = << list_variable = [x for x in iterable if condition] >>.

Exemplo 1:

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

fish_list = [fish for fish in fish_tuple if fish != 'octopus']
print(fish_list)

Exemplo 2:

number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)


-> Nested loops em list comprehensions:
Nested loops são loops dentro de loops; então, em list comprehensions, são dois loops.

Exemplo de nested loop normal:

lista = []

for x in [10, 20, 30]:
	for y in [1, 2, 3]:
		lista.append(x * y)

print(lista)

Exemplo idêntico em list comprehension:

lista = [x * y for x in [10, 20, 30] for y in [1, 2, 3]]
print(lista)
