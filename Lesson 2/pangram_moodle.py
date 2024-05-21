
# Count the occurrence of vowels in the string entered by the user

# Approach - 1
inputStr = input("Enter the string - ")
vowels = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
    }
    
for c in inputStr:
    if c in vowels:
        vowels[c] += 1
        
print(vowels)

# Approach - 2
inputStr = input("Enter the string - ")
vowelsList = ["a","e","i","o","u"]
vowels = { 
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0}

for c in inputStr:
    if c in vowelsList:
        if c in vowels:
            vowels[c] += 1
        else:
            vowels[c] = 1
            
print(vowels)

# Count the occurrence of each alphabhet in the string entered by the user

inputStr = input("Enter the string - ")
charCount = {
    "a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,
}

for c in inputStr:
    if c.isalpha():
        if c in charCount:
            charCount[c] += 1
        else:
            charCount = 1
            
print(charCount)



# Find if the number entered by the user is a Panagram or not ?

numberAsString = input("Enter the number - ")

numCount = {
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
    "9":0
    }
    
for num in numberAsString:
    if num in numCount:
        numCount[num] += 1
 
panagram = True
for count in numCount.values():
    if count == 0:
        panagram = False

if panagram:
    print("Entered number is a Panagram")
else:
    print("Entered number is not a Panagram")
 
 