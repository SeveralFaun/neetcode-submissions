class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            hashmap[n] = i

        for i, n in enumerate(nums):
            dif = target - n
            if dif in hashmap and hashmap[dif] != i:
                return [i, hashmap[dif]]

