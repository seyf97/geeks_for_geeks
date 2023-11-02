
class Solution:
    def minDist(self, arr, n, x, y):
        dist = 0
        min_dist = n
        last_is_x = False
        last_is_y = False
        if (x in arr) and (y in arr):
            for i in range(len(arr)):
                if arr[i]==x:
                    if last_is_y:
                        if dist<min_dist:
                            min_dist=dist
                    last_is_x = True
                    last_is_y = False
                    dist=1

                elif arr[i]==y:
                    if last_is_x:
                        if dist<min_dist:
                            min_dist=dist
                    last_is_y = True
                    last_is_x = False
                    dist=1
                else:
                    if last_is_y or last_is_x:
                        dist+=1
            return min_dist
        else:
            return -1


print(Solution().minDist([1,4,2,6,5,1,2,8],8,1,2))