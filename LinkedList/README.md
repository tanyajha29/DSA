# LinkedList

Placement-focused revision notes for LinkedList.

## Problems

<!-- AUTO-GENERATED START -->

### 206. Reverse Linked List (Easy)

🔗 LeetCode Folder: [`206-reverse-linked-list`](../206-reverse-linked-list)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        //dummy.next=head;
        ListNode prev=null;
        ListNode curr=head;

        while(curr !=null){
            ListNode nextTemp=curr.next;
            curr.next=prev;
            prev=curr;
            curr=nextTemp;
        }
        return prev;
        
    }
}
```

<!-- AUTO-GENERATED END -->
