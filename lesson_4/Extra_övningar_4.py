#1. Skriv ett program som hälsar användaren 10 gånger


hälsning = "Hej! "
x=1

while x < 11:
    print(hälsning)
    x+=1

#2. Skriv ett program (med for-loop) som skriver ut följande:

lista=(1,22,333,4444,55555,666666,7777777,88888888,999999999)
for x in lista:
  print(x)

#3. 
rättal=42
gissning=int(input("Gissa talet"))
while gissning!=rättal:
    gissning=int(input("Fel, försök igen!"))
if gissning == rättal:
        print("Grattis, du har gissat talet!")

#4.
lista_med_olika_tal= [1,45,46,47,25,3,5,9,8,7,200,205,201,405,408,485,48,78,58,68,66,63,13,16,15]
for x in lista_med_olika_tal:
  print(x)
  if x %2==1:
      print("Not allowed!")
      break


#5. 
first_list=[3,7,9,2,6]
second_list=[2,3,6,7,9]

tuple_lista=list()
for tal in second_list:
  first_list_index = first_list.index(tal)
  tuple_lista.append((tal, first_list_index))
  
print(tuple_lista)

# Gör inte 6


#7 
fruits=["apple","orange","pear","banana","grapes"]
my_basket=list()

antal=int(input("How many? "))

position = 0
index = 0

while index < antal:
  index += 1
  my_basket.append(fruits[position])
  position+=1
  if position == 5:
    position = 0
print(my_basket)

#8

i = 0 
primes = list()
while i < 100:
    i += 1

    int_match = 0 
    start = 1 
    
    if (i / 2).is_integer() == False: 
        while i > start: 
            start += 1
            if (i / start).is_integer() == True: 
                print(i)
                int_match += 1

    if int_match == 1:
        primes.append(i) 
print(primes)

    