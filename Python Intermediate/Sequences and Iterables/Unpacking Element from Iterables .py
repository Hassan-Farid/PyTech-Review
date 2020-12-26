'''
Assume an N-valued tuple or sequence, this script unpacks the values from such tuples/sequences into variables
'''

# If the number of values in the tuple is small and known
seq = (2,'Jack',4,5,67,'Hello') 

#Assign N number of varaibles and use assignment operator to assign values to them
a,b,c,x,y,z = seq
print(b)

#This technique works not only on tuples but on every type of sequence
seq = [2,'Jack',4,5,67, 'Hello']
a,b,c,x,y,z = seq
print(x)

seq = 'Hello!'
a,b,c,x,y,z = seq
print(c)

# Now if the number of values in the tuple are too many such that it is hard to unpack using assignment operator
# For such a case, we can use star unpacking i.e. use of * operator

#Suppose we are given a list of marks of assignment submitted by the students and we want to find the average marks obtained
#by the first 10 students who submitted the assignment
seq = [12,43,50,32,44,23,45,31,20,9,14,20,42]
*early, stud1, stud2, stud3 = seq
avg_marks = sum(early)/len(seq)
print(avg_marks)

#Star-unpacking can also be used in case we want to perform one function over another in terms of parameters
#Suppose the program is fed to a machine that uses the tags stored in the provided tuple/sequence to apply different functions
#If the tag is 'add' then it adds all the parameters and if the tag is 'mul' it multiplies all the numbers
def mul(*args):
    import numpy as np
    return np.prod(np.array(args))    


seqs = [('add',2,3),('mul',4,15,32),('add',2,7,8,9,13)]

for tags, *args in seqs:
    if tags == 'add':
        print(sum(args))
    elif tags == 'mul':
        print(mul(args))