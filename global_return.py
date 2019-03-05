1. << return >> estabelece uma relação com a variável que chama a função.
2. << global >> torna uma variável encerrada num escopo limitado duma função em algo universalmente acessível.

Exemplos de código fazendo a mesma coisa, porém numa com << return >> e noutra com << global >>:

# A variável << result >> é relacionada com a soma de 3 mais 5 por << return >>.
def add(num1, num2):
	return num1 + num2

result = add(3, 5)
print(result)

# A variável << result >> é relacionada com a soma de 3 mais 5 por << global >>,
# que permite o acesso dessa variável fora do escopo da função.
def add(num1, num2):
	global result
	result = num1 + num2

add(3,5)
print(result)


-> Multiple return values:

a. Exemplo com global (DEFICITÁRIO EM CÓDIGOS LONGOS):

def profile():
	global name
	global age
	name = "Danny"
	age = 30

profile()
print(name)
print(age)

b. Exemplo com return de ou tuple ou list ou dict:

def profile():
	name = "Danny"
	age = 30
	return name, age # é o mesmo que (name, age) -> tuple

obj = profile()
print(f"Nome: {obj[0]}, Idade: {obj[1]}")

# ou unpacking diretamente o tuple
p_name, p_age = profile()
print(f"Nome: {p_name}, Idade: {p_age}")
