import re

head = """
{% block funciton %}
param string
{% endblock %}
"""
# pat = r'#{1,6}'
pat = r'\{\% block \S+ \%\}([\s\S]*)\{\% endblock \%\}'
result = re.search(pattern=pat, string=head)
print(result.group())
# for i in result.group():
#     print(i)
