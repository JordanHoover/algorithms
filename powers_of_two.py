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
''' Explanation of the recursion:

When the recursion happens, it's going to stop the execution
of the current stack frame at that point.
Then it's going to keep going down to the base case of n equals 1

Then, 1 will be returned to the stack frame that came before it,
and will become the value of prev,
and execution will continue on that frame: it will then calculate
a value for itself, by multiplying prev (which is now 1), by 2.
then it will print out this curr value of 2
then it will return this curr value to the next stack frame,

the next stack frame up will get the 2 for it's prev value,
and then continue execution at that point -> multiplying this val
by 2 and then printing it and then returning the new curr value of 
4 to the stack frame above it,
and that will keep going until all it's all done
'''
