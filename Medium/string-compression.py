class Solution:
    def compress(self, chars: List[str]) -> int:
        l = len(chars)

        # Return char for single char
        if l == 1:
            return 1
        
        compressed = []
        i = 0

        while i < l:
            # Assigning the char for which we will be counting
            curr = chars[i]
            count = 0 

            # Counting the current character adjacently
            while i < l and chars[i] == curr:
                count += 1
                i += 1
            compressed.append(curr)
            if count > 1:
                compressed.extend(list(str(count)))

        # Modify the chars list in-place
        chars[:len(compressed)] = compressed
        
        return len(compressed)
        

        