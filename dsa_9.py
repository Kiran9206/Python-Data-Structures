# Bit_Manipulation

# Q7. Add Binary Strings
'''
Problem Description
Given two binary strings A and B. Return their sum (also a binary string).

Problem Constraints
1 <= length of A <= 105
1 <= length of B <= 105
A and B are binary strings

Input Format
The two argument A and B are binary strings.
Output Format
Return a binary string denoting the sum of A and B

Example Input
Input 1:
A = "100"
B = "11"
Input 2:
A = "110"
B = "10"
Example Output
Output 1:
"111"
Output 2:
"1000"

Example Explanation
For Input 1:
The sum of 100 and 11 is 111.
For Input 2:
The sum of 110 and 10 is 1000.
'''

def addBinary(A,B):
    out='';carry_forward =0
    if len(A) > len(B):
        deff = len(A) - len(B)
        deff*='0'
        B = deff + B
    elif len(A) < len(B):
        deff = len(B) - len(A)
        deff*='0'
        A = deff + A
    for index in range(len(A)-1,-1,-1):
        Sum  = int(A[index]) + int(B[index]) + carry_forward
        carry_forward = Sum // 2
        digit = Sum % 2
        if index == 0 and carry_forward>0:
            out = str(carry_forward)+ str(digit) + out
        else: out = str(digit) + out
    return out 

'''
A = "1010110111001101101000"
B = "1000011011000000111100110"
# A = "110"
# B = "10"
print(addBinary(A,B))
'''

print(ord('a'))
        