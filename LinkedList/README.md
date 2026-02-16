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

### 234. Palindrome Linked List (Easy)

🔗 LeetCode Folder: [`234-palindrome-linked-list`](../234-palindrome-linked-list)

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
    public boolean isPalindrome(ListNode head) {
        if(head==null || head.next==null) return true;

        ListNode slow=head;
        ListNode fast=head;

        //find middle

        while(fast!=null&& fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }

        //reverse 

        ListNode curr=slow;
        ListNode prev=null;

        while(curr!=null){
            ListNode nextTemp=curr.next;
            curr.next=prev;
            prev=curr;
            curr=nextTemp;
        }

        //compare

        ListNode first=head;
        ListNode second=prev;

        while(second!=null){
            if(first.val != second.val)
            return false;

            first=first.next;
            second=second.next;
        }
        return true;
    }
}
```

<!-- AUTO-GENERATED END -->
