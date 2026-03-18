# LinkedList

Placement-focused revision notes for LinkedList.

## Problems

<!-- AUTO-GENERATED START -->

### 2. Add Two Numbers (Medium)

🔗 LeetCode Folder: [`2-add-two-numbers`](../2-add-two-numbers)

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

🔗 LeetCode Folder: [`19-remove-nth-node-from-end-of-list`](../19-remove-nth-node-from-end-of-list)

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

🔗 LeetCode Folder: [`21-merge-two-sorted-lists`](../21-merge-two-sorted-lists)

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

### 141. Linked List Cycle (Easy)

🔗 LeetCode Folder: [`141-linked-list-cycle`](../141-linked-list-cycle)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next==null) return false;

        ListNode slow=head;
        ListNode fast=head;

        while(fast!=null&& fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;

            if(slow== fast) return true;
        }
        return false;

        
    }
}
```

### 143. Reorder List (Medium)

🔗 LeetCode Folder: [`143-reorder-list`](../143-reorder-list)

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
