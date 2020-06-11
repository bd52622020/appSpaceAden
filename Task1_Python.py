#how many words

f = open ("Shakespeare.txt")
test_string = f.read()
res = len(test_string.split())

print ("The number of words in shakespeare" , str (res))


#how many lines
f = open("Shakespeare.txt")
def Check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    print(len(final)) 
     
      

string = f.read()
vowels = "AaEeIiOoUu"

Check_Vow(string, vowels); 

# how many numbers

f = open ("Shakespeare.txt","r")
total_numbers = 0
for line in f :
   parts = line.split()
   total_numbers += len(parts)
print (total_numbers)

# read a string from standard input reverse input print the string and the reverse string

x = input('enter string')
print('Hello, ' + x)

s = input("Enter a string: ")
print (s[::-1])

# extract the third column and replace the errors ("," "*" with hyphen (-)

import regex as re
outfile="out.csv"

f = open ("phoneNumbers.txt")

data=f.read()
lines=data.splitlines()


with open(outfile, 'w') as file:
  for line in lines:
    number = line[-12:]
    print(number)
    x = re.sub("[*,]", "-", number)
    print(x)
    file.write(x+"\n")