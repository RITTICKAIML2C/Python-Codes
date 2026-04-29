# 1. Function : Count frequency of element in list 
def count_freq(num):
    freq = {}
    for n in num:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    return freq
print(count_freq([1,2,2,3,3,3]))

# 2. Function : find second largest using function
def second_largest(nums):
    largest = nums[0]
    second = nums[0]
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second 
print(second_largest([10,20,30]))

# 3. Function : merge two dictionaries and sum commom keys
def merge_dict(d1, d2):
    result = {}
    for key in d1:
        result[key] = d1[key]
    for key in d2:
        if key in result:
            result[key] += d2[key]
        else:
            result[key] = d2[key]
    return result
print(merge_dict({'a':10, 'b':20}, {'b':30, 'c':40}))

# 4. Function : find all duplicates in a list 
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)
print(find_duplicates([1,2,2,3,4,5,5,6]))

# 5. Function : word frequency in a sentence
def word_frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
print(word_frequency("I love Python I love Coding"))

# 6. Function: group numbers (even & odd)
def even_odd(nums):
    freq = {'even' : [], 'odd' : []}
    for num in nums:
        if num % 2 == 0:
            freq['even'].append(num)
        else:
            freq['odd'].append(num)
    return freq
print(even_odd([1,2,3,4,5]))

# 7. Function : find top scorer from dictionary 
def top_scorer(d):
    topper = max(d, key=d.get)
    return topper, d[topper]
data = {'A':85, 'B':92, 'C':88}
print(top_scorer(data))

# 8. Function : remove duplicates without using set 
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
print(remove_duplicates([1,2,2,3,3,4,5]))

# 9. Function : count vowels using dictionary 
def count_vowels(text):
    vowels = "aeiouAEIOU"
    freq = {}
    for ch in text:
        if ch in vowels:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
    return freq
print(count_vowels("apple"))

# 10. List + Dict + Function 
def analyze_students(students, marks):
    data = dict(zip(students, marks))
    topper = max(data, key=data.get)
    avg = sum(marks) / len(marks)
    below_avg = [name for name in data if data[name] < avg]
    return data, topper, avg, below_avg
students = ["Rittick", "Aman", "Raj"]
marks = [85, 92, 67]
result = analyze_students(students, marks)
print("Dictionary:", result[0])
print("Topper:", result[1])
print("Average:", result[2])
print("Below Average:", result[3])
