
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# front->middle->rear
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        if self.front and self.rear:
            return True
        else:
            return False

    def enqueue(self, item):
        if not self.front:
            self.front = Node(item,None)
            self.rear = self.front
        else:
            self.rear.next = Node(item,None)
            # update our rear 
            self.rear = self.rear.next
            
    def dequeue(self):
        if self.is_empty():
            return None
        
        dummy = self.front
        self.front = self.front.next 
        return dummy
      
    def peek(self):
        if self.front and self.rear:
            return self.front.val
        else:
            return None
    


# Create a new Queue
q = Queue()

# Add elements to the queue
q.enqueue(('Love Song', 'Sara Bareilles'))
q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
q.enqueue(('Hug from a Dinosaur', 'Torres'))
print_queue(q)

# View the front element
print("Peek: ", q.peek()) 

# Remove elements from the queue
print("Dequeue: ", q.dequeue()) 
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty: ", q.is_empty()) 

# Remove the last element
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty:", q.is_empty()) 
