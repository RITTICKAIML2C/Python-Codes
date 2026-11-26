# Python 1 — Merge Two Sorted Lists
def merge_sorted(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
print(merge_sorted([1, 3, 5, 7], [2, 4, 6, 8]))

# Python 2 — Find the Longest Word in a Sentence
def longest_word(sentence):
    words = sentence.split()
    if not words:
        return None
    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("Python programming is really interesting"))
