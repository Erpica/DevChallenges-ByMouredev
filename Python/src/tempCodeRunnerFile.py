string1 = "oamor"
string2 = "roma"

def check_words(string1, string2):
    def is_isogram (mystring):
        isograma = True
        for caracter in mystring:
            if (mystring.lower().count(caracter) > 1):
                isograma = False
        if (isograma == True):
            print(f"\nLa palabra {mystring} es un isograma")


    if (string1.lower() == string2.lower()):
        print(" - Las palabras son iguales - ")
    elif (len(string1) == len(string2) and list(string1.lower())[::-1] == list(string2.lower())):
        print(f"Las parlabras {string1} y {string2} son palíndromas")
        anagrama = True
        for caracter in string1:
            if (string1.lower().count(caracter) == string2.lower().count(caracter)):
                pass
            else:
                anagrama = False
        if (anagrama):
            print(f"\nLas palabras {string1} y {string2} son también anagrama. ")
        else:
            print(f"\nLas palabras {string1} y {string2} no son anagrama. ")
        is_isogram(string1)
        is_isogram(string2)



check_words(string1, string2)