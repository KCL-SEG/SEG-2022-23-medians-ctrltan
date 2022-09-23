"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(nums):
    if len(nums)%2 == 0:
        med = (nums[int(len(nums)/2)] + nums[int((len(nums)/2)-1)])/2
    else:
        med = nums[int((len(nums)-1)/2)]
    return(med)

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

median(numbers)
