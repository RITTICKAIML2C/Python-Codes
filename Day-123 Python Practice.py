# 🐍 Q1. Python — Find the Longest Word
# Input: "Python programming is interesting"
# Output: "programming"
text = "Python programming is interesting"
print(max(text.split(), key=len))

# 🐍 Q2. Python — Count Vowels and Consonants
# Input: "programming"
# Output: Vowels: 3, Consonants: 8
s = "programming"
vowels = sum(ch.lower() in "aeiou" for ch in s if ch.isalpha())
consonants = sum(ch.isalpha() and ch.lower() not in "aeiou" for ch in s)
print("Vowels:", vowels, "Consonants:", consonants)
