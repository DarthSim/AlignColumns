import sublime
import sublime_plugin

from text_block import TextBlock, DifferentNumberOfColumnsError, WhiteSpacesError

class AlignColumnsCommand(sublime_plugin.TextCommand):

  def run(self,edit):
    sel = self.view.sel()

    if len(sel) == 1:
      text = self.view.substr(sel[0])
      text_block = TextBlock(text)
      aligned_columns = text_block.align()
      self.view.replace(edit, sel[0], aligned_columns)
    
    elif len(sel) > 1:
      sublime.error_message("Sorry, but I can align only one selection")