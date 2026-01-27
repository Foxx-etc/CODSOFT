import random as r

lower = []
lower.extend("qwertyuiopasdfghjklzxcvbnm")

upper = []
upper.extend("QWERTYUIOPASDFGHJKLZXCVBNM")

symbols = []
symbols.extend("~!@#$%^&*()_+-[]{}:;',.><?/")

num = []
num.extend("1234567890")


while True:
    try:
        lenOfPass = int(input("Lenght Of Password : "))
        break
    except:
        print("Invalid Input! Enter Number...")

complexity = input("Enter The Complexity Of The Password (E)asy, (M)edium, (H)ard : ").upper()



# Easy : only including charachters from 2 variables - lower, upper
if complexity == 'E':
    result = []
    r.shuffle(result)
    while len(result) <= lenOfPass:
        result.append(r.choice(lower))
        result.append(r.choice(upper))
    while len(result) != lenOfPass:
        result.pop()



# Medium : only including charachters from 3 variables - lower, upper, symbols
elif complexity == 'M':
    result = []
    r.shuffle(result)
    while len(result) <= lenOfPass:
        result.append(r.choice(lower))
        result.append(r.choice(upper))
        result.append(r.choice(symbols))
    while len(result) != lenOfPass:
        result.pop()



# Hard : only including charachters from all 4 variables - lower, upper, symbols, num
elif complexity == 'H':
    result = []
    r.shuffle(result)
    while len(result) <= lenOfPass:
        result.append(r.choice(lower))
        result.append(r.choice(upper))
        result.append(r.choice(symbols))
        result.append(r.choice(num))
    while len(result) != lenOfPass:
        result.pop()


print("".join(result))


