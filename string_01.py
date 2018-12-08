country = "Bangaldesh"

for c in country:
    print(c)

country = country.replace("Bangaldesh", "BANGladesh")
print(country)

country = country.lower()
print(country)

country = country.upper()
print(country)

country = country.capitalize()
print(country,"\n")

myString = "I am a programmer"
words = myString.split()
print(words)

for word in words:
    print(word)

#count = myString.count("a programmer")
#print(count)
