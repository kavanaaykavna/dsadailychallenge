class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        hash_table = {}

        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        for num in nums:
            if hash_table[num] == 1:
                return num