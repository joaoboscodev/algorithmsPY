def is_valid_input(nums):
    return isinstance(nums, list) and nums and all(
        isinstance(num, int) and num >= 0 for num in nums)


def sort_nums(nums):
    return sorted(nums)


def find_duplicate_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]
    return False


def find_duplicate(nums):
    if not is_valid_input(nums):
        return False

    if len(nums) == 1:
        return False

    sorted_nums = sort_nums(nums)
    return find_duplicate_sorted(sorted_nums)
