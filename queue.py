

Queue = []
def push():
    if len(Queue)==n:
        print("The Queue is full!")
    else:
        for i in range(n):
            u = int (input("Enter the element : "))
            a = Queue.append(u)
            print(Queue)

def pop_element():
    if not Queue:
        print("Queue is empty!")
    else:
        b=Queue.pop(0)
        print(b)
def display():
    print(Queue)

n = int(input("How many elements do you want : "))   
while True:
    user = int (input("Enter Your Choice 1.push 2.pop 3.display 4.exit\n"))
    if user == 1:
        push()
    elif user == 2:
        pop_element()
    elif user == 3:
        display()
    elif user == 4:
        break
    else :
        print("Enter correct choice!")
