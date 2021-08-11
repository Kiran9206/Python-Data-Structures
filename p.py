
import collections #and also Queue module int that we use for push is put and pop is get and also we want mention a time limit for showing an error
stack = collections.deque()
def push():
    if len(stack)==n:
        print("The stack is full!")
    else:
        for i in range(n):
            u = int (input("Enter the element : "))
            a = stack.append(u)
            print(stack)

def pop_element():
    if not stack:
        print("Stack is empty!")
    else:
        b=stack.pop()
        print(b)

n = int(input("How many elements do you want : "))   
while True:
    user = int (input("Enter Your Choice 1.push 2.pop 3.exit\n"))
    if user == 1:
        push()
    elif user == 2:
        pop_element()
    elif user == 3:
        break
    else :
        print("Enter correct choice!")
