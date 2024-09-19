# print number from 1 to 100
i = 1
while(i<=100):
    print(i)
    i +=1
    
# print number from 100 to 1
i = 100
while(i<=1):
    print(i)
    i -=1
    
# print the multiple of a number n 
i = 1
n = 3
while(i<=10):
    print(i*n)
    i += 1
    
# print the table of number user input
i = 1
n = int(input("Enter a number = "))
while(i<=10):
    m = i*n 
    print(i,"*",n,"=",m)
    i += 1    

# print the element of the list 
list1 = ["ayesha","iqra","kalsoom","mahreen"]
idx = 0
while(idx<len(list1)):
    print(list1[idx])
    idx +=1 
    
# search for a number in a tuple 
tup = (1,2,5,6,3,8,4,9,2,13,11,10,11)
index = 0
while(index<len(tup)):
    print(tup[index])
    index += 1