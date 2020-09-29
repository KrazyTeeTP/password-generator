import random
import string

# chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01233456789'
chars = string.ascii_letters + string.digits + '!@#$'

num_chars = int(input("please enter the number of characters you want: "))
num_pass = int(input("please enter the number of passwords you want to generate: "))

for x in range(num_pass):
	final_pass = ""
	for x in range(0, num_chars):
		rand_char = random.choice(chars)
		final_pass = final_pass + rand_char
	print(final_pass)
