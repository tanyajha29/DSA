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
    public ListNode sortList(ListNode head) {
        // 1. Base Case
        if(head == null || head.next == null){
            return head;
        }

        // 2. Find Middle
        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;

        while(fast != null && fast.next != null){
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        // 3. Split the list into 2 halves
        if(prev != null){
            prev.next = null;
        }

        ListNode left = head;
        ListNode right = slow;

        ListNode sortedLeft = sortList(left);
        ListNode sortedRight = sortList(right);
        
        
        // 5. Merge the sorted halves
        return merge(sortedLeft, sortedRight);
    }

    // Merge Function
    public ListNode merge(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        while(l1 != null && l2 != null){
            if(l1.val <= l2.val){
                tail.next = l1;
                l1 = l1.next;
            }else{
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }
        if(l1 != null){
             tail.next = l1;
        }
        if(l2 != null){
             tail.next = l2;
        }

        return dummy.next;
    }
}