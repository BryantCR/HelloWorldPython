print( "Hello World" )

name = "Bryan"
print( "Hello", name )	# with a comma
print( "Hello"+ name )	# with a +

num = 20
print( "Hello", num )	# with a comma
print( "Hello"+ str(num) )	# with a +	-- this one should give us an error!

fave_food1 = "Hamburguer"
fave_food2 = "Ice cream"
print( "I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string