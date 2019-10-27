import os
import re
import traceback
from deoplete.source.base import Base
from os.path import expanduser

# ------------------------------- KEYWORD -------------------------------------------------------------------------

home = expanduser("~")

d1 = os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/")
d2 = os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/ruby-dictionary3/")

if os.path.exists(d1):
    ruby = open(os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete"))
elif os.path.exists(d2):
    ruby = open(os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete"))
else:
    print('どれにも該当しません、ruby-dictionary3を入れてください。')

index_ruby = ruby.readlines()
data_ruby = list(map(lambda s:s.rstrip(),index_ruby))
ruby.close()

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