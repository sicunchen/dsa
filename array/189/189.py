# solution 1
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        extra = [None]*len(nums)
        for i in range(len(nums)):
            extra[(i+k) % len(nums)] = nums[i]

        for i in range(len(nums)):
            nums[i] = extra[i]

#solution 2 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr,start,end):
            while start<end:
                temp=arr[start]
                arr[start]=arr[end]
                arr[end]=temp
                start,end=start+1,end-1
        k%=len(nums)
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)