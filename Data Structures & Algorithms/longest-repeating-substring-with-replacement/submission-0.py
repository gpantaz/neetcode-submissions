class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        unique_chars = set(s)

        for chara in unique_chars:
            count = left = 0
            for right in range(len(s)):
                if s[right] == chara:
                    count += 1

                while (right - left + 1) - count > k:
                    if s[left] == chara:
                        count -= 1
                    left += 1

                res = max(res, right - left + 1)
        return res

