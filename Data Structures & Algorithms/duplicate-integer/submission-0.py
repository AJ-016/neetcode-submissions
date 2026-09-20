class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set()
        for n in nums:
            if n in arr:
                return True

            arr.add(n)
        return False