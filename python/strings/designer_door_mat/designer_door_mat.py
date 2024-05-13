# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    s = input()
    dims = s.split()
    length = int(dims[0])
    width = int(dims[1])
    
    rug = []
    y = 1
    for i in range(int((length-1)/2)+1):
        string = ""
        if i != (length-1)/2:
            number_of_dashes = int((width - ((i+y)*3))/2)
            string = "-"*number_of_dashes
            string = string + ".|."*((i+y))
            string = string + "-"*number_of_dashes
            y += 1
            rug.append(string)

        else:
            for j in range(int((width-7)/2)):
                string += "-"
            string = string + "WELCOME"
            string = string + string[:int((width-7)/2)] 
            rug.append(string)
        
    rug_len = len(rug)-2
    for x in range(rug_len,-1,-1):
        rug.append(rug[x])
            
        
    for line in rug:
        print(line)

#https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true