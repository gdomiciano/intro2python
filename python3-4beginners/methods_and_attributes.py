class Planet:

  # Class level attribute
  shape = 'round'

  # instance Method
  def __init__(self, name, radius, gravity, system_name):
    self.name = name
    self.radius = radius
    self.gravity = gravity
    self.system_name = system_name

  # instance method
  def orbit(self):
    return f'{self.name} is orbiting in the {self.system_name} system'

  # class level method
  @classmethod
  def commons(cls):
    return f'All planets are {cls.shape} because of the gravity'

  #works for instance and class methods, does not access instance and class atributes or methods
  @staticmethod
  def spin(speed='200 miles per hour'):
    return f'the planet spins and spins at {speed}'

earth = Planet('Earth', 120000, 8.5, 'Solar')

print(f'Name is: {earth.name}')
print(f'Radius is: {earth.radius}')
print(f'Gravity is: {earth.gravity}')
print(earth.orbit())
print(f'shape is: {earth.shape}')
print(earth.commons())


#Accessing via class level
print(f'shape is: {Planet.shape}')
print(Planet.commons())
