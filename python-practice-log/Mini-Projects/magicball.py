import random

question = input("Question: ")
print ("Question :", question)

random_number = random.randint(1, 9)


if random_number == 1:
  print("Magic Ball: Yes - definitely.")
elif random_number == 2:
  print("Magic Ball: It is decidedly so.")
elif random_number == 3:
  print("Magic Ball: Without a doubt.")
elif random_number == 4:
  print("Magic Ball: Reply hazy, try again.")
elif random_number == 5:
  print("Magic Ball: Ask again later.")
elif random_number == 6:
  print("Magic Ball: Better not tell you now.")
elif random_number == 7:
  print("Magic Ball: My sources say no.")
elif random_number == 8:
  print("Magic Ball: Outlook not so good.")
elif random_number == 9:
  print("Magic Ball: Very doubtful.")
else:
  print("Error")


