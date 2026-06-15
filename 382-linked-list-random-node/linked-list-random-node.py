import random

class Solution(object):

    def __init__(self, head):

        self.values = []

        curr = head

        # store all node values
        while curr:

            self.values.append(curr.val)

            curr = curr.next

    def getRandom(self):

        return random.choice(self.values)