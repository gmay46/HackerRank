def print_rangoli(size):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    placeholder = []
    rangoli = []
    
    #building out the intial lists e -> e,d,c,b,a
    for x in range(size-1,-1,-1):
        placeholder += alphabet[x]
        rangoli.append(list(placeholder))

    #adding the right hand side of the top
    for x in range(len(rangoli)):
        initial_length = len(rangoli[x]) 
        if len(rangoli[x]) > 1:
            for y in range(len(rangoli[x])-1):
                rangoli[x].insert(initial_length, rangoli[x][y])
    
    #need to know the halfway point
    half_size = len(rangoli)

    #cloning the top to the bottom by inserting the lines into the same position
    #stopping prior to the halfway point
    for x in range(half_size-1):
       rangoli.insert(half_size,rangoli[x])

    #add the interior dashes
    joined_rangoli = []
    for item in rangoli:
        joined_rangoli.append('-'.join(item))

    #check the widest letter to letter line (which is in the middle)
    width = len(joined_rangoli[half_size-1])
    
    #add the exterior dashes
    assembled_rangoli = []
    for item in joined_rangoli:
        current_len = len(item)
        if current_len != width:
            spaces = int((width - current_len)/2)
            assembled_rangoli.append("-"*spaces+item+"-"*spaces)
        else:
            assembled_rangoli.append(item)
    
    #
    print("\n".join(assembled_rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#https://www.hackerrank.com/challenges/alphabet-rangoli/problem