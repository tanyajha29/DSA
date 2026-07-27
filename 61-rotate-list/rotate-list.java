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
    public ListNode rotateRight(ListNode head, int k) {

        if(head == null || head.next == null || k == 0){
            return head;
        }
        // 1. find the length of the list
        int length = 1;
        ListNode tail = head;

        while(tail.next != null){
            tail = tail.next;
            length++;
        }

        // 2. avoid unnecessary rotations
        k = k % length;

        if(k == 0){
            return head;
        }

        // 3. make the list circular
        tail.next = head;

        // 4. find new tail
        int steps = length - k - 1;
        ListNode newTail = head;

        for(int i = 0; i < steps; i++){
            newTail = newTail.next;
        }

        // 5. find new head
        ListNode newHead = newTail.next;

        // 6. break the node
        newTail.next = null;

        return newHead;
    }
}