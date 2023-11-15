for _ in range(int(input())):
    s = input().strip()
    n = len(s)

    # Count the frequency of each letter
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1

    # Find the most frequent letter
    max_freq = 0
    max_char = ''
    for i in range(26):
        if freq[i] > max_freq:
            max_freq = freq[i]
            max_char = chr(i + ord('a'))

    # Remove all the letters that are not equal to the most frequent letter
    s = ''.join(c for c in s if c == max_char)

    # Remove adjacent letters
    ans = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            ans += 1
    ans = (ans + 1) // 2
    print(ans)
