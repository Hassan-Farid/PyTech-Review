'''
    Sometimes a single loop is not enough for the application we have to peform, thus, we need to use loops within loops
    This use of loops within loops is known as Nested Looping and is quite used in application development
'''

#Using nested looping to find a palindrome
text = "level"
isPalindrome = False
for i in range(len(text)): #Starts checking characters of text from beginning
    for j in range(len(text) - i - 1, -1, -1): #Starts checking characters of text from the end
        if text[i] == text[j]:
            isPalindrome = True #Is assigned True for every match
        else:
            isPalindrome = False #Is assigned False for every non-match

print("Is {} a palindrome: {}".format(text, isPalindrome))

#Using nested looping to perform matrix multiplication
A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[9,8,7], [6,5,4], [3,2,1]]
C = [[0] * len(B[0])] * len(A) #The matrix yielded as a product has rows equal to first matrix and columns equal to second matric

for i in range(len(A)): #Looping for the rows of the first matrix
    for j in range(len(B[0])): #Looping for the columns of the second matrix
        for k in range(len(C)): #Looping for the length of the resulting matrix
            C[i][j] += A[i][k] * B[k][j]

print(C)

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a program that uses nested looping to sort elements of a list

Enter the elements of a list (seperated by commas): ___________________ (Input comes in blank)

Once the input has been entered, the program should return the inputted list in sorted order:

Enter the elements of a list: 4,5,11,7,16,3,14,19
Sorted List: [3,4,5,7,11,14,16,19] 

'''