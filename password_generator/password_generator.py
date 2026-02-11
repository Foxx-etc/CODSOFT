import random as r

# we would use this variable to convert all the letters to upper case by str().upper()
alpha = ("qwertyuiopasdfghjklzxcvbnm")
symbols = ("~!@#$%^&*(+-[}:;<?/")
num = ("1234567890")


# validation
while True:
    try:
        lenOfPass = int(input("Lenght Of Password(must be greater than 6): "))

        try:
            if not lenOfPass >= 6:
                raise Exception
            else:
                break
        except:
            print("length must be greater than 6!\n")

    except:
        print("Invalid Input! Enter Number...\n")


# validation
while True:
    try:
        complexity = input("Enter The Complexity Of The Password (E)asy, (M)edium, (H)ard : ").upper()
        if not complexity.isalpha():
            raise Exception
        
        elif complexity.isalpha():
            try:
                if complexity=='E' or complexity=='M' or complexity=='H':
                    break
                else:
                    raise Exception
            except:
                print("ENTER VALID LETTER!\n")

    except Exception:
        print("ENTER A LETTER!\n")

# we got both lenOfPass & complexity valid


# Easy : only including charachters from 2 variables - lower, number
if complexity == 'E':
    result = []

    while len(result) <= lenOfPass:
        result.append(r.choice(alpha))
        result.append(r.choice(num))

    while len(result) != lenOfPass:
        result.pop()
  
    r.shuffle(result)
    print(f'Your Password : { ''.join(result) }')


# Medium : only including charachters from 3 variables - lower, upper, symbols
elif complexity == 'M':
    result = []

    while len(result) <= lenOfPass:
        result.append(r.choice(alpha))
        result.append(r.choice(str(alpha).upper()))
        result.append(r.choice(symbols))

    while len(result) != lenOfPass:
        result.pop()

    r.shuffle(result)
    print(f'Your Password : {''.join(result)}')


# Hard : only including charachters from all 4 variables - lower, upper, symbols, num
elif complexity == 'H':
    result = []

    while len(result) <= lenOfPass:
        result.append(r.choice(alpha))
        result.append(r.choice(str(alpha).upper()))
        result.append( r.choice(symbols))
        result.append(r.choice(num))

    while len(result) != lenOfPass:
        result.pop()
    
    r.shuffle(result)
    print(f'Your Password : { ''.join(result) }')


else:
    print("Invalid Input! Try Again")
