Exemplificação insólita do uso de condicionais.

1. Sintaxe: << condition_if_true if condition else condition_if_false >>; e. g.:

is_nice = True
state = "nice" if is_nice else "not nice"
print(state)


2. Sintaxe: << (if_test_is_false, if_test_is_true)[test] >>; e. g.:

nice = True
personality = ("mean", "nice")[nice]
print(f"The cat is {personality}")

Obs.: Recomenda-se não se usar tal forma, uma vez em que há casos onde os dois condicionais são valorados,
pois o tuple é primeiramente construído; e. g.:

condition = True
print(2 if condition else 1/0) # Exemplo 1, em que só um condicional é valorado.
print((1/0, 2)[condition]) # Exemplo 2, raised ZeroDivisionError porque os dois condicionais são valorados.


3. Sintaxe: << first_condition or second_condition >>; e. g.:

print(True or "Some")
print(False or "Some")
