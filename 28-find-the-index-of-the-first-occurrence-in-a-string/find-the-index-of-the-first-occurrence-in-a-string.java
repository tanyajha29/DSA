//using haystack

class Solution {
    
    public int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }
}


/*class Solution {
    // 1. Changed method name from 'find' to 'strStr' to match the Driver
    public int strStr(String haystack, String needle) {

        if (needle.length() == 0) return 0;

        // 2. Added <= so you don't skip the very last possible match position
        for (int j = 0; j <= haystack.length() - needle.length(); j++) {
            int i = 0;

            // 3. Use .length() and .charAt() for Strings
            while (i < needle.length() && haystack.charAt(j + i) == needle.charAt(i)) {
                i++;
            }

            // 4. Return 'j' (the starting index), not 'i' (the length of the match)
            if (i == needle.length()) return j;
        }
        return -1;
    }
}*/