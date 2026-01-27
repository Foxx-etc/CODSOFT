import random as r

# we would use this variable to convert all the letters to upper case by str().upper()
alpha = []
alpha.extend("qwertyuiopasdfghjklzxcvbnm")

symbols = []
symbols.extend("~!@#$%^&*(+-[}:;<?/")

num = []
num.extend("1234567890")

# validation
while True:
    try:
        lenOfPass = int(input("Lenght Of Password : "))
        break
    except:
        print("Invalid Input! Enter Number...\n")

complexity = input("Enter The Complexity Of The Password (E)asy, (M)edium, (H)ard : ").upper()


# Easy : only including charachters from 2 variables - lower, upper
if complexity == 'E':
    result = []
    r.shuffle(result)
    while len(result) <= lenOfPass:
        result.append(r.choice(alpha))
        result.append(r.choice(str(alpha).upper()))
    while len(result) != lenOfPass:
        result.pop()
    print(f'Your Password : { ''.join(result) }')


# Medium : only including charachters from 3 variables - lower, upper, symbols
elif complexity == 'M':
    result = []
    r.shuffle(result)
    while len(result) <= lenOfPass:
        result.append(r.choice(alpha))
        result.append(r.choice(str(alpha).upper()))
        result.append(r.choice(symbols))
    while len(result) != lenOfPass:
        result.pop()
    print(f'Your Password : { ''.join(result) }')


# Hard : only including charachters from all 4 variables - lower, upper, symbols, num
elif complexity == 'H':
    result = []
    r.shuffle(result)
    while len(result) <= lenOfPass:
        result.append(r.choice(alpha))
        result.append(r.choice(str(alpha).upper()))
        result.append(r.choice(symbols))
        result.append(r.choice(num))
    while len(result) != lenOfPass:
        result.pop()
    print(f'Your Password : { ''.join(result) }')
else:
    print("Invalid Input! Try Again")
