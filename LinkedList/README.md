# LinkedList

Placement-focused revision notes for LinkedList.

## Problems

<!-- AUTO-GENERATED START -->

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

<!-- AUTO-GENERATED END -->
