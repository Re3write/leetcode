# public int search(int[] nums, int target) {
# 		int start = 0;
# 		int end = nums.length - 1;
# 		while (start <= end) {
# 			int mid = (start + end) / 2;
# 			if (target == nums[mid]) {
# 				return mid;
# 			}
#             左半段是有序的
# 			if (nums[start] <= nums[mid]) {
#                 target 在这段里
# 				if (target >= nums[start] && target < nums[mid]) {
# 					end = mid - 1;
# 				} else {
# 					start = mid + 1;
# 				}
#             右半段是有序的
# 			} else {
# 				if (target > nums[mid] && target <= nums[end]) {
# 					start = mid + 1;
# 				} else {
# 					end = mid - 1;
# 				}
# 			}
#
# 		}
# 		return -1;
# 	}

#python版二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
