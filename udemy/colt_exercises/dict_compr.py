"""
1.
Given two lists:
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
create a dictionary that looks like this:
{'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}
"""
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0, len(list2))}
print(answer)
