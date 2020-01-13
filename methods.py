mylist = [1,2,3]
mylist.append(4)
print(mylist)
mylist.pop()
print(mylist)
mylist.reverse()
print(mylist)
#help(mylist.insert)
mylist.sort()
print(mylist)

##############################     FUNCTIONS!   ################################
def name_function():
	"""
	DOCSTRING: Information about the function. 
	Input: no input. 
	OUTPUT: Hello
	"""
	print("Hello")

name_function()

def say_hello(name="NAME"):
	return ("HELLO " + name)

result = say_hello("Emilio")
type(result)
print(result)



def add(a1,a2):
	return a1 + a2

result = add(10,20)

print(result)


# FInd out if the word "dog" is in a string

def dog_check(mystring):
	return 'dog' in mystring.lower()

print(dog_check("Dog ran away"))


#################  Pig Latin

def pig_latin(word):
	first_letter = word[0]
	# check if vowel 
	if first_letter in 'aeiou':
		pig_word = word + 'ay'
	else:
		pig_word = word[1:] + first_letter + 'ay'

	return pig_word

print(pig_latin("apple"))

def myfunc(a,b):
	#Returns 5% of the sum of a and b
	return sum((a,b)) * 0.05
print(myfunc(40,60))


def myfunction(*args):
	print(args)
	for item in args:
		print (item)

myfunction(40,60,100,1,34)


def myfunc(**kwargs):
	print(kwargs)
	if 'fruit' in kwargs:
		print('My fruit of choice is {}'.format(kwargs['fruit']))
	else:
		print('I did not find any fruit here')


myfunc(fruit='apple', veggie= 'lettuce')


def myfunc(*args, **kwargs):
	print(args)
	print(kwargs)
	print('I would like {} {}'.format(args[0], kwargs['food']))

myfunc(10,20,30, fruit='orange', food='eggs', animal='dogs')


 











