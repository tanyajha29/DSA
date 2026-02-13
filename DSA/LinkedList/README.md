# LinkedList

Placement-focused revision notes for LinkedList.

## Problems

<!-- AUTO-GENERATED START -->

### 2. Add Two Numbers (Medium)

🔗 LeetCode Folder: [`2-add-two-numbers`](../../2-add-two-numbers)

- **Pattern:** Linked List
- **Time Complexity:** O(m+n)
- **Space Complexity:** O(1)

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {

            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;

            int sum = x + y + carry;
            carry = sum / 10;

            curr.next = new ListNode(sum % 10);
            curr = curr.next;

            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        return dummy.next;
    }
}
```

### 19. Remove Nth Node From End Of List (Medium)

🔗 LeetCode Folder: [`19-remove-nth-node-from-end-of-list`](../../19-remove-nth-node-from-end-of-list)

- **Pattern:** Two Pointers
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

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
    public ListNode removeNthFromEnd(ListNode head, int n) {
       ListNode dummy=new ListNode();
       dummy.next= head;
       ListNode slow=dummy;
       ListNode fast=dummy;
       for(int i =0;i<=n;i++){
        fast=fast.next;
       }
       while(fast!=null){
        slow=slow.next;
        fast=fast.next;
       }
       slow.next=slow.next.next;
       return dummy.next;
    }
}
```

### 21. Merge Two Sorted Lists (Easy)

🔗 LeetCode Folder: [`21-merge-two-sorted-lists`](../../21-merge-two-sorted-lists)

- **Pattern:** Linked List
- **Time Complexity:** O(m+n)
- **Space Complexity:** O(1)

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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy=new ListNode(-1);
        ListNode current=dummy;
        while(list1 !=null && list2 !=null){
            if(list1.val<=list2.val){
                current.next=list1;
                list1= list1.next;
            }else{
                current.next=list2;
                list2= list2.next;
            }
            current=current.next;
        }
        current.next=(list1!=null)?list1:list2;
        return dummy.next;
    }
}
```

### 143. Reorder List (Medium)

🔗 LeetCode Folder: [`143-reorder-list`](../../143-reorder-list)

- **Pattern:** Reverse + Merge
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

```java
class Solution {
    public void reorderList(ListNode head) {

        if (head == null || head.next == null) return;

        // 1. Find middle
        ListNode slow = head;
        ListNode fast = head;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // 2. Reverse second half
        ListNode prev = null;
        ListNode curr = slow.next;

        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }

        slow.next = null; // break first half

        // 3. Merge two halves
        ListNode first = head;
        ListNode second = prev;

        while (second != null) {
            ListNode t1 = first.next;
            ListNode t2 = second.next;

            first.next = second;
            second.next = t1;

            first = t1;
            second = t2;
        }
    }
}
```

<!-- AUTO-GENERATED END -->
