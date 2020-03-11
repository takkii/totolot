import pandas as pd
from pandas import Series
import os, re, sys, traceback
from os.path import expanduser
from sklearn import svm, metrics
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

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
    print("Needing, ruby-dictionary3.")
    traceback.print_exc()

index_ruby = ruby.readlines()
Seri = pd.Series(index_ruby)
sort_ruby = Seri.sort_index()
tfidf = TfidfVectorizer()
tfidf_vec = tfidf.fit_transform(sort_ruby)

col = tfidf.get_feature_names()
print(pd.DataFrame(tfidf_vec.toarray(), columns=col))

ruby.close()