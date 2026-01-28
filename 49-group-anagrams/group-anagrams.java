class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        // Step 1: store original + sorted version
        String[][] arr = new String[strs.length][2];

        for (int i = 0; i < strs.length; i++) {
            char[] ch = strs[i].toCharArray();
            Arrays.sort(ch);
            arr[i][0] = strs[i];           // original
            arr[i][1] = new String(ch);    // sorted
        }

        // Step 2: sort based on sorted strings
        Arrays.sort(arr, (a, b) -> a[1].compareTo(b[1]));

        // Step 3: group adjacent anagrams
        List<List<String>> result = new ArrayList<>();

        for (int i = 0; i < arr.length; ) {
            List<String> group = new ArrayList<>();
            String key = arr[i][1];

            while (i < arr.length && arr[i][1].equals(key)) {
                group.add(arr[i][0]);
                i++;
            }

            result.add(group);
        }

        return result;
    }
}
