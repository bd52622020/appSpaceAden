# 1
# dict={"Sedan": 1500,"SUV": 2000,"Pickup": 2500,"Minivan": 1600,"Van": 2400,"Semi": 13600,"Bicycle": 7,"Motorcycle": 110}
# list = [i.upper() for i in dict if dict[i]<5000]
# print (list)

#2
# list1=[4, 6, 3, 9, 10, 19]
# list2 = list(map(lambda x: x**2, list1))
# print (list2)

#3
if __name__ == '__main__':
    
    birthdays = {
        'mohamed adan': '10/1/1994',
        'jack howley': '11/2/1974',
        'stacey brown': '29/12/1982',
        'ali jay': '01/2/1999'}
    
    for name in birthdays:
        print(name)
        
    print ('name')
    name = input()
    if name in birthdays:
        print ('{}\'s birthday is {}.'.format(name,birthdays[name]))
    else:
        print('no such name'.formate(name))
        