#Use the deque FIFO, first in, first out. I.e if ["lisa", "olle", "pelle"] is in the list, then use pop left so that "lisa" is first to leave the queue.

#1. Generate a list with 50 names
from collections import deque
from random import choices, shuffle
from random import randint

names=["lisa", "olle", "pelle", "Adam", "Bertil", "Caesar", "David", "Erik", "Filip", "Gustav", "Helge", "Ivar", "Johan"]
names=choices(names, k=50)
print(names)
#2. Create a Queue `deque` with a maximum length of 10

queue=deque(maxlen=10)

while len(queue) > 10: 
    (queue.popleft())  
print(queue)
#3. Let random number of person leave the queue

#4. When the random number of persons has left the queue, fill the missing spots
#5. Iterate until all 50 has gone through the queue
