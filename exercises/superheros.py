# Write your solutions for 1.5 here!
class Superhero:


    def __init__(self, name, power,strength):
        self.name = name
        self.power = power
        self.strength = strength
def vivi(superh):
	print(superh.name)
	print(superh.strength)
v=Superhero("vivian","water",4775)
vivi(v)	
def save(work,Superh):
    if(Superh.strength<work):
        print(Superh.name+" is not strong enough :(")
    else:
        Superh.strength =Superh.strength-work
save(99999,v)
vivi(v)