class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev_product = 1
        prefix_product = []
        for num in nums:
            prefix_product.append(prev_product)
            prev_product *= num

        suf_product = 1
        suffix_product = []
        for num in nums[::-1]:
            suffix_product.append(suf_product)
            suf_product *= num

        suffix_product = suffix_product[::-1]

        res = []
        for pref, suf in zip(prefix_product, suffix_product):
            res.append(pref * suf)
        
        return res
