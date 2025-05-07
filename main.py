import random

characters = []
characters.append("abcdefghijklmnopqrstuvwxyz")
characters.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
characters.append("0123456789")
characters.append("!@#$%^&*()_+[]{}|;':,.<>?")

allCharacters =''.join(characters)
passwordSize=16

password = ''.join(allCharacters[random.randint(0, len(allCharacters)-1)] for _ in range(passwordSize))

# password = ''
# for i in range(passwordSize):
#   password += allCharacters[random.randint(0, len(allCharacters)-1)]

print(password)