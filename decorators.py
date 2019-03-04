Antes de explicar os decorators, há alguns assuntos sobre funções que precisam ser dominados.
Por exemplo, tome-se << some_function >> abaixo:

def some_function():
	pass

A linha << some_function() >> executa a função, enquanto que a linha << some_function >> faz apenas
referência à função, porém não a executa.

-> Nested functions: funções podem ser definidas dentro de outras funções; e. g.:

def hi(name = "Gabriel"):
	print("Now you are inside the hi() function")

	def greet():
		return "Now you are in the greet() function"

	def welcome():
		return "Now you are in the welcome() function"

	print(greet())
	print(welcome())
	print("Now you are back in the hi() function")

hi()


-> Funções podem retornar outras funções; e. g.:

def hi(name = "Gabriel"):
	def greet():
		return "Now you are in the greet() function"

	def welcome():
		return "Now you are in the welcome() function"

	if name == "Gabriel":
		return greet
	else:
		return welcome

a = hi()
print(a) # No output, << a >> aponta para greet()
print(a()) # print(a("Jobson")) tem como output um erro, pois greet() não tem nenhum parâmetro.

b = hi("Jobson")
print(b) # No output, << b >> aponta para welcome()
print(b())


-> Funções como argumentos de outras funções; e. g.:

def hi():
	return "Hi Gabriel!"

def do_something_before_hi(function):
	print("I'm doing some boring work before executing hi()")
	print(function())

do_something_before_hi(hi)



-> Decorators: são funções que modificam a funcionalidade de outras funções, ou seja, executam
código antes e depois de uma função. Confira pep-318 para mais informações. Exemplos:


1. Exemplo longo:

def new_decorator(function):

	def wrap_the_function():
		print("I am doing some boring work before executing function()")
		function()
		print("I am doing some boring work after executing function()")

	return wrap_the_function

def function_decorable():
	print("I am the function which needs some decoration to remove my foul smell")

function_decorable()

function_decorable = new_decorator(function_decorable)
function_decorable()


2. Exemplo curto:

def new_decorator(function):

	def wrap_the_function():
		print("I am doing some boring work before executing function()")
		function()
		print("I am doing some boring work after executing function()")

	return wrap_the_function

@new_decorator # @new_decorator == function_decorable = new_decorator(function_decorable)
def function_decorable():
	"""Hey you! Decorate me!"""

	print("I am the function which needs some decoration to remove my foul smell")

function_decorable()

<< @new_decorator >> é uma forma curta de dizer:
<< function_decorable = new_decorator(function_decorable) >>.

No exemplo curto, << print(function_decorable.__name__) >> tem como output << wrap_the_function >>, mas
o esperado era << function_decorable >>. Para o nome e o docstring de function_decorable não seja sobreposto
por wrap_the_function, usa-se functools.wraps:

from functools import wraps

def new_decorator(function):

	@wraps(function)
	def wrap_the_function():
		print("I am doing some boring work before executing function()")
		function()
		print("I am doing some boring work after executing function()")

	return wrap_the_function

@new_decorator
def function_decorable():
	"""Hey yo! Decorate me!"""

	print("I am the function which needs some decoration to remove my foul smell")

function_decorable()
print(function_decorable.__name__)


3. Outro exemplo:

from functools import wraps

def decorator_name(function):

	@wraps(function)
	def decorated(*args, **kwargs):
		if not can_run:
			return "Function will not run"
		return function(*args, **kwargs)

	return decorated

@decorator_name
def test_function():
	return("Function is running")

can_run = True
print(test_function())

can_run = False
print(test_function())


-> Usos notáveis dos decorators:

a. Autorizações: normalmente usados em Flask e Django para checar se há permissões de uso do app; e. g.:

from functools import wraps

def requires_auth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username, auth.password):
			authenticate()
		return f(*args, **kwargs)
	return decorated

b. Logging; e. g.:

from functools import wraps

def logit(func):
	@wraps(func)
	def with_logging(*args, **kwargs):
		print(func.__name__ + " was called")
		return func(*args, **kwargs)
	return with_logging

@logit
def addition_func(x):
	"""Do some math."""
	return x + x

result = print(addition_func(4))


-> Nested decorators em funções:

from functools import wraps

def logit(logfile = 'file.log'):

	def logging_decorator(func):

		@wraps(func)
		def wrapped_function(*args, **kwargs):
			log_string = func.__name__ + " was called"
			print(log_string)
			# Open the logfile and append
			with open(logfile, 'a') as opened_file:
				# Now we log to the specified logfile
				opened_file.write(log_string + '\n')

		return wrapped_function

	return logging_decorator

@logit() # @logit() == myfunc1 = logit()(myfunc1)
def myfunc1():
	pass

myfunc1()

@logit(logfile = 'func2.log')
def myfunc2():
	pass

myfunc2()


-> Decorators com classes:

class Logit(object):

	logfile = 'out.log'

	def __init__(self, func):
		self.func = func

	# Depois que a classe for instanciada, o seu objeto pode ser usado como esta função.
	# instance = Logit() -> lança __init__
	# instance() -> lança __call__
	def __call__(self, *args):
		log_string = self.func.__name__ + " was called"
		print(log_string)
		# Open the logfile and append
		with open(self.logfile, 'a') as opened_file:
			# Now we log to the specified logfile
			opened_file.write(log_string + '\n')
		# Now, send a notification
		self.notify()

		# return base func
		return self.func(*args)


	def notify(self):
		# Decorators com classes permitem mais funções!
		pass

# Renomeia logfile
Logit.logfile = 'out2.log'

@Logit # myfunc1 = Logit(myfunc1) -> lança Logit.__init__(myfunc1)
def myfunc1():
	pass

myfunc1() # -> lança Logit.__call__()
