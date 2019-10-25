import sys
bank = 0
lives = 3
print("THE GAME OF QUAILAND : The Awakining")
print("Shikoric 1")
overwriten = input("level 1 : is my number lower than 62 or higher than , if its lower type < if its higher type >")
print("hint : clock")
if overwriten == "<":
  print("WRONG")
  bank -= 3
  lives -= 1
if overwriten == ">":
  print("GREAT!!!!!!!!!!!!!!!!!!!! *sarcasm included*")
  bank += 3
if lives == 0:
  print("Sorry , But you ran out of lives")
  print("your score is " + str(bank))
  sys.exit()

untitled = input("Level 2 : is my number 76? type yes or no")
print("hint: orbit")
if untitled == "yes":
  print("Great! u smart")
  bank += 3
if untitled == "no":
  print("Wrong")
  bank -= 3
  lives -= 1
if lives == 0:
  print("Sorry , But you ran out of lives")
  print("your score is " + str(bank))
  sys.exit()
itsgood = input("level 3: how many letters in the alphabet type 11 or 36")
if itsgood == "11":
  print("u aced it!")
  bank += 3
if itsgood == "36":
  print("wrong its how many letters in *the alphabet*")
  bank -= 3
  lives -= 1
if lives == 0:
  print("Sorry , But you ran out of lives")
  print("your score is " + str(bank))
  sys.exit()
itsgod = input("what is 0/0 type 0 or nn")
if itsgod == "nn":
  print("thats correct! you're good at this")
  bank += 3
if itsgod == "0":
  print("Wrong!")
  bank -= 3
  lives -= 1
print("You walked in a hallway and saw a mystirious golden orb with a golden sign saying FOR THE HERO , there was 2 guards who let you picked it up it was the one and only IOMIc slatt")
print("You heard a voice saying the domocruio beast is coming , you must hurry")
print("Go now theres not alot of time left before Quiland faces its end")
print("Go,save Quiland ")
print("To be continued on THE GAME OF QUILAND : IOMIc")
print("final score")
print(bank)
print("lives remaining")
print(lives)
print("thanks for playing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
