import math
import sys

from Animal import Animal
from Dog import Dog

ar = ["x", "y", "z"]

z = 52
ar.append("a")
for x in ar:
    print(x)

animals = "cuándo no está \n"
print(f'The value of pi is approximately {z:5d}.')
print(f'My hovercraft is full of {animals!r}.')
print("Hola tengo {} apples".format(z))
print(f"Hola tengo {z} apples")
print('The value of pi is approximately %6.5f.' % math.pi)

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print(f"Unexpected error: {sys.exc_info()[0]} with size {len(sys.exc_info())}")
    raise
d: Animal = Dog('Bobby')
d.add_trick('Jump')
d.add_trick('Catch the ball')

print(f"{d.get_specie()}'s name is {d.name} and his tricks are {d.tricks}")
