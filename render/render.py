import os

from render.template import gen_templates_mapper


class Render(object):
    def __init__(self, template_dir=None):
        self.templates = gen_templates_mapper(template_dir) if template_dir else _templates

    def render(self, parsed):
        _html = ''
        for line in parsed:
            template = self.templates[line['type']]

    def render_list(self, template, values):
        for val in values:
            pass
