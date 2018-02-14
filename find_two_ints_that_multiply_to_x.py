#  Given an Array of numbers, find 2 integers that multiple to a certain
#  value

#  naive solution
def find_two_ints(input_array, target_value):
  for n in input_array:
    for x in input_array[1::]:
      if x*n==target_value:
        return x,n

#  put in the Array
arry = [1,4,1,6,5,9,20,-3,20]

#  print out the 2 numbers, if there are any
print(find_two_ints(arry, 80))