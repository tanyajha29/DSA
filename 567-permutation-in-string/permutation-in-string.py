from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_len = Counter()
        # points to start of window
        left = 0

        for right in range (len(s2)):
            # add element in the window
            window_len[s2[right]] += 1

            # check window size 
            if right - left + 1 > len(s1):
                window_len[s2[left]] -= 1

                # delete the less frequency element
                if window_len[s2[left]] == 0:
                    del window_len[s2[left]]
                left += 1

            if window_len == s1_count:
                return True
        return False