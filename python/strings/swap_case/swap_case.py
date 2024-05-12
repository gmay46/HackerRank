def swap_case(s):
    
    for_return = ""
    
    for char in s:
        if char.isupper():
            for_return += char.lower()
        else:
            for_return += char.upper()
    
    return for_return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)