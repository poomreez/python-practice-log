class City:
  def __init__(self, name, country, population, landmarks, code, founding_year, mayor):
       self.name = name
       self.country = country
       self.population = population
       self.landmarks = landmarks
       self.code = code
       self.founding_year = founding_year
       self.mayor = mayor

   

bangkok = City('Bangkok', 'Thailand', 11392000, ['Grand Palace', 'Wat Arun', 'Chao Phraya River'], 'BKK', 1238, 'Chadchart Sittipunt')
newyork = City('New York', 'USA', 8419000, ['Statue of Liberty', 'Empire State Building', 'Central Park'], 'NYC', 1625, 'Bill de Blasio')
print(vars(bangkok))
