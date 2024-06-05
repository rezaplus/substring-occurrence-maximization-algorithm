def find_max(t, z):
    # Function to find all substrings of a given string
    def get_all_substrings(s):
        substrings = set()
        n = len(s)
        for i in range(n):
            for j in range(i+1, n+1):
                substrings.add(s[i:j])
        return substrings

    # Function to count occurrences of a substring in a string
    def count_occurrences(sub, s):
        count = 0
        start = 0
        while True:
            start = s.find(sub, start)
            if start == -1:
                break
            count += 1
            start += 1  # Move past this occurrence
        return count

    # Get all substrings of t
    substrings = get_all_substrings(t)
    max_value = 0

    # Iterate over each substring and calculate the desired value
    for sub in substrings:
        occurrences = count_occurrences(sub, z)
        max_value = max(max_value, len(sub) * occurrences)

    return max_value

if __name__ == '__main__':
    result = find_max("acldm1labcdhsnd", "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
    print(result)  # Output should be 20
