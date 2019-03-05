Toda a classe pode ter atributos instanciados (instance attributes). Por padrão, python utiliza um dicionário
(dict) para armazenar atributos instanciados de objetos. Isso é realmente útil, uma vez que permite estabelecer arbitrariamente novos atributos durante o processo de execução.
Contudo, para pequenas classes com atributos conhecidos, isso pode ser um problema. O dicionário gasta bastante
RAM e python não pode reservar uma quantidade específica de memória em criação de objetos para armazenar todos
os atributos da instanciação. Com efeito, se se cria uma quantidade grande de objetos (coisa na casa dos
milhares e dos milhões), a memória RAM e o desempenho vai para o espaço.
Para contornar a situação, pode-se armazenar esses atributos conhecidos em __slots__, evitando que python os
aloque em dicionários, fixando um espaço a um grupo invariável de atributos e salvando RAM.

1. Exemplo sem __slots__:

class MyClass(object):
	def __init__(self, name, identifier):
		self.name = name
		self.identifier = identifier
		self.set_up()
	# ...

2. Exemplo com __slots__:

class MyClass(object):
	__slots__ = ['name', 'identifier']
	def __init__(self, name, identifier):
		self.name = name
		self.identifier = identifier
		self.set_up()
	# ...
