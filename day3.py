'''
1. Write a program that grades students based on marks A, B, C, D and F
'''
marks = int(input ('Enter your total marks out of 100: '))
if(marks >= 80):
    print('Your Grade is A')
elif(marks >= 70 ):
    print('Your Grade is B')
elif(marks >= 60 ):
    print('Your Grade is C')
elif(marks >= 50 ):
    print('Your Grade is D')
else:
    print('Your Grade is F')

'''
2. Write a program that checks whether the number entered by a user is even or odd.
'''
number = int(input('Enter a number: '))
if(number % 2 == 0):
    print("Number you entered is Even ")
else:
    print("Number you entered is Odd ")

'''
3. Write a program that checks the greatest of 3 numbers entered by the user.
'''
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
if(number1 >= number2 and number1 >= number3):
    print('The greatest of 3 numbers is first number: ', number1)
elif(number2 >= number3):
    print('The greatest of 3 numbers is second number: ', number2)
else:
    print('The greatest of 3 numbers is third number: ', number3)
    
    
'''
4. Write a program that checks the greatest of 4 numbers entered by the user.
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
if(num1 >= num2 and num1 >= num3 and num1 >= num4 ):
    print('The greatest of 4 numbers is first number: ', num1)
elif(num2 >= num3 and num2 >= num4):
    print('The greatest of 4 numbers is second number: ', num2)
elif(num3 >= num4):
    print('The greatest of 4 numbers is third number: ', num3)
else:
    print('The greatest of 4 numbers is fourth number: ', num4)


'''
5. Write a program that checks whether the number is a multiple of 7 or not.
'''
number7 = int(input ("Enter any number: "))
if(number7 % 7 == 0):
    print("The number",number7 ,"is a multiple of 7")
else:
    print("The number",number7 ,"is not a multiple of 7")
    
'''
6. Write a program to input 3 fav movies from the use and then enter it into a list.
'''
# 1st method
movie1 = input("Enter your fav movie/series no. 1: ")
movie2 = input("Enter your fav movie/series no. 2: ")
movie3 = input("Enter your fav movie/series no. 3: ")
fav = [movie1, movie2, movie3 ]
print(fav)

# 2nd method
movies = []
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

# 3rd method 
movie = []
movie.append(movie1 = input("Enter your fav movie/series no. 1: "))
movie.append(movie2 = input("Enter your fav movie/series no. 2: "))
movie.append(movie3 = input("Enter your fav movie/series no. 3: "))
print(movie)

'''
7. Write a program to check that a list contain palindrome or not.
'''
# palindrome sentence => Borrow or rob?
list1 = ['b','o','r','r','o','w','o','r','r','o','b']
# list1 = [1,2,3,4,3,2,1]
list_copy = list1.copy()
list_copy.reverse()
if (list1 == list_copy ) :
    print("Yes, It's a vaild palendrome.")
else:
    print("Not a palendrome")