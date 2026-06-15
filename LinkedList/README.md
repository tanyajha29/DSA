# LinkedList

Placement-focused revision notes for LinkedList.

## Problems

<!-- AUTO-GENERATED START -->

### 142. Linked List Cycle Ii (Medium)

🔗 LeetCode Folder: [`142-linked-list-cycle-ii`](../142-linked-list-cycle-ii)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

            # 1. detect cycle
            if slow == fast :
                slow = head

                # 2. find cycle start
                while slow != fast :
                    slow = slow.next
                    fast = fast.next 
                return slow
        return None
```

### 203. Remove Linked List Elements (Easy)

🔗 LeetCode Folder: [`203-remove-linked-list-elements`](../203-remove-linked-list-elements)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
       dummy = ListNode(0)
       dummy.next = head
       curr = dummy

       while curr and curr.next :
        # remove the node
        if curr.next.val == val :
            curr.next = curr.next.next
        else :
            curr = curr.next
       return dummy.next
```

### 237. Delete Node In A Linked List (Medium)

🔗 LeetCode Folder: [`237-delete-node-in-a-linked-list`](../237-delete-node-in-a-linked-list)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
```

### 328. Odd Even Linked List (Medium)

🔗 LeetCode Folder: [`328-odd-even-linked-list`](../328-odd-even-linked-list)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution:
    def oddEvenList(self, head):

        if not head or not head.next:
            return head

        odd = head
        even = head.next

        # save even list start
        even_head = even

        while even and even.next:

            # connect odd nodes
            odd.next = even.next
            odd = odd.next

            # connect even nodes
            even.next = odd.next
            even = even.next

        # attach even list after odd list
        odd.next = even_head

        return head
```

### 382. Linked List Random Node (Medium)

🔗 LeetCode Folder: [`382-linked-list-random-node`](../382-linked-list-random-node)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
import random

class Solution(object):

    def __init__(self, head):

        self.values = []

        curr = head

        # store all node values
        while curr:

            self.values.append(curr.val)

            curr = curr.next

    def getRandom(self):

        return random.choice(self.values)
```

### 528. Swapping Nodes In A Linked List (Medium)

🔗 LeetCode Folder: [`528-swapping-nodes-in-a-linked-list`](../528-swapping-nodes-in-a-linked-list)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        fast = head 
        slow = head

        # move fast to the kth position from the beginning
        for i in range(k - 1) :
            fast = fast.next
        
        # store the kth element
        first = fast

        # move fast and slow until end
        # the slow will be at the kth position form the end
        while fast.next :
            slow = slow.next
            fast = fast.next

        # swap the nodes
        first.val, slow.val = slow.val, first.val

        return head
```

### 725. Split Linked List In Parts (Medium)

🔗 LeetCode Folder: [`725-split-linked-list-in-parts`](../725-split-linked-list-in-parts)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        curr = head
        len = 0

        # find the length of the node
        while curr :
            len += 1
            curr = curr.next
        
        # calculate the length
        base_size = len // k
        extra = len % k

        curr = head
        results = []


        for i in range(k) :
            temp_head = curr

            # current part size
            current_size = base_size
            
            if extra > 0 :
                current_size +=1
                extra -= 1
            
            # move to last node od current
            for j in range(current_size - 1) :
                if curr :
                    curr = curr.next
            
            # Cut linked list after required nodes.
            if curr :
                next_part = curr.next
                curr.next = None
                curr = next_part
            
            results.append(temp_head)
        return results
```

### 835. Linked List Components (Medium)

🔗 LeetCode Folder: [`835-linked-list-components`](../835-linked-list-components)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        curr = head
        count = 0

        # set to store and check the connected components
        result_set = set(nums)

        while curr :
            # current node belongs to nums
            if curr.val in result_set :

                # end of cennected nodes
                if curr.next is None or curr.next.val not in result_set :
                    count += 1
            
            curr = curr.next
        
        return count
```

### 908. Middle Of The Linked List (Easy)

🔗 LeetCode Folder: [`908-middle-of-the-linked-list`](../908-middle-of-the-linked-list)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        # 2 pointers
        # 1 (slow) moves 1 step at a time
        # 2 (fast) moves 2 step at a time

        fast = head
        slow = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        # the slow pointer will end up at the middle only 
        # return slow
        return slow
```

### 2573. Remove Nodes From Linked List (Medium)

🔗 LeetCode Folder: [`2573-remove-nodes-from-linked-list`](../2573-remove-nodes-from-linked-list)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        prev = None
        curr = head

        # reverse the linked list
        while curr :
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head = prev
        max_seen = head.val
        curr = head

        # check and remove the smaller node
        while curr and curr.next :
            if curr.next.val < max_seen :
                curr.next = curr.next.next
                
            else :
                curr = curr.next
                max_seen = curr.val

        # reverse the linked list back

        prev = None
        curr = head
        while curr :
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return  prev
```

<!-- AUTO-GENERATED END -->
