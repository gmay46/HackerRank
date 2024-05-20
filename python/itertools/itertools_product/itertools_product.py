# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == "__main__":
    A = input()   
    B = input()

    for item in list(product(map(int,A.split()),map(int,B.split()))):
        print(item, end = " ")

#https://www.hackerrank.com/challenges/itertools-product/problem