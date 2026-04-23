string1 = "radar"
string2 = "pythonpython"

# Palíndromas
print(f"La palabra {string1} es palíndroma: ", list(string1.lower())[::-1] == list(string1.lower()))
print(f"La palabra {string2} es palíndroma: ", list(string2.lower())[::-1] == list(string2.lower()))

##### Así mejor: #####
# Palíndromas
#print(f"La palabra {string1} es palíndroma: ", string1 == string1[::-1])
#print(f"La palabra {string2} es palíndroma: ", string2 == string2[::-1])

# Anagama:
print(f"La palabra {string1} es anagrama de {string2}: ", sorted(string1) == sorted(string2))

# Isograma
def is_isogram(my_string):
    isograma_dict = {}
    for character in my_string:
        isograma_dict[character] = isograma_dict.get(character, 0) + 1

    #print (isograma_dict)
    isisogram = True
    num_of_characters = isograma_dict[character]
    for character in isograma_dict:
        if (isograma_dict[character] != num_of_characters):
            isisogram = False
            return

    return isisogram

print(f"La palabra {string1} es isograma: ", is_isogram(string1))
print(f"La palabra {string1} es isograma: ", is_isogram(string2))