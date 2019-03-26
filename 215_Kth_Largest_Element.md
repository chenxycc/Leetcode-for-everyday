#### 采用堆排序

```
from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: 
            return 0
        heap = []
        for i in range(len(nums)):
            heappush(heap,nums[i])
            if len(heap) > k:
                heappop(heap)
        return heap[0]

```
