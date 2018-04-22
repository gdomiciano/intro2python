class Planet:

  def __init__(self, name, radius, gravity, system_name):
    self.name = name
    self.radius = radius
    self.gravity = gravity
    self.system_name = system_name

  def orbit(self):
    return f'{self.name} is orbiting in the {self.system_name} system'

earth = Planet('Earth', 120000, 8.5, 'Solar')

print(f'Name is: {earth.name}')
print(f'Radius is: {earth.radius}')
print(f'Gravity is: {earth.gravity}')
print(earth.orbit())

planet_x = Planet('Planet X', 400000, 5.5, 'Solar')

print(f'Name is: {planet_x.name}')
print(f'Radius is: {planet_x.radius}')
print(f'Gravity is: {planet_x.gravity}')
print(planet_x.orbit())
