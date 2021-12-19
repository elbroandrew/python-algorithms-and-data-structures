"""
1. LISTS INTERSECTION.
Given two lists [1,2,3,4] and [3,4,5,6], create a variable called 'answer', which is a new
list that is the intersection of the two. Your output should be  [3,4] . Hint: use the 'in' operator to test whether an element is in a list. For example: 5 in [1,5,2] is True. 3 in [1,5,2] is False.
"""

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
answer = [i for i in list1 if i in list2]
print(answer)

"""
2. Given a list of words  ["Elie", "Tim", "Matt"] create a variable called 'answer2' which is a new list with each word reversed and in lower case (use a slice to do the reversal!) Your output should be ['eile', 'mit', 'ttam']'
"""

words = ["Elie", "Tim", "Matt"]
answer2 = [x[::-1].lower() for x in words]
print(answer2)

"""
3. For all the numbers between 1 and 100 (including 100), create a variable called 'answer3', which contains a list with all the numbers that are divisible by 12: (12, 24, etc)
"""
answer3 = [x for x in range(1, 101) if x % 12 == 0]
print(answer3)

"""
4. Given the string, create a variable called 'answer4', which is a list containing all the letters from "amazing", but not the vowels (a, e, i, o, and u). The answer should look like: ['m', 'z', 'n', 'g'].
"""
answer4 = [x for x in "amazing" if x not in "aeiou"]
print(answer4)
