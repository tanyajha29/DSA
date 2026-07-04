# Others

Placement-focused revision notes for Others.

## Problems

<!-- AUTO-GENERATED START -->

### 125. Valid Palindrome (Easy)

🔗 LeetCode Folder: [`125-valid-palindrome`](../125-valid-palindrome)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right :
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum() :
                left += 1
            
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum() :
                right -= 1

            # compare and move forward
            if s[left].lower() != s[right].lower() :
                return False
            left += 1
            right -= 1
        return True
```

### 151. Reverse Words In A String (Medium)

🔗 LeetCode Folder: [`151-reverse-words-in-a-string`](../151-reverse-words-in-a-string)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def reverseWords(self, s):
        n = len(s) - 1
        result = ""
        while n >= 0 :
            while n >= 0 and s[n] == " " :
                n -= 1

            if n < 0 :
                break

            end = n
            while n >= 0 and s[n] != " " :
                n -= 1

            word = s[n + 1: end + 1]
            if result != "" :
                result += " "

            result += word

        return result
```

### 162. Find Peak Element (Medium)

🔗 LeetCode Folder: [`162-find-peak-element`](../162-find-peak-element)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        # base case 
        # if array has a single element
        if n == 1 :
            return 0
        
        # if 1st element is the peak
        elif nums[0] > nums[1] :
            return 0

        # if last element is the peak
        elif nums[n - 1] > nums[n - 2] :
            return(n - 1)
        
        # binary search
        low = 1
        high = n - 1

        while low <= high :
            mid = (low + high) // 2 
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1] :
                return mid
            elif nums[mid] > nums[mid - 1] :
                low = mid + 1
            else :
                high = mid - 1
        return -1
```

### 345. Reverse Vowels Of A String (Easy)

🔗 LeetCode Folder: [`345-reverse-vowels-of-a-string`](../345-reverse-vowels-of-a-string)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def reverseVowels(self, s):
        left = 0
        right = len(s) - 1
        s = list(s)
        vowels = set("aeiouAEIOU")

        while left < right :
            while left < right and s[left] not in vowels :
                left += 1
            
            while left < right and s[right] not in vowels :
                right -= 1

            s[right], s[left] = s[left], s[right]
            left += 1
            right -= 1

        return "".join(s)
```

### 409. Longest Palindrome (Easy)

🔗 LeetCode Folder: [`409-longest-palindrome`](../409-longest-palindrome)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):

        freq = Counter(s)
        ans = 0

        for i in freq.values() :
            ans += (i//2) * 2

        if ans < len(s) :
            ans += 1
        
        return ans
```

### 680. Valid Palindrome Ii (Easy)

🔗 LeetCode Folder: [`680-valid-palindrome-ii`](../680-valid-palindrome-ii)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    def validPalindrome(self, s):
        def check_after_skipping(left, right) :
            while left < right :
                if s[left] != s[right] :
                    return False
                left += 1
                right -= 1
            return True 

        left , right = 0, len(s) - 1
        while left < right :
            if s[left] != s[right] :
                return check_after_skipping(left + 1, right) or check_after_skipping(left, right - 1)
            left += 1
            right -= 1
        return True
```

### 907. Koko Eating Bananas (Medium)

🔗 LeetCode Folder: [`907-koko-eating-bananas`](../907-koko-eating-bananas)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # function to calculate hours
        def calculateHour( piles, speed) :
            hrs = 0
            for i in piles :
                hrs += math.ceil( i/speed )
            
            return hrs

        # binary Search
        high = max(piles)
        low = 1
        result = high
        
        while low <= high :
            mid = (low + high)//2
            total_hour = calculateHour(piles, mid)

            # check the hour value
            if total_hour <= h :
                result = mid
                high = mid - 1
            else :
                low = mid + 1
        return result
```

### 1408. Find The Smallest Divisor Given A Threshold (Medium)

🔗 LeetCode Folder: [`1408-find-the-smallest-divisor-given-a-threshold`](../1408-find-the-smallest-divisor-given-a-threshold)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
import math

class Solution:
    def find_sum(self, nums, m) :
        return sum(math.ceil(i/m) for i in nums)

    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if len(nums) > threshold :
            return -1

        low = 1
        high = max(nums)

        while low <= high :
            mid = (low + high)//2
            if (self.find_sum(nums, mid) <= threshold ) :
                high = mid - 1
            else :
                low = mid + 1
        
        return low
```

### 1605. Minimum Number Of Days To Make M Bouquets (Medium)

🔗 LeetCode Folder: [`1605-minimum-number-of-days-to-make-m-bouquets`](../1605-minimum-number-of-days-to-make-m-bouquets)

- **Pattern:** General
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
class Solution(object):
    # funtion to check if the blooming is possible or not
    def possible(self, arr,day, m, k) :
        count = 0
        bouquets_formed = 0

        for i in range(len(arr)) :
            if arr[i] <= day :
                count += 1
            else :
                bouquets_formed += count // k 
                count = 0
            # last count tweak
        bouquets_formed += (count // k )

        return bouquets_formed >= m 

    def minDays(self, bloomDay, m, k):
        # not enough / base case
        if m * k > len(bloomDay) :
            return -1
        
        # binary search
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while low <= high : 
            mid = (low + high)//2
            if self.possible(bloomDay, mid, m, k) :
                ans = mid
                high = mid - 1
            else: 
                low = mid + 1
        return ans
```

<!-- AUTO-GENERATED END -->
