*args e **kwargs

1. Não é necessário escrever *args e **kwargs, mas apenas * e ** respectivamente.
2. Ambos são usados na definição de funções, como parâmetros, e passam vários argumentos para uma função.
3. A ordem dos parâmetros na função é: << def func(normal_arg, *args, **kwargs): >>.
4. O uso mais comum de ambos é em functions decorators.

*args:
Permite enviar uma quantidade indefinida de variáveis non-keyworded como argumento duma função, cujo
acesso na função será por intermédio duma lista chamada args; e. g.:

def test_var_args(f_arg, *args):
	print(f"first normal arg: {f_arg}")
	print(f"*args list: {args}")
	for arg in args:
		print(f"another arg through *args: {arg}")

test_var_args('gabriel', 'python', 'eggs', 'test')

**kwargs:
Permite enviar uma quantidade indefinida de variáveis keyworded como argumento duma função, cujo
acesso será por intermédio dum dicionário chamado kwargs; e. g.:

def test_var_kwargs(**kwargs):
	print(f"**kwargs dict: {kwargs}")
	for key, value in kwargs.items():
		print(f"Key: {key}, Value: {value}")

test_var_kwargs(name='gabriel')


-> Usando *args e **kwargs para chamar uma função:

Considere a seguinte função:

def test_args_kwargs(arg1, arg2, arg3):
	print(f'arg1: {arg1}')
	print(f'arg2: {arg2}')
	print(f'arg3: {arg3}')

# Para passar os argumentos em *args:
args = ["two", 3, 5] # ou por tuple = ("two", 3, 5)
test_args_kwargs(*args)

# Para passar os argumentos em **kwargs:
kwargs = {'arg3': 3, 'arg2': 'two', 'arg1': 5}
test_args_kwargs(**kwargs)
