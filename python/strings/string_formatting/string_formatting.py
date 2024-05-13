def print_formatted(number):

    pad = len(str("{0:b}".format(number)))
    for num in range(1,number+1):  
        print(str(num).rjust(pad, " ") + " " +str("{0:o}".format(num)).rjust(pad, " ")+ " " +str("{0:x}".format(num)).rjust(pad, " ").upper()+ " " + str("{0:b}".format(num)).rjust(pad, " ") ) 
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#https://www.hackerrank.com/challenges/python-string-formatting/problem