class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\

        l, m , h = 0,0, len(nums)-1

        while m<=h:
            if nums[m] == 0:
                nums[m],nums[l] = nums[l],nums[m]
                m +=1
                l +=1
            elif nums[m] == 1:
                m +=1
            else:
                nums[h],nums[m] = nums[m], nums[h]
                h -= 1


            

            







        