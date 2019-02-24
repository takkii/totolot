import os
import re
import traceback
from deoplete.source.base import Base
from os.path import expanduser

# ------------------------------- KEYWORD -------------------------------------------------------------------------

home = expanduser("~")
ruby = open(os.path.expanduser("~/.vim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete"))
mini = open(os.path.expanduser("~/.vim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_test_complete"))
unit = open(os.path.expanduser("~/.vim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_test2_complete"))
report = open(os.path.expanduser("~/.vim/repos/github.com/takkii/ruby-dictionary3/autoload/source/minitest_reporter_complete"))
data_ruby = ruby.readlines()
data_mini = mini.readlines()
data_unit = unit.readlines()
data_report = report.readlines()
ruby.close()
mini.close()
unit.close()
report.close()

# ------------------------------- KEYWORD -------------------------------------------------------------------------

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'totolot'
        self.filetypes = ['ruby']
        self.mark = '[Spirit_of_the_Forest]'
        rubymatch = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        regexmatch = [r'[<a-zA-Z(?: .+?)?>.*?<\/a-zA-Z>]']
        self.input_pattern = '|'.join(rubymatch + regexmatch)
        self.rank = 500

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            dic = data_ruby + data_mini + data_unit + data_report
            dict = list(map(lambda s:s.rstrip("\n").dic))
            dict.sort(key=lambda dic: dic[0])
            return dic
        except Exception:
            traceback.print_exc()
