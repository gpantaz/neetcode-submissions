class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        array = list(freqs.values())
        
        min_heap = array[:k]
        heapq.heapify(min_heap)

        # Traverse the rest of the array
        for x in array[k:]:
            if x > min_heap[0]:
                heapq.heapreplace(min_heap, x)

        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap))

        res_num = []
        for num, freq in freqs.items():
            if freq in res:
                res_num.append(num)
        return res_num