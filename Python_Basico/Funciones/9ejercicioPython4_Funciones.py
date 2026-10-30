#Cree una función que le dé la vuelta a un string y lo retorne.
#Esto ya lo hicimos en iterables.
#“Hola mundo” → “odnum aloH”

word="Hola Mundo galactico"
def opposite(word):
    new_word=""
    for letter in range(len(word)-1,-1,-1):
        new_word=new_word+word[letter]
    return new_word
print(opposite(word))