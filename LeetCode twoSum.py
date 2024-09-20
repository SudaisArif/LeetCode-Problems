class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    pass
                else:
                    if nums[i] + nums[j] == target:
                        if len(answer) == 0:
                            answer.append(i)
                            answer.append(j)
                        

        return answer
        