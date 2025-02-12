queue = []
front = -1
rear = -1
item = 0

def create():
    global front, rear, queue
    front = rear = 0
    print("    Creating Queue\n\n")
    for i in range(3):
        element = int(input("    Enter element: "))
        queue.append(element)
        rear += 1
    rear -= 1

def insertItem():
    global front, rear, queue, item
    if (front == 0 and rear == 3 - 1) or front == rear + 1:
        print("    OVERFLOW.")
    elif front == -1 and rear == -1:
        front = rear = 0
        item = int(input("    Enter an element: "))
        queue[rear] = item
    else:
        rear += 1
        item = int(input("    Enter an element: "))
        queue[rear] = item

def deleteItem():
    global front, rear, queue
    if front == -1 and rear == -1:
        print("    UNDERFLOW.")
    elif front == rear:
        print("    Deleted element is", queue[front])
        front = rear = -1
    else:
        print("    Deleted element is", queue[front])
        front += 1

def display():
    global front, rear, queue
    print("    Front element of the queue is", queue[front])
    print("    Rear element of the queue is", queue[rear])

    if front == -1 and rear == -1:
        print("    Queue is empty.")
        exit(0)
    else:
        i = front
        while i != rear:
            print("    ", queue[i], end=" ")
            i += 1
        print("    ", queue[rear])  # rear er age prjnto cholbe tai alada vabe rear print kora lagbe
        print()

if __name__ == '__main__':
    while True:
        print("    1. Create")
        print("    2. Insert")
        print("    3. Delete")
        print("    4. Display")
        print("    5. Exit")

        choice = int(input("    Enter your choice: "))
        print()

        if choice == 1:
            create()
        elif choice == 2:
            insertItem()
        elif choice == 3:
            deleteItem()
        elif choice == 4:
            display()
        elif choice == 5:
            print("    Program successfully exited...")
            exit(0)
        else:
            print("    Invalid choice. Please try again.\n")
