import string
import random

alphabets=list(string.ascii_letters)
digits=list(string.digits)
special_char=list("!@#$%&()£")
characters = list(string.ascii_letters+string.digits+"!@#$%&()£")

def generate_random_passwd():
    length=int(input("Entrer la taille du password: "))
    alphabets_count=int(input("Entrer le nombre de lettres que vous voulez: "))
    digits_count=int(input("Entrer le nombre de chiffres: "))
    special_char_count=int(input("Entrer le nombre de character spéciaux: "))
    characters_count=alphabets_count+digits_count+special_char_count
    if characters_count>length:
        print("Le nombre total de caractères est supérieur à la longueur du password.")
        return 
    passwd=[]
    for i in range(alphabets_count):
        passwd.append(random.choice(alphabets))
    for i in range(digits_count):
        passwd.append(random.choice(digits))
    for i in range(special_char_count):
        passwd.append(random.choice(special_char))
    if characters_count<length:
        random.shuffle(characters)
        for i in range(length-characters_count):
            passwd.append(random.choice(characters))
    random.shuffle(passwd)
    print("Voici votre password: ") 
    print("".join(passwd))
    
generate_random_passwd()