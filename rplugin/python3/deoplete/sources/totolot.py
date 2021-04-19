import os
import re
from operator import itemgetter

import numpy as np
from deoplete.source.base import Base
from numba import njit


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'totolot'
        self.filetypes = ['ruby']
        self.mark = '[ruby-dictionary3]'
        rubymatch = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        regexmatch = [r'[<a-zA-Z(?: .+?)?>.*?<\/a-zA-Z>]']
        self.input_pattern = '|'.join(rubymatch + regexmatch)
        self.rank = 500

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    @njit
    def numba_numpy_dataframe(self, context):
        try:
            rel_path = "repos/github.com/takkii/ruby-dictionary3/"

            paths = [os.path.expanduser(os.path.join(p, rel_path)) for p in [
                "~/.cache/dein/",
                "~/.local/share/dein/",
                "~/.config/nvim/.cache/dein/",
                "~/.config/nvim/",
                "~/.vim/bundles"
            ]]

            path = next(p for p in paths if os.path.exists(p))

            ruby_method = open(os.path.join(path, "autoload/source/ruby_method_deoplete"))
            rubymotion_method = open(os.path.join(path, "autoload/source/rubymotion_method"))
            rurima_list = open(os.path.join(path, "autoload/source/rurima_list"))

            index_ruby = list(ruby_method.readlines()) + list(rubymotion_method.readlines()) + list(
                rurima_list.readlines())

            sort_ruby = np.array(index_ruby).tolist()
            data_ruby = list(map(lambda s: s.rstrip(), sort_ruby))
            ruby_method.close()
            rubymotion_method.close()

            # sort and itemgetter
            dic = data_ruby
            dic.sort(key=itemgetter(0))
            return dic

        except StopIteration:
            print("Don't forget, Install dein plugin manager github repo takkii/ruby-dictionary3.")

    def gather_candidates(self, context):
        try:
            (self, context).numba_numpy_dataframe(self, context)
        except Exception:
            print("catch Exception throw ...")
