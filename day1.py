#Exercise #1
#Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

list_num = []
i = 0
while i >= len(list_num):
    i += 1
    if i == 11:
        break
    print(i**3)

#Get first prime numbers up to 100
for i in range(2,101): 
    for j in range(2,101):
        if i%j == 0:
            break
    if i == j:
        print(i)

#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors. Gracefully log the error if the user doesn't enter a number
age = int(input("User's Age: "))

if age < 18:
    print("kids")
elif age >= 18 and age <= 65:
    print("Adults")
else:
    print("Seniors")