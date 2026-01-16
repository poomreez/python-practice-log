gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

print ("Q1) Do you like Dawn or Dusk?")
print ("1) Dawn") 
print ("2) Dusk")
q1 = int (input ("Type your number answer: "))

if q1 ==1 :
  gryffindor +=1
  ravenclaw +=1
elif q1 ==2 :
  hufflepuff +=1
  slytherin +=1
else :
  print ("Wrong input!")

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

print ("Q2) When I’m dead, I want people to remember me as:")
print ("1) The Good") 
print ("2) The Great")
print ("3) The Wise")
print ("4) The Bold")
q2 = int (input ("Type your number answer: "))

if q2 ==1 :
  hufflepuff +=2
elif q2 ==2 :
  slytherin +=2
elif q2 ==3 :
  ravenclaw +=2
elif q2 ==4 :
  gryffindor +=2
else :
  print ("Wrong input!")

# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~

print ("Q3) Which kind of instrument most pleases your ear?")
print ("1) The violin") 
print ("2) The trumpet")
print ("3) The piano")
print ("4) The drum")
q3 = int (input ("Type your number answer: "))

if q3 ==1 :
  slytherin +=4
elif q3 ==2 :
  hufflepuff +=4
elif q3 ==3 :
  ravenclaw +=4
elif q3 ==4 :
  gryffindor +=4
else :
  print ("Wrong input!")

# ~~~~~~~~~~~~~~~ Result ~~~~~~~~~~~~~~~

print ("Total score :")
print ("🦁 Gryffindor :", gryffindor)
print ("🦅 Ravenclaw :", ravenclaw)
print ("🦡 Hufflepuff :", hufflepuff)
print ("🐍 Slytherin :", slytherin)

houses = {
  'Gryffindor': gryffindor, 
  'Ravenclaw': ravenclaw, 
  'Hufflepuff': hufflepuff, 
  'Slytherin': slytherin
}
highest_score = max(houses, key=houses.get)
(print) ("Your house is :", highest_score ,"!")