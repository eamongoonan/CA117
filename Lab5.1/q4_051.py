from sys import stdin

if (__name__ == "__main__"):
    nums = sorted([int(num.strip()) for num in stdin])
    nlen = len(nums)
    mean = sum(nums) / len(nums)
    if nlen % 2:
        median = nums[nlen // 2]
    else:
        median = (nums[nlen // 2] + nums[nlen // 2 - 1]) / 2
    mode = max(
        {num: nums.count(num) for num in nums}.items(),
        key=lambda kv: kv[1]
    )[0]

    print("Mean: {:.1f}".format(mean))
    print("Median: {:.1f}".format(median))
    print("Mode:", mode)
