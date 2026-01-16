class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(f'The sound of {self.name} is: {self.name}! {self.name}!')
  
  def display_details(self):
    print(f'Entry Number: {self.entry}')
    print(f'Name: {self.name}')
    print(f'Type: {self.types}')
    print(f'Description: {self.description}')
    if self.is_caught == True:
      print(f'{self.name} has already been caught!')
    else:
      print(f'{self.name} has not been caught yet..')

pikachu = Pokemon(25, 'Pikachu', 'Electric', 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', True)
clefairy = Pokemon(35, 'Clefairy', 'Fairy', 'On nights with a full moon, Clefairy gather from all over and dance. Bathing in moonlight makes them float.', False)
psyduck = Pokemon(54, 'Psyduck', 'Water', 'It is constantly wracked by a headache. When the headache turns intense, it begins using mysterious powers.', False)

pikachu.speak()
pikachu.display_details()

clefairy.speak()
clefairy.display_details()

psyduck.speak()
psyduck.display_details()