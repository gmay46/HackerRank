if __name__ == '__main__':
    s = input()
    
    hasAlphanumeric, hasAlphabet, hasDigit, hasLower, hasUpper = False,False,False,False,False
    
    for char in s:
        if char.isalnum():
            hasAlphanumeric = True
        if char.isalpha():
            hasAlphabet = True
        if char.isupper():
            hasUpper = True
            continue
        if char.islower():
            hasLower = True
            continue
        if char.isnumeric():
            hasDigit = True
            continue
        if hasAlphanumeric == True and hasAlphabet == True and hasDigit == True and hasLower == True and hasUpper == True:
            break
            
    print(hasAlphanumeric)
    print(hasAlphabet)
    print(hasDigit)
    print(hasLower)
    print(hasUpper)

#https://www.hackerrank.com/challenges/string-validators/problem