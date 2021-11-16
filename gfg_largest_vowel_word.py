def findSubstring(s, k):
    # Write your code here
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = None
    total = 0
    for i in range(len(s)):
        count = 0
        for letter in s[i:k + i]:
            if letter in vowels:
                count += 1
        if count > total:
            total = count
            words = s[i:k + i]
    return total, words


s = input()
k = int(input().strip())
result = findSubstring(s, k)
print(result)
