def mean(nums: list[float]) -> float:
    """Return the population mean of a list of numbers."""
    if not nums:
        raise ValueError("mean requires at least one number")
    return sum(nums) / len(nums)