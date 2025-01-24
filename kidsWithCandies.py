"""
Determines if each child can have the greatest number of candies after receiving extra candies.
Args:
    candies (list[int]): A list of integers representing the number of candies each child has.
    extraCandies (int): An integer representing the number of extra candies to be given to each child.
Returns:
    list[bool]: A list of boolean values where each value indicates whether the corresponding child can have the greatest number of candies after receiving the extra candies.
"""

candies = [2,3,5,1,3]
def kidsWithCandies(candies : list[int], extraCandies: int)->list[bool]:
    max_candies = max(candies)
    result = []
    for i in candies:
        if i + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result
p = kidsWithCandies(candies, 3)

print(p)

