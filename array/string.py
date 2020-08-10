# serialization
bfs_order = ['1', '2', '3', '#', '#', '5']
print("[%s]" % ','.join(bfs_order))  # "[1,2,3,#,#,5]" <class 'str'>

# deserialization
data = "[%s]" % ','.join(bfs_order)
print(data[1:-1].split(','))  # ['1', '2', '3', '#', '#', '5'] <class 'list'>

# string ignoring cases
s = "A man, a plan, a canal: Panama"
string = ''.join(char.lower() for char in s if char.isalpha() or char.isdigit())
print(string)

import re
string = re.sub(r'[^A-Za-z0-9]', '', s).lower()
print(string)

# strStr indexOf
source = "abcdabcdefg"
target = "bcd"
print(source.index(target))

