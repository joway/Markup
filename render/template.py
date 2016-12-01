import os
import re

from utils.files import get_files_form_dir

TEMPLATES_DIR = os.path.dirname(__file__) + '/templates'


def gen_templates_mapper(directory=TEMPLATES_DIR):
    templates = {}
    for filename in get_files_form_dir(directory=directory):
        with open(directory + '/' + filename, encoding='utf-8') as file:
            templates[filename.split('.html')[0]] = file.read()
    return templates


TEMPLATES_MAPPER = gen_templates_mapper()
FOR_ENDFOR_RE = r'{% for %}(.+?){% endfor %}'


class TemplateNode(object):
    def __init__(self, parsed):
        self._type = parsed['type']
        self._template = TEMPLATES_MAPPER[self._type]

        self._rendered = getattr(self, 'template_%s' % self._type.lower())(parsed)

    def __str__(self):
        return self._rendered

    def replace_value(self, _template, value):
        return re.sub(r'{{ value }}', repl=value, string=_template)

    def get_for_wrapper(self, _template):
        return re.sub(FOR_ENDFOR_RE, repl='%s', string=_template)

    def get_for_child(self, _template):
        return re.findall(FOR_ENDFOR_RE, string=self._template, flags=re.S)[0]

    def template_heading(self, parsed):
        level_replaced = re.sub(r'{{ level }}', repl=str(parsed['level']), string=self._template)
        result = self.replace_value(level_replaced, parsed['values'][0])
        return result

    def template_list(self, parsed):
        li_tmpl = self.get_for_child(self._template)
        wrapper_li = self.get_for_wrapper(self._template)
        lis_html = [self.replace_value(li_tmpl, value) for value in parsed['values']]
        return wrapper_li % ''.join(lis_html)

    def template_olist(self, parsed):
        return self.template_list(parsed)

    def template_ulist(self, parsed):
        return self.template_list(parsed)

    def template_cr(self, parsed):
        return self._template

    def template_line(self, parsed):
        _html = []
        for value in parsed['values']:
            if isinstance(value, dict):
                _html.append(str(TemplateNode(value)))
            else:
                _html.append(value)
        return self.replace_value(self._template, ''.join(_html))

    def template_quote(self, parsed):
        return self.replace_value(self._template, parsed['values'][0])

    def template_bold(self, parsed):
        return self.replace_value(self._template, parsed['values'][0])
