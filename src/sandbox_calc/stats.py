def mean(nums: list[float]) -> float:
    if not nums:
        raise ValueError("Input list cannot be empty")
    return sum(nums) / len(nums)