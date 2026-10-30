#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
#“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

my_text="I love Nación Sushi"
def counter_cases(my_text):
    upper=0
    lower=0
    for letter in my_text:
        if letter.isupper():
            upper=upper+1
        elif letter.islower():
            lower=lower+1   
    print(f"There is {upper} upper cases and {lower} lower cases")
counter_cases(my_text)