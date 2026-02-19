# LinkedList

Placement-focused revision notes for LinkedList.

## Problems

<!-- AUTO-GENERATED START -->

### 92. Reverse Linked List Ii (Medium)

🔗 LeetCode Folder: [`92-reverse-linked-list-ii`](../92-reverse-linked-list-ii)

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
    public ListNode reverseBetween(ListNode head, int left, int right) {

        //check if listnode is empty
        if(head==null|| left==right) return head;

        ListNode dummy=new ListNode();
        dummy.next=head;

        ListNode prev=dummy;

        //move prev till left
        for(int i= 1;i<left; i++){
            prev=prev.next;
        }

        //move current next to prev
        ListNode curr=prev.next;

        //itetrate right-left times and reverse
        for (int i=0; i<right-left;i++){
            ListNode nextTemp=curr.next;

            curr.next=nextTemp.next;
            nextTemp.next=prev.next;
            prev.next=nextTemp;
        }
        return dummy.next;
        
    }
}
```

<!-- AUTO-GENERATED END -->
