def average(numbers):
    """Return the mean of a list of numbers."""
    return sum(numbers) / len(numbers)  


def median(numbers):
    """Return the median of a list of numbers."""
    s = sorted(numbers)
    mid = len(s) // 2
    return s[mid]                      
