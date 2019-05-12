import os
import re
import traceback
import bisect
from deoplete.source.base import Base
from os.path import expanduser

# ------------------------------- KEYWORD -------------------------------------------------------------------------

home = expanduser("~")

with open(os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete"), encoding='utf-8') as w:
    for ruby in w:
        ruby = ruby.rstrip()
        ruby_index = list(ruby.split())
        data_ruby = bisect.bisect_right(ruby_index, ruby)

with open(os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_test_complete"), encoding='utf-8') as q:
    for test in q:
        test = test.rstrip()
        test_index = list(test.split())
        data_test = bisect.bisect_right(test_index, test)

with open(os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/minitest_reporter_complete"), encoding='utf-8') as f:
    for report in f:
        report = report.rstrip()
        report_index = list(report.split())
        data_report = bisect.bisect_right(report_index, report)

with open(os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/rails_method_complete"), encoding='utf-8') as z:
    for rails in z:
        rails = rails.rstrip()
        rails_index = list(rails.split())
        data_rails = bisect.bisect_right(rails_index, rails)

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
            dic = data_ruby + data_test + data_report + data_rails
            return dic
        except Exception:
            traceback.print_exc()
