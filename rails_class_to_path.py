import sublime, sublime_plugin
import re

# Когда в коде выделено имя ruby-класса, например
# Api::V1::Catalogs::OfferSerializer, плагин копирует в буфер обмена путь
# создаваемый из этого имени: api/v1/catalogs/offer_serializer.
# 
# Плагин запускается по сочетанию клавишь `ctrl+k, ctrl+h`.
class RailsClassToPath(sublime_plugin.WindowCommand):
  def run(self):
    text = self.get_selected()
    text = text.replace('::', '/')
    text = re.sub(r'(?<!^)(?<!/)(?=[A-Z])', '_', text).lower()
    sublime.set_clipboard(text)
    return None

  def get_selected(self):
    view = self.window.active_view()
    sel_region = view.sel()[0]
    selected_text = view.substr(sel_region)
    return selected_text
