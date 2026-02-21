import sublime
import sublime_plugin
import re

class RailsClassToPathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                continue

            original = self.view.substr(region)
            converted = self.convert(original)
            self.view.replace(edit, region, converted)

    def convert(self, text):
        text = text.strip()

        # Path -> Class
        if text.startswith('/') or text[0].islower():
            return self.path_to_class(text)

        # Class -> Path
        if text.startswith('::') or text[0].isupper():
            return self.class_to_path(text)

        return text

    def class_to_path(self, text):
        text = text.replace('::', '/')
        text = re.sub(r'(?<!^)(?<!/)(?=[A-Z])', '_', text).lower()
        return text

    def path_to_class(self, text):
        absolute = text.startswith('/')
        text = text.lstrip('/')

        parts = text.split('/')
        parts = [self.snake_to_camel(p) for p in parts if p]

        result = '::'.join(parts)

        if absolute:
            result = '::' + result

        return result

    def snake_to_camel(self, word):
        return ''.join(part.capitalize() for part in word.split('_'))
