# number of iterations
n= 20

# multiples of i print fizz
i = 3

# multiples of j print fizz buzz
j = 5

# range operation in python is inclusive on bottom end
# and exclusive on top/second input
# so to go from 1 to 100, need range n+1
for x in range(1,n+1):
    if x % j ==0:
        print("fizz buzz")
    elif x % i==0:
        print("fizz")
    else:
        print(x)


# now write it as a function
# notes: have to test highest multiple condition first, so "fizz buzz"
# argument must be the bigger multiple

def fizz_buzz(n, fizz, fizz_buzz):
    for x in range(1, n+1):
        if x % fizz_buzz == 0: print("fizz buzz")
        elif x % fizz == 0: print("fizz")
        else: print(x)





