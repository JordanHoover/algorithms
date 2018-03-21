# print powers of 2 from 1 through n inclusive (so including n)

def powers(n):
    if(n <1):
        return 0
    elif (n==1):
        print(1)
        return 1
    else:
        prev = (powers(n//2))  # need to use integer /floor division
        curr = (prev * 2)
        print(curr)
        return curr

powers(50)
