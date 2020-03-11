import pandas as pd
from pandas import Series, DataFrame
import os, re, sys, traceback
from os.path import expanduser

# ------------------------------- KEYWORD -------------------------------------------------------------------------


home = expanduser("~")

d1 = os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/ruby-dictionary3/")
d2 = os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/")
d3 = os.path.expanduser("~/.cache/dein/repos/github.com/takkii/ruby-dictionary3/")

if os.path.exists(d1):
    ruby = open(os.path.expanduser(
        "~/.config/nvim/.cache/dein/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete"))
elif os.path.exists(d2):
    ruby = open(os.path.expanduser(
        "~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete"))
elif os.path.exists(d3):
    ruby = open(os.path.expanduser(
        "~/.cache/dein/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete"))
else:
    print('どれにも該当しません、ruby-dictionary3を入れてください。')

index_ruby = ruby.readlines()
Seri = pd.Series(index_ruby)
sort_ruby = Seri.sort_index()
data_ruby = DataFrame(sort_ruby)
# data_ruby = list(map(lambda s: s.rstrip(), sort_ruby))
print(data_ruby)
ruby.close()

# ------------------------------- KEYWORD -------------------------------------------------------------------------
