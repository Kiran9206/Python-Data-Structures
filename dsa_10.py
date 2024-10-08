# Strings

# Q1. Toggle Case
'''
Problem Description
You are given a character string A having length N, consisting of only lowercase and uppercase latin letters.
You have to toggle case of each character of string A. For e.g 'A' is changed to 'a', 'e' is changed to 'E', etc.
Problem Constraints
1 <= N <= 105
A[i] ∈ ['a'-'z', 'A'-'Z']

Input Format
First and only argument is a character string A.
Output Format
Return a character string.

Example Input
Input 1:
 A = "Hello" 
Input 2:
 A = "tHiSiSaStRiNg" 

Example Output
Output 1:
 hELLO 
Output 2:
 ThIsIsAsTrInG 

Example Explanation
Explanation 1:
 'H' changes to 'h'
 'e' changes to 'E'
 'l' changes to 'L'
 'l' changes to 'L'
 'o' changes to 'O'
Explanation 2:
 "tHiSiSaStRiNg" changes to "ThIsIsAsTrInG".
 '''

def toggleCase(A):
    arr = []
    for Char in A:
        if (ord(Char) >= 65 and ord(Char) <= 90):
            arr.append(chr(ord(Char)+32))
        elif (ord(Char) >= 97 and ord(Char) <= 122):
            arr.append(chr(ord(Char)-32))
        else: arr.append(Char)
    return ''.join(arr)
'''
A = "Hello" 
A = "tHiSiSaStRiNg" 
print(toggleCase(A))
'''

# ---------------------------------------------------------------------------------------

# Q2. Simple Reverse
'''
Problem Description
Given a string A, you are asked to reverse the string and return the reversed string.

Problem Constraints
1 <= |A| <= 105
String A consist only of lowercase characters.

Input Format
First and only argument is a string A.
Output Format
Return a string denoting the reversed string.
Example Input
Input 1:
 A = "scaler"
Input 2:
 A = "academy"

Example Output
Output 1:
 "relacs"
Output 2:
 "ymedaca"

Example Explanation
Explanation 1:
Reverse the given string.
'''

def simpleReverse(A):
    A = A[::-1]
    return A

'''
A = "scaler"
A = "academy"
print(simpleReverse(A))
'''

# --------------------------------------------------------------------------------------------------------------------
# Q3. Reverse the String
'''
Problem Description
You are given a string A of size N.
Return the string A after reversing the string word by word.
NOTE:
A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.

Problem Constraints
1 <= N <= 3 * 105

Input Format
The only argument given is string A.
Output Format
Return the string A after reversing the string word by word.

Example Input
Input 1:
A = "the sky is blue"
Input 2:
A = "this is ib"
Example Output
Output 1:
"blue is sky the"
Output 2:
"ib is this"    

Example Explanation
Explanation 1:
We reverse the string word by word so the string becomes "blue is sky the".
Explanation 2:
We reverse the string word by word so the string becomes "ib is this".
'''

def reverseWords(A):
    arr = A.split(" ")
    arr = arr[::-1]
    return ' '.join(arr).strip()
'''
A = "the sky is blue"
print(reverseWords(A))
'''
# ---------------------------------------------------------------------------------------------
# Q4. Longest Palindromic Substring
'''
Problem Description
Given a string A of size N, find and return the longest palindromic substring in A.
Substring of string A is A[i...j] where 0 <= i <= j < len(A)
Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
Incase of conflict, return the substring which occurs first ( with the least starting index).

Problem Constraints
1 <= N <= 6000

Input Format
First and only argument is a string A.
Output Format
Return a string denoting the longest palindromic substring of string A.

Example Input
Input 1:
A = "aaaabaaa"
Input 2:
A = "abba
Example Output
Output 1:
"aaabaaa"
Output 2:
"abba"

Example Explanation
Explanation 1:
We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".
Explanation 2:
We can see that longest palindromic substring is of length 4 and the string is "abba".
'''

def palindrome(A,s,e):
    while (s<e):
        if (A[s]!=A[e]):
            return 0
        else: s+=1; e-=1
    return 1

def longestPalindrome(A): #brute force approch #Space complexity = O(1),    Time Complexity = O(n^3)
    ans = s = e = 0
    for start in range(len(A)):
        for end in range(start,len(A)):
            if palindrome(A,start,end):
                if ans < (end-start+1):
                    ans = (end-start+1)
                    s = start;e=end
    return A[s:e+1]

def longestPalindrome1(A): #Otimized code..... #Space complexity = O(1),    Time Complexity = O(n^2)>> n^2 + n^2 >> 2n^2>> (n^2)
    ans=s=e=0
    for index in range(len(A)):
        L=R=index
        #odd palindrome....
        while(L>=0 and R<len(A)):
            if A[L] != A[R]:
                break
            L-=1; R+=1
        if ans < (R-L-1):
            ans = R-L-1
            s = L+1; e=R
    for index  in range(len(A)):
        L=index; R = index+1
        while(L>=0 and R<len(A)): #even palindrome....
            if A[L] != A[R]:
                break
            L-=1; R+=1
        if ans < (R-L-1):
            ans = R-L-1
            s = L+1; e=R
    return A[s:e+1]    
'''
A = "aaaabaaa"
A = "abb"
print(longestPalindrome1(A))
'''


# ----------------------------------------------------------------------------------------------------------------------

# Q1. Longest Common Prefix
'''
Problem Description
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.
The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Problem Constraints
0 <= sum of length of all strings <= 1000000

Input Format
The only argument given is an array of strings A.
Output Format
Return the longest common prefix of all strings in A.

Example Input
Input 1:
A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2:
A = ["abab", "ab", "abcd"];

Example Output
Output 1:
"a"
Output 2:
"ab"

Example Explanation
Explanation 1:
Longest common prefix of all the strings is "a".
Explanation 2:
Longest common prefix of all the strings is "ab".
'''

def commonPrefix(A): #pending....................................
    m = 10**9
    for index in range(len(A)):
        m = min(m,len(A[index]))
    arr = []
    for index in range(m):
        count = 0
        ch = A[0][index]
        for index1 in range(len(A)):
            if ch == A[index1][index]:
                count+=1
        if count == len(A):
            arr.append(ch)            
    return ''.join(arr)

A = ["abcdefgh", "aefghijk", "abcefgh"]
A = ["abab", "ab", "abcd"]
print(commonPrefix(A))
# -------------------------------------------------------------------------------------------------------------------------------

# Q2. Count Occurrences
'''
Problem Description
Find the number of occurrences of bob in string A consisting of lowercase English alphabets.

Problem Constraints
1 <= |A| <= 1000

Input Format
The first and only argument contains the string A, consisting of lowercase English alphabets.
Output Format
Return an integer containing the answer.

Example Input
Input 1:
  "abobc"
Input 2:
  "bobob"
Example Output
Output 1:
  1
Output 2:
  2
Example Explanation
Explanation 1:
  The only occurrence is at second position.
Explanation 2:
Bob occures at first and third position.
'''
def occurences(A):
    # res  = A.count('bob')
    s =0; ans =0
    while s<len(A):
        if A[s:s+3] == 'bob':
            ans+=1
        s+=1;
    return ans
'''
A = "abobc"
A = "bobob"
print(occurences(A))
'''
# ----------------------------------------------------------------------------------------------------------
# Q3. Amazing Subarrays

'''
You are given a string S, and you have to find all the amazing substrings of S.
An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
Input
Only argument given is string S.
Output
Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.
Constraints
1 <= length(S) <= 1e6
S can have special characters
Example
Input
    ABEC
Output
    6
Explanation
    Amazing substrings of given string are :
    1. A
    2. AB
    3. ABE
    4. ABEC
    5. E
    6. EC
    here number of substrings are 6 and 6 % 10003 = 6.
Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
'''
def amazingSubarrays(A):
    Count = 0;modulo = 10003;
    vowel = ['a', 'e', 'i', 'o', 'u' , 'A' , 'E' , 'I', 'O', 'U']
    for index, char in enumerate(A):
        if char in vowel:
            Count+=(len(A)-index)
    if Count >= modulo:
        Count%=modulo
    return Count
'''
A = 'ABEC'
print(amazingSubarrays(A))
'''
# --------------------------------------------------------------------------------------------
# Q4. Isalnum()
'''
Problem Description
You are given a function isalpha() consisting of a character array A.
Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.

Problem Constraints
1 <= |A| <= 105

Input Format
Only argument is a character array A.
Output Format
Return 1 if all the characters of the character array are alphanumeric (a-z, A-Z and 0-9), else return 0.

Example Input
Input 1:
 A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
Input 2:
 A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 All the characters are alphanumeric.
Explanation 2:
 All the characters are NOT alphabets i.e ('#').

'''
def isAlnum(A): #Space complexity = O(1),    Time Complexity = O(N)
    for char in A:
        if ord(char) >= ord('A') and ord(char) <= ord('Z'):
            continue
        elif ord(char) >= ord('a') and ord(char) <= ord('z'):
            continue 
        elif ord(char) >= ord('0') and ord(char) <= ord('9'):
            continue
        else: return 0
    return 1

'''
# A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']
A = ['S','c','a','l','e','r','A','c','a','d','e','m','y','2','0','2','0']
print(isAlnum(A))
'''

# ------------------------------------------------------------------------------------------------------------------------------
