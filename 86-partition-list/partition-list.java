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
    public ListNode partition(ListNode head, int x) {
        // use 2 dummy Lists to store the small and large list
        ListNode dummySmall = new ListNode(0);
        ListNode dummyLarge = new ListNode(0);

        ListNode Small = dummySmall;
        ListNode Large = dummyLarge;

        while(head != null){
            if(head.val < x){
                Small.next = head;
                Small = Small.next;
            }
            else{
                Large.next = head;
                Large = Large.next;
            }
            head = head.next;
        }

        Large.next = null;

        Small.next = dummyLarge.next;

        return dummySmall.next;
    }
}