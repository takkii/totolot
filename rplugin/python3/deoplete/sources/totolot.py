import os
import re
import traceback
from deoplete.source.base import Base
from os.path import expanduser

# ------------------------------- KEYWORD -------------------------------------------------------------------------

home = expanduser("~")
ruby = open(os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete"))
test = open(os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_test_complete"))
report = open(os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/minitest_reporter_complete"))
rails = open(os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/rails_method_complete"))
index_ruby = ruby.readlines()
index_test = test.readlines()
index_report = report.readlines()
index_rails = rails.readlines()

data_mix = index_ruby + index_test + index_report + index_rails
data_ruby = list(map(lambda s:s.rstrip(),data_mix))

# ------------------------------- KEYWORD -------------------------------------------------------------------------

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'totolot'
        self.filetypes = ['ruby']
        self.mark = '[Do_Your_Best!]'
        rubymatch = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        regexmatch = [r'[<a-zA-Z(?: .+?)?>.*?<\/a-zA-Z>]']
        self.input_pattern = '|'.join(rubymatch + regexmatch)
        self.rank = 500

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            dic = data_ruby
            dic.sort(key=lambda dic: dic[0])
            return dic
        except Exception:
            traceback.print_exc()
        finally:
            data_mix.close