from parser.yacc import parser
from render import Render
from render.template import TemplateNode

with open('test.md', encoding='utf-8') as file:
    result = parser.parse(file.read())
    for node in result:
        # pass
        print(TemplateNode(node))
    # render = Render()
    # render.render(result)
