import random
from termcolor import colored

colours = ["red", "green", "blue", "white"]

def xmas_tree(n):
    print("\n\n")
    k = 2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k -1
        for j in range(0,i+1):
            print(colored("* ", random.choice(colours)), end="")
        print("\r")
        amount = 2*n-3
    for i in range(0,3):
        print(" "*amount, "#")

xmas_tree(20)