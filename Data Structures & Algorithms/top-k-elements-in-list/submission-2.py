class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        array = list(freqs.values())
        
        min_heap = array[:k]
        heapq.heapify(min_heap)

        heap = []
        for num in freqs.keys():
            heapq.heappush(heap, (freqs[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res