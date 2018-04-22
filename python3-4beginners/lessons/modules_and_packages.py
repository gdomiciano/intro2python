
from space.planet import Planet
from space.calc import planet_mass, planet_vol


earth = Planet('Earth', 120000, 8.5, 'Solar')
print(f'Name is: {earth.name}')
print(f'Radius is: {earth.radius}')
print(f'Gravity is: {earth.gravity}')
print(earth.orbit())
print(f'shape is: {earth.shape}')
print(earth.commons())
print(earth.spin('a very high speed'))


earth_mass = planet_mass(earth.gravity, earth.radius)
earth_vol = planet_vol(earth.radius)

print(f'{earth.name} had a mass of {earth_mass} and a volume of {earth_vol}')
