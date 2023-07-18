def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}

        for i in range(len(nums)):
            if target - nums[i] in nmap:
                return [i, nmap[target - nums[i]]]
            nmap[nums[i]] = i

#O(n)
