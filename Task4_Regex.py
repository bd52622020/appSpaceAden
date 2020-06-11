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


data=f.readlines()
print(data[0])
