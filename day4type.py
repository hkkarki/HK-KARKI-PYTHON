a=5
print(type(a))

a= "hello"
print(type(a))

 # print(int(a))

b= True
print(type(b))

# isinstance

a= "22"
print(isinstance(a,int))
print(isinstance(a, str))


test1="hello"
test2="from broadway"
test3 = 2222
test4=2222


# hello from broadway 2222

print(test1, test2, test3)

# print(test1+test2+test3)
print(test1+" "+test2+" "+str(test3))

# string formatting 'f'

print(f'{test1} {test2} {test3+test4}')



# python string

test= "hello"
print(test.upper())
print(test.lower())
print(test.title())
print(test.count("l"))

