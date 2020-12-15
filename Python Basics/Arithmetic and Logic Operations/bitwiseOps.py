'''
    Sometimes we need to apply bitwise operations on each bit of an integer
    This is more of a binary based operation which is needed in developing logic solving applications
'''

#Converting an integer into binary form (bits)
num = 25
bnum = bin(num)
print(bnum) #Neglect the 0b at the start as it is to represent the binary number

#To apply bitwise operations it not necessary to use above step, its just a representation of the integers in binary incase it is needed
#We now move to the bitwise operations in Python

#Bitwise OR operation (Applies OR operation on equivalent individual bits)
num1 = 2 #0b010
num2 = 6 #0b110
print("{0} OR {1} = {2}".format(bin(num1), bin(num2), bin(num1 | num2)))

#Bitwise AND operation (Applies AND operation on equivalent individual bits)
num1 = 2 #0b010
num2 = 6 #0b110
print("{0} AND {1} = {2}".format(bin(num1), bin(num2), bin(num1 & num2)))

#Bitwise NOT operation (Applies NOT operation on individual bits)
num = 6 #0b110
print("NOT {}".format(bin(~num)))

#Bitwise XOR operation (Applies XOR operation on individual bits)
num1 = 2 #0b010
num2 = 6 #b0110
print("{0} XOR {1} = {2}".format(bin(num1), bin(num2), bin(num1 ^ num2)))

#Bitwise Left Shift (Applies num2 left shift of bits on num1)
num1 = 29 #0b11101
num2 = 2
print("{0} shifted left by {1} bits gives {2}".format(bin(num1), num2, bin(num1 << num2)))

#Bitwise Right Shift (Applies num2 right shift of bits on num1)
num1 = 29 #0b11101
num2 = 2
print("{0} shifted right by {1} bits gives {2}".format(bin(num1), num2, bin(num1 >> num2)))

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a manual 2-bit truth table that computes the result of the logical expression Q = (~((A OR B) AND ~(A AND B)) OR (A AND B))
The output should look like this:

|A|B|Q|
|0|0|1|
|0|1|0|
|1|0|0|
|1|1|1|
'''