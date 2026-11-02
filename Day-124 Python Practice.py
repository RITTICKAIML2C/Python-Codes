# 🐍 Q1. Python — Find the First Repeated Element
# Input: [4, 2, 7, 2, 5, 4]
# Output: 2
nums = [4, 2, 7, 2, 5, 4]
seen = set()
for x in nums:    
  if x in seen:        
    print(x)        
    break    
    seen.add(x)

# 🐍 Q2. Python — Find the Third-Largest Unique Number
# Input: [10, 5, 8, 10, 3, 8, 7]
# Output: 7
nums = [10, 5, 8, 10, 3, 8, 7]
unique = sorted(set(nums), reverse=True)
print(unique[2] if len(unique) >= 3 else None)
