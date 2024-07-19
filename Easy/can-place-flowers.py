class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        # Counting the numbers of extra flowers that can be planted
        count = 0
        i = 0
        
        while i < l:
            if flowerbed[i] == 0:
                # Determining if previous and next positions are empty
                prevEmpty = (i == 0) or (flowerbed[i-1]==0)
                nextEmpty = (i == l -1) or (flowerbed[i+1]==0)
                # Planting flowers if none at adjacent
                if prevEmpty and nextEmpty:
                    flowerbed[i] = 1
                    count += 1
                    i += 1
                else:
                    i += 1
            else:
                i += 1
        # Checking if given numbers are less than total flowers that can be planted
        if count >= n:
            return True
        return False