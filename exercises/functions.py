# Write your solution for 1.4 here!

def is_prime(x):
	if(x>2 and x%2==0):
		print("it's not prime")
	else:
		i=2
		flag=0
		while(flag==0 and i<x):
			if(x%i==0 and i!=1):
				print("it's not prime")
				flag=1
			i=i+1
is_prime(7)
