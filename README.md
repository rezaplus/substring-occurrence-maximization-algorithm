# Maximum Substring Occurrence Algorithm

## Overview
This algorithm is designed to find the maximum value of a product, where the product is calculated as the length of a substring of a given string `t` multiplied by the number of times that substring occurs in another string `z`.

## Usage
1. **Input**: The algorithm takes two input strings `t` and `z`.
2. **Output**: It returns the maximum value of [length of substring x number of occurrences in `z`] for all substrings of `t`.

## Algorithm Steps
1. Generate all possible substrings of `t`.
2. For each substring, count how many times it occurs in `z`.
3. Calculate the product of the length of the substring and its occurrence count in `z`.
4. Track the maximum product value encountered.
5. Return the maximum product value as the result.

## Example
```python
from max_substring_occurrence import find_max

t = "acldm1labcdhsnd"
z = "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"

result = find_max(t, z)
print(result)  # Output: 20
