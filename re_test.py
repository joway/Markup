import re

head = """
1. h1
2. h2
* 123
- 321
######## 123
"""
# pat = r'#{1,6}'
pat = r'[\-\*]'
result = re.search(pattern=pat, string=head)
print(result.group())
# for i in result.group():
#     print(i)
