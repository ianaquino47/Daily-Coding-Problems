# This problem was asked by Google.

# Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

def merge(lists):
    new_head = current = Node(-1)
    heap = [(lst.val, i) for i, lst in enumerate(lists)]
    heapq.heapify(heap)
    while heap:
        current_min, i = heapq.heappop(heap)
        # Add next min to merged linked list.
        current.next = Node(current_min)
        current = current.next
        # Add next value to heap.
        if lists[i] is not None:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next
    return new_head.next