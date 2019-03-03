1. Sets: comportam-se basicamente como listas, mas não tem ordem e não podem conter elementos idênticos.

Exemplo:

lista = [1, 2, 3, 3, 4, 5, 6, 7, 7, 8]
duplos = []

for elemento in lista:
	if lista.count(elemento) > 1 and elemento not in duplos:
		duplos.append(elemento)
print(duplos)

lista = [1, 2, 3, 3, 4, 5, 6, 7, 7, 8]
duplos = set([x for x in lista if lista.count(x) > 1])
print(duplos)


2. Set methods:

-> União: junta os elementos de dois grupos e retorna um único set.

set1 = {'amarelo', 'vermelho', 'azul', 'verde', 'preto'}
set2 = {'vermelho', 'marrom'}
print(set1.union(set2))

-> Intersecção: compara dois grupos e retorna seus elementos comuns.

set1 = {'amarelo', 'vermelho', 'azul', 'verde', 'preto'}
set2 = {'vermelho', 'marrom'}
print(set1.intersection(set2))

-> Diferença: compara dois grupos e retorna os elementos não compartilhados com o segundo set.

set1 = {'amarelo', 'vermelho', 'azul', 'verde', 'preto'}
set2 = {'vermelho', 'marrom'}
print(set1.difference(set2))

-> Diferença simétrica: compara dois grupos e retorna os elementos não compartilhados entre ambos.

set1 = {'amarelo', 'vermelho', 'azul', 'verde', 'preto'}
set2 = {'vermelho', 'marrom'}
print(set1.symmetric_difference(set2))

-> Gênero: verifica se um grupo está para o outro grupo na relação de gênero.

animais = {'cachorro', 'gato', 'jacaré', 'caturrita', 'homem'}
reptil = {'jacaré'}
print(animais.issuperset(reptil))

-> Subordinação: verifica se um grupo está para outro grupo na relação de espécie.

animais = {'cachorro', 'gato', 'jacaré', 'caturrita', 'homem'}
reptil = {'jacaré'}
print(reptil.issubset(animais))
