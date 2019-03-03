1. Iterators: É um objeto atravessável em toda sua extensão, de modo que se possa acessar todos os
seus elementos; e. g. uma lista.

2. Iterable: É qualquer objeto que pode fornecer um iterator. Em python, é um objeto que tem ou
o método __iter__ ou __getitem__, cujos retornos são ou um iterator ou índices.

3. Iteration: É o processo de acessar um elemento de um objeto, como uma lista. << for x in [1, 2, 3]: >>.

4. Generators: são iterators que podem ser processados, percorríveis ou atravessáveis apenas uma vez.
Isso se dá porque eles não armazenam todos os valores na memória, eles geram (generate) os valores
on the fly, ou seja, durante o próprio processo. Eles são utilizáveis ou por um 'for' loop ou por passá-los
por qualquer função que construa iterations. Na maioria das vezes, generators são implementados como funções,
embora elas não retornem um valor, mas os constroem 'yield'. E. g.:

def generator_function():
	for i in range(10):
		yield i # como 'return', mas seu valor é endereçado para construção dum generator

print(generator_function()) # generator object

for item in generator_function():
	print(item)

-> Exemplo de generator duma sequência de Fibonnaci:

def fibonnaci(n):
	a = b = 1
	for i in range(n):
		yield a
		a, b = b, a + b

for x in fibonnaci(10):
	print(x)


-> Os built-in next() e iter():

Um objeto generator suporta o built-in next(), que chama manualmente o elemento do iteration; e. g.:

def generator_function():
	for i in range(3):
		yield i

gen = generator_function()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) # Raise StopIteration, pois não há mais elementos.

OBS.: O loop 'for', chama next() automaticamente, assim como lida com StopIteration.


Objetos iterables podem ser convertidos em iterators com o built-in iter(), como strings ou listas; e. g.:

string = 'Gabriel'
iterator = iter(string)
print(next(iterator))
print(next(iterator))
print(next(iterator))
