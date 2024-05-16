def print_rangoli(size):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    placeholder = []
    rangoli = []
    
    for x in range(size-1,-1,-1):
        placeholder += alphabet[x]
        rangoli.append(list(placeholder))

    for x in range(len(rangoli)):
        initial_length = len(rangoli[x]) 
        if len(rangoli[x]) > 1:
            for y in range(len(rangoli[x])-1):
                rangoli[x].insert(initial_length, rangoli[x][y])
    
    half_size = len(rangoli)

    for x in range(half_size-1):
       rangoli.insert(half_size,rangoli[x])

    joined_rangoli = []
    for item in rangoli:
        joined_rangoli.append('-'.join(item))

    width = len(joined_rangoli[half_size-1])
    assembled_rangoli = []
    for item in joined_rangoli:
        current_len = len(item)
        if current_len != width:
            spaces = int((width - current_len)/2)
            assembled_rangoli.append("-"*spaces+item+"-"*spaces)
        else:
            assembled_rangoli.append(item)
    print("\n".join(assembled_rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#https://www.hackerrank.com/challenges/alphabet-rangoli/problem