# LinkedList

Placement-focused revision notes for LinkedList.

## Problems

<!-- AUTO-GENERATED START -->

### 2871. Double A Number Represented As A Linked List (Medium)

🔗 LeetCode Folder: [`2871-double-a-number-represented-as-a-linked-list`](../2871-double-a-number-represented-as-a-linked-list)

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
    public ListNode doubleIt(ListNode head) {
        if(head.val > 4){
            head = new ListNode(0, head);
        }

        ListNode curr = head;

        while(curr != null){
            curr.val = (curr.val * 2) % 10;

            if(curr.next != null && curr.next.val > 4){
                curr.val++;
            }

            curr = curr.next;
        }
        return head;
    }
}
```

<!-- AUTO-GENERATED END -->
