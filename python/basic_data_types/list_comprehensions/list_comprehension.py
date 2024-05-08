
if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3

#-------------For checking in browser
    grid = [[n1,n2,n3] for n1 in range(0,x+1) for n2 in range(0,y+1) for n3 in range(0,z+1)]
    not_sum = [ item for item in grid if sum(item) != n]

    print(not_sum)
#-------------For checking in browser
