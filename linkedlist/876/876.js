//two pointers technique. Fast pointer travels twice as fast as the slow pointer, and when the fast pointer reaches the end the slower pointer is in the middle.
var middleNode = function(head) {
  let slow = (fast = head);
  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
  }

  return slow;
};
