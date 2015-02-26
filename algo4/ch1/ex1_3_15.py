from queue import Queue

def main():
    q = Queue()
    k = int(raw_input())
    count = 0
    while True:
    	item = raw_input()
    	if item == "-1":
    		break
    	q.enqueue(item)
    	count += 1
    print count,k
    for i in range(count):
    	item = q.dequeue()
    	if i == (count - k):
    		print item
main()