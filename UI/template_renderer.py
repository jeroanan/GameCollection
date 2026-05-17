"""Renders templates using Jinja2."""
from jinja2 import Environment, PackageLoader


class TemplateRenderer:
    """Renders templates using Jinja2."""

    def render(self, template, **args):
        """Renders a template with the given arguments."""
        template = self.__get_template(template)
        return template.render(args)

    def __get_template(self, template):
        env = Environment(loader=PackageLoader("UI.web_server", "markup"))
        return env.get_template(template)
