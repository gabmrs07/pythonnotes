Datatypes:

1. Mutable: capazes de mudança.
2. Immutable: constantes.

foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']
print(foo)
# Expected output: ['hi']
# Real output: ['hi', 'bye']

Tal output acontece porque toda vez que se cria um alias de um mutable datatype, se há uma mudança no alias
ou na matriz, então ele é refletido aos seus clones.

def printer(f):
	def wrapper(*args, **kwargs):
		print(f(*args, **kwargs))
	return wrapper

@printer
def add_to(num, target = []):
	target.append(num)
	return target

add_to(1) # Output: [1]
add_to(2) # Output: [1, 2]
add_to(3) # Output: [1, 2, 3]

Os outputs da função não são, respectivamente, << [1] >>, << [2] >> e << [3] >>; mas são cumulativos. Isso
se dá por conta de que os default arguments são declarados somente uma vez, na definição da função, e não
toda a vez que uma função é chamada. Portanto, argumentos mutáveis não devem ser usados como default arguments
se a intenção da função for a de reutilizar a variável sem os valores anteriores. Como resolução do exemplo
acima, tem-se o estabelecimento dum imutável, << None >>, como default argument:

def printer(f):
	def wrapper(*args, **kwargs):
		print(f(*args, **kwargs))
	return wrapper

@printer
def add_to(num, target = None):
	if target is None:
		target = []
	target.append(num)
	return target

add_to(1) # Output: [1]
add_to(2) # Output: [2]
add_to(3) # Output: [3]
