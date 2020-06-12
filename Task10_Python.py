#Write a program to remove consecutive duplicates of a given list:
from itertools import groupby
def compress(nums):
    return[key for key, group in groupby(nums)]
n_list = [0,0,1,2,3,3,4,5,6,7,7,7,8,9,9,]
print("Originial list:")
print(n_list)
print("duplicates removed:")
print(compress(n_list))

#write a python program to create a lambda function that adds 15 to
# a given number passed in as an argument,also create a lambda function that multiplies argument a with argument b and print the result.

l = lambda n : n + 15
print(l(5))
l = lambda x,y : x * y
print(l(20,10))

#write a python program to find numbers divisible by nineteen or thirteen from a list of numbers using lambda
numbers = [121,65,86,228,26,39,32,152,77]
print("original list:")
print(numbers)
result = list(filter(lambda x:(x % 19 == 0 or x % 13 == 0), numbers))
print("numbers are divisible by nineteen or  thirteen:")
print (result)