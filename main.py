import random

characters = []
characters.append("abcdefghijklmnopqrstuvwxyz")
characters.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
characters.append("0123456789")
characters.append("!@#$%^&*()_+[]{}|;':,.<>?")

allCharacters =''.join(characters)
passwordSize=16

password=''

for i in range(passwordSize):
  position = random.randint(0, len(allCharacters)-1)
  password += allCharacters[position]

print(password)