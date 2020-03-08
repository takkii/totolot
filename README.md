[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)[![GitHub release](https://img.shields.io/github/release/takkii/totolot.svg?style=flat)](GitHub)[![GitHub Status](https://img.shields.io/github/last-commit/takkii/totolot.svg?style=flat)](GitHub)

<div align="center"><img src="https://github.com/takkii/Bignyanco/blob/master/images/python_ruby.gif" alt="Python¤ÈRuby" title="logo"></div>

# Totolot created date [ 2019.01.31 ]

*Made [Python3](https://www.python.org/) (Bignyanco Evolutions)*

#### How To Use

--------------------------------------------------------------------

[ Need [deoplete.nvim](https://github.com/Shougo/deoplete.nvim) ]

```markdown
※ deoplete requires msgpack 1.0.0+.

pip uninstall msgpack-python
pip install msgpack

※ already installed msgpack

pip install -U msgpack

※ totolot HEAD version is numpy needing

pip install numpy

※ Use Installer.

git clone https://github.com/takkii/totolot.git

cd totolot

python install.py
```

### installer setup views.

```
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
Collecting msgpack==1.0.0
  Using cached msgpack-1.0.0-cp37-cp37m-manylinux1_x86_64.whl (275 kB)
Installing collected packages: msgpack
Successfully installed msgpack-1.0.0
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
Collecting numpy==1.18.1
  Using cached numpy-1.18.1-cp37-cp37m-manylinux1_x86_64.whl (20.1 MB)
Installing collected packages: numpy
Successfully installed numpy-1.18.1

<module 'msgpack' from '$HOME/.pyenv/versions/3.7.6/lib/python3.7/site-packages/msgpack/__init__.py'>
<module 'numpy' from '$HOME/.pyenv/versions/3.7.6/lib/python3.7/site-packages/numpy/__init__.py'>
```

### ※ Please setup.

--------------------------------------------------------------------

### Use Vim8/Neovim for totolot env, dein plugin manager.

other you use, ['takkii/Bignyanco'](https://github.com/takkii/Bignyanco).

--------------------------------------------------------------------

totolot [ruby-dictionary3](https://github.com/takkii/ruby-dictionary3) read path.

Conditional branch Transplant from [MinTab](https://github.com/takkii/MinTab).

--------------------------------------------------------------------

### [ Only Use Neovim ]

[dein](https://github.com/Shougo/dein.vim) plugin manager,
use case.

[ init.vim / .vimrc ]

```markdown
call dein#add('takkii/totolot')
call dein#add('takkii/ruby-dictionary3')
```

or

[ dein.toml ]

```markdown
[[plugins]]
repo = 'takkii/totolot'

[[plugins]]
repo = 'takkii/ruby-dictionary3'
```

--------------------------------------------------------------------

#### It is necessary to load ruby-dictionary3.

```markdown

Totolot is Vim8/Neovim Plugins, Vim8 set path '~/.cache/dein'

```

#### totolot Sample picture to views [Do_your_Best!]

![background](https://github.com/takkii/totolot/blob/master/images/background.gif)

#### totolot images icon

![totolot](https://github.com/takkii/totolot/blob/master/images/totolot.gif)

Author Takayuki Kamiyama.
