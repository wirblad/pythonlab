# #---VAR----

# #UPPG4

# print("Skriv in ditt förnamn:")
# fnamn = input()
# print("Skriv in ditt efternamn:")
# enamn = input()
# print(f"Du heter: {enamn} {fnamn}")

# #UPPG5

# print("Mata in tal1:")
# tal1 = int(input())
# print("Mata in tal2:")
# tal2 = int(input())
# resultat = tal1**tal2
# print(resultat)
# resultat = tal1 % tal2
# print(resultat)
# resultat = tal1 // tal2
# print(resultat)

# #UPPG8

# tal = int(input("Mata in tal: "))
# print(tal >= 100)

# #----IF-----

# #UPPG1

# tal = int(input("Mata in ett tal: "))
# if tal > 10:
#     print("Talet är större än 10")
# if tal <= 10:
#     print("Talet är mindre än 10")

# #UPPG2

# tal = int(input("Hur många paket finns kvar: "))
# if tal < 10:
#     print("Beställ 30 st")
# elif tal >= 10 and tal < 20:
#     print("Beställ 20 st")
# else:
#     print("Behövs ej")

# #UPPG3

# tal1 = int(input("Ange ett tal: "))
# tal2 = int(input("Ange ett tal till: "))
# if tal1 > tal2:
#     tal3 = tal1
# else:
#     tal3 = tal2
# print(f"Det största talet är {tal3}")

#UPPG4

# tal1 = int(input("Ange ett tal: "))
# tal2 = int(input("Ange ett tal till: "))
# tal3 = int(input("och ett till: "))

# biggest = 0

# if tal1 > tal2 and tal1 > tal3:
#     biggest = tal1
# elif tal2 > tal1 and tal2 > tal3:
#     biggest = tal2
# else:
#     biggest = tal3
# print(f"Det största talet är {biggest}")

#UPPG5

# category = str(input("Vilken kategori tillhör du: "))
# if category == "vuxen":
#     print("Resan kostar 30 kr")
# elif category == "student":
#     print("Resan kostar 20 kr")
# elif category == "pensionär":
#     print("Resan kostar 20 kr")

#UPPG6

# birthyear = int(input("Enter year of birth: "))
# if birthyear >= 1980 and birthyear < 1990:
#     print("You are born in the 1980s")
# elif birthyear < 2000 and birthyear >= 1990:
#     print("You are born in the 1990s")
# elif birthyear < 1980 or birthyear > 2000:
#     print("You are NOT born in the 1980s or 1990s")

#UPPG7

# country = str(input("Enter your country: "))
# if country == "sverige" or country == "norge" or country == "danmark":
#     print("You live in scandinavia")
# else:
#     print("You don't live in scandinavia")

#UPPG8

# sum = int(input("How much money u got?: "))
# discount = str(input("Do you have discount?: "))

# if sum >=15 and sum <25 and discount == "no":
#     print("You can buy a small burger")
# elif sum >=15 and sum <25 and discount == "yes":
#     print("You can buy a small burger and fries")
# elif sum >25 and sum <=50 and discount == "no":
#     print("You can buy a big burger")
# elif sum >25 and sum <=50 and discount == "yes":
#     print("You can buy a big burger and fries")
# elif sum > 60 or sum > 50 and sum < 60 and discount == "yes":
#     print("You can buy a meal")

#-- STRINGS ---- 

#UPPG1

# word1 = str(input("Enter text1: "))
# word2 = str(input("Enter text2: "))
# word3 = str(input("Enter text3: "))

# print(f"You wrote the following words: {word1} {word2} {word3}")

#UPPG2

# string = "hello world"
# substring = string.find("w")
# print(f"Hittad w på pos {substring}")

#UPPG3

#namn = "kurt andersson"
#print(namn.title())

#UPPG4

# string = "detta är en text som du skall ändra"
# string2 = (string.replace(" ", "*"))
# print(string2)
# print(string2.count("*"))

#UPPG5

# string = input("Enter e-mail: ")
# print(string)

# if string.find("@") != -1 and string.find(".") != -1:
#     print("has a @ and .")
# else:
#     print("Not correct mail")

# substring = string.split(".")
# substring2 = substring[2]

# if len(substring2) == 2 or len(substring2) == 3:
#     print("CORRECT")
# else:
#     print("Not correct")

#UPPG6

# string = input("Enter a text: ")
# print(len(string.split()))

#UPPG7

# string = input("Enter a text: ")
# string2 = string [::-1]
# new = string.replace(" ","")
# new2 = string2.replace(" ","")
# if new == new2:
#     print("PALINDROME")
# else:
#     print("NOT PALINDROME")

#LOOP

#UPPG1

# for x in range(0,11):
#     print(x)

# x = 0

# while x < 11:
#     print(x)
#     x=x+1

#UPPG2

# tal1 = int(input("Enter a number: "))
# tal2 = int(input("Enter second number: "))

# if tal1 > tal2:
#     small = tal2
#     big = tal1
# else:
#     small = tal1
#     big = tal2

# #for x in range(small,big):
# #    print(x)

# while small < big:
#     print(small)
#     small = small + 1

#UPPG 3

# while True:
#    tal1 = int(input("Enter a number: "))
#    tal2 = int(input("Enter second number: ")) 
#    print(f"Sum = {tal1+tal2}")
#    cont = input("Do you want to continue: ")
#    if cont == "no":
#     break

#UPPG4

# sum = 0
# for x in range(1,11):
#     tal = int(input(f"Enter number{x}: "))
#     sum = sum + tal
# print(sum)

#UPPG5

# tal = int(input("Enter a number: "))

# while tal > 0:
#     print(tal)
#     tal=tal-1

#UPPG6

# while True:
#    import random
#    print("Rolling the dices....")
#    print("The values are ....")
#    tal1 = random.randint(1,6)
#    tal2 = random.randint(1,6)

#    print(tal1)
#    print(tal2)
   
   
#    cont = input("Roll again: ")
#    if cont == "no":
#     break

#---- LISTOR -----

#UPPG1

# list = []

# for x in range(1,5):
#    tal = int(input(f"Enter number{x}: "))
#    list.append(tal)

# biggest = 0
# for x in list:
#    if x > biggest:
#       biggest = x

# print(f"Biggest number is {biggest}")

#UPPG2

#board = []

# for i in range(8):
#    if i == 1 or i == 6:
#       row = ['b']
#    else:
#       row = ['']
#    for i in range(8):
#       board.append(row)


#print(board)

#UPPG3

# bankaccounts = {}

# while True:

#    val = input("1. Skapa konto\n2. Ta bort konto\n3. Lista alla kontonummer\n4. Lista totalsaldo\n5. Lista alla kontonummer och saldo\n6. Quit\n")
#    if val == "1":
#       accountNr = input("Ange kontonummer att skapa: ")
#       saldo = int(input("Ange saldo: "))
#       bankaccounts[accountNr] = saldo
#    if val == "2":
#       accountNr = input("Ange kontonummer att ta bort: ")
#       del bankaccounts[accountNr]
#    if val == "3":
#       for key in bankaccounts.keys():
#          print(f"Kontonummer: {key}")
#    if val == "4":
#       Totalvalue = 0
#       for value in bankaccounts.values():
#          Totalvalue = Totalvalue + value
#       print(f"Totalt saldo på banken: {Totalvalue}")
#    if val == "5":
#       for key,value in bankaccounts.items():
#          print(key, value)
#    if val == "6":
#       break

# -- FUNC --

#UPPG1


# def add(str1, str2):
#    return str1+str2



#UPPG2

# def calcVat(sum):
#       return sum*0.2

#UPPG3

# def adult(age):
#    if age < 18:
#       return False
#    else:
#       return True



# age = int(input("Enter your age"))
# if adult(age):
#    print("Your are an adult")
# else:
#    print("You are not an adult")

#UPPG4

# def findLongestWord(listofStrings):
#    longest = ""
#    for x in listofStrings:
#       if len(x) > len(longest):
#          longest = x
#    return longest


# listofStrings = ["testm","massa","strängar","hej"]
# print(findLongestWord(listofStrings))

#UPPG5

# def calcTaxes(salery):
#    if salery >= 30000:
#       return salery*0.33
#    elif salery < 15000:
#       return salery*0.12
#    else:
#       return salery*0.28

# print(calcTaxes(20000))

# ----- CLASS ----

#UPPG1

# class matRatt:
#    def __init__(self, namn, pris, typ, kalorier):
#       self.namn = namn
#       self.pris = pris
#       self.typ = typ
#       self.kalorier = kalorier
   
# ratt1 = matRatt("köttbullar",100,"kött", 500)
# ratt2 = matRatt("svamplasagne", 120, "vegetarisk", 450)
# ratt3 = matRatt("linssoppa", 80, "vegansk", 300)
# meny = []
# meny.append(ratt1)
# meny.append(ratt2)
# meny.append(ratt3)

# for x in meny:
#    print(f"Alternativ: {x.namn} Pris: {x.pris} Typ: {x.typ} Kalorier: {x.kalorier}\n")



#UPPG2

class Person:
   def __init__(self,birthdate):
      self.birthdate = birthdate
   def setName(self,name):
      self.namn = name
   def changeAdress(self, adress):
      self.adress = adress
   namn = ""
   adress = ""
   postNr = 0
   postOrt = ""

p1 = Person("23-04-13")
p1.setName("Henrik")
p1.changeAdress("Törresröd")
p1.postOrt = "lilla edet"
print(p1.birthdate)
print(p1.namn)
print(p1.adress)
print(p1.postOrt)












  










    











