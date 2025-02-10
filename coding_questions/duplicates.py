'''
The following function is inefficient. Optimize it for better performance.
def find_duplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and nums[i] not in duplicates:
                duplicates.append(nums[i])
    return duplicates
Task: Rewrite the function to reduce time complexity.

'''
# this function has time complexity of O(n), better than the given function

def get_duplicates(nums):
  exists = set()
  duplicates = []
  for num in nums:
    if num in exists:
        duplicates.append(num)
    else:
      exists.add(num)
  return duplicates

