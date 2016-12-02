from parser.yacc import parser
from render.template import Template

with open('test.md', encoding='utf-8') as file:
    result = parser.parse(file.read())
    print('----------')
    temp = Template(result)
    print(temp)
    # for i in result:
    #     print(i)
