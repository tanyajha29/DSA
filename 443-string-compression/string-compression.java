class Solution {
    public int compress(char[] chars) {
        int index = 0;
        int i = 0;

        while(i < chars.length){
            int count = 0;
            char curr = chars[i];

             while(i < chars.length && chars[i] == curr){
                i++;
                count++;
             }

             chars[index++] = curr;
             
             if(count > 1){
                String str = String.valueOf(count);

                for(char c : str.toCharArray()){
                chars[index++] = c;
             }
             }
        }
        return index;
    }
}
