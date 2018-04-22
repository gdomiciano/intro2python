class Planet:

  def __init__(self):
    self.name='Earth'
    self.radius=120000
    self.gravity=8.5
    self.system='Solar system'

  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}'

earth = Planet()

print(f'Name is: {earth.name}')
print(f'Radius is: {earth.radius}')
print(f'Gravity is: {earth.gravity}')
print(earth.orbit())

planetX = Planet()
