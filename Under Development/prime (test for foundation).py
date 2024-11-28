
print('''This is a program to find the prime numbers. Enter any positive number, 0 included in front of the Number field.
      The programe will tell you if the value you entered is not a number. Negative numbers are'nt supported yet.''')
deter = 5
while deter == 5:
    n = (input('Number: '))
    dictee = range(-1,9)
    if n == int and n in dictee:
        int(n)
        print('processing...')
        trans = "False"
        
    else:
         print("""Please enter a POSITIVE number
        Letters, Decimals, fractions, percents, special characters and emticons/emojis are not allowed""")
         break
    if n == 1 and n in dictee:
        print(n, "is a prime number")
    elif n == 0:
        print('0 is not a prime number nor a positive number.')
    elif n > 1 and int:
     for i in range(2, n):
           if (n % i) == 0:
            trans = "True"
    if trans == "True":
        print(n, "isn't a prime number")
        continue
    else:
          print(n, " is a prime number")
          continue
