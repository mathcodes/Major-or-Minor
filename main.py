print("\n\nWelcome to the major or minor chord identifier. Have your guitar or piano ready to answer the questions!\n")

root = str(input('• What is the first note of the cord you are playing? \n• In other words what is the "root" of the chord? \n• This is mpost likely the lowest note being played when you play the chord.\n\n'))

third = str(input('\n• What is the third note of the scale?\n\n'))

fretDistance = int(input('\n• How many frets do you have to move on one string to go from the root to the 3rd note?\n\n'))

if fretDistance == int(3):
  scale = str("minor")
  print(f"\nOk, That mean the first chord is a minor chord! You can play the {scale} scale over these chord.!")
else:
  scale = str("Major")
  print("\nOk, That mean the first chord is a Major chord! You can play {scale} scale over these chord!\n\n")

print("\nEXCELLENT!!!\n\nLet's dig a little deeper! \n\nThere are many different scales, or modes, that start with both the minor chord and the Major Chord.\n\nGet this phrase stuck in your head forever: \n\nI Dig People Like My Aunt Locrian\n\n Now think Ancient Greece. More specifically, the different regions of Ancient Greece where the major contributors in forming  the basis of the music theory we use today lived!!! Yeah, those ones! \n\nHere they are: \n\nIonian, Dorian, Phrygian, Lydian, Myxolydian, Aeolian, Locrian\n\n I • D • P • L • M • A • L")


"""bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y" or "y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
"""